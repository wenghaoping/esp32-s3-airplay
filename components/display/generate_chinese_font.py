#!/usr/bin/env python3
"""Generate a complete GB2312 LVGL bitmap font from the bundled WQY BDF.

The source font is already part of the u8g2 component and includes the
complete GB2312 character set. Run from any directory; no Python packages are
required. The output is committed so firmware builds do not run this script.
"""

from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "u8g2/tools/font/bdf/wenquanyi_13px.bdf"
OUTPUT = HERE / "font_wqy14_gb2312.c"


def allowed_codepoints():
    chars = set(range(0x20, 0x7F))
    for high in range(0xA1, 0xF8):
        for low in range(0xA1, 0xFF):
            try:
                chars.add(ord(bytes((high, low)).decode("gb2312")))
            except UnicodeDecodeError:
                pass
    chars.update(ord(c) for c in "？—…·“”‘’￥")
    # These two GB2312 punctuation code points are absent from the bundled
    # BDF; LVGL's fallback font supplies them.
    chars.difference_update((0x2015, 0x30FB))
    return chars


def parse_bdf():
    allowed = allowed_codepoints()
    glyphs = {}
    lines = SOURCE.read_text(encoding="latin-1").splitlines()
    i = 0
    while i < len(lines):
        if not lines[i].startswith("STARTCHAR "):
            i += 1
            continue
        code = None
        advance = 16
        box = (0, 0, 0, 0)
        rows = []
        i += 1
        while i < len(lines) and lines[i] != "ENDCHAR":
            line = lines[i]
            if line.startswith("ENCODING "):
                code = int(line.split()[1])
            elif line.startswith("DWIDTH "):
                advance = int(line.split()[1])
            elif line.startswith("BBX "):
                box = tuple(map(int, line.split()[1:5]))
            elif line == "BITMAP":
                width, height, _, _ = box
                rows = lines[i + 1 : i + 1 + height]
                i += height
            i += 1
        if code in allowed and code not in glyphs:
            glyphs[code] = (advance, box, rows)
        i += 1
    missing = allowed - glyphs.keys()
    if missing:
        raise SystemExit(f"BDF is missing {len(missing)} GB2312 glyphs")
    return glyphs


def packed_bitmap(width, height, rows):
    bits = []
    for row in rows:
        value = int(row, 16)
        padded_width = len(row) * 4
        bits.extend((value >> (padded_width - x - 1)) & 1 for x in range(width))
    bits.extend([0] * ((8 - len(bits) % 8) % 8))
    return bytes(
        sum(bits[i + j] << (7 - j) for j in range(8))
        for i in range(0, len(bits), 8)
    )


def main():
    glyphs = parse_bdf()
    codes = sorted(glyphs)
    bitmap = bytearray()
    desc = ["{.bitmap_index=0,.adv_w=0,.box_w=0,.box_h=0,.ofs_x=0,.ofs_y=0}"]
    for code in codes:
        advance, (width, height, x, y), rows = glyphs[code]
        desc.append(
            f"{{.bitmap_index={len(bitmap)},.adv_w={advance * 16},"
            f".box_w={width},.box_h={height},.ofs_x={x},.ofs_y={y}}}"
        )
        bitmap.extend(packed_bitmap(width, height, rows))

    def chunks(items, n):
        for start in range(0, len(items), n):
            yield items[start : start + n]

    with OUTPUT.open("w") as out:
        out.write("/* Generated from WenQuanYi Bitmap Song (GPLv2 with font embedding exception).\n"
                  " * Complete GB2312 plus ASCII and common punctuation.\n"
                  " * Regenerate with components/display/generate_chinese_font.py. */\n"
                  '#include "lvgl.h"\n\n')
        out.write("static const uint8_t glyph_bitmap[] = {\n")
        for chunk in chunks(list(bitmap), 20):
            out.write("  " + ",".join(f"0x{x:02x}" for x in chunk) + ",\n")
        out.write("};\n\nstatic const lv_font_fmt_txt_glyph_dsc_t glyph_dsc[] = {\n")
        for item in desc:
            out.write("  " + item + ",\n")
        out.write("};\n\nstatic const uint16_t unicode_list[] = {\n")
        for chunk in chunks([c - codes[0] for c in codes], 16):
            out.write("  " + ",".join(str(x) for x in chunk) + ",\n")
        out.write("};\n\nstatic const lv_font_fmt_txt_cmap_t cmaps[] = {{\n"
                  f"  .range_start={codes[0]},.range_length={codes[-1] - codes[0] + 1},\n"
                  f"  .glyph_id_start=1,.unicode_list=unicode_list,.list_length={len(codes)},\n"
                  "  .type=LV_FONT_FMT_TXT_CMAP_SPARSE_TINY\n}};\n\n"
                  "static const lv_font_fmt_txt_dsc_t font_dsc = {\n"
                  "  .glyph_bitmap=glyph_bitmap,.glyph_dsc=glyph_dsc,.cmaps=cmaps,\n"
                  "  .cmap_num=1,.bpp=1,.bitmap_format=0\n};\n\n"
                  "const lv_font_t font_wqy14_gb2312 = {\n"
                  "  .get_glyph_dsc=lv_font_get_glyph_dsc_fmt_txt,\n"
                  "  .get_glyph_bitmap=lv_font_get_bitmap_fmt_txt,\n"
                  "  .line_height=16,.base_line=3,.dsc=&font_dsc,\n"
                  "  .fallback=&lv_font_montserrat_14\n};\n")
    print(f"Wrote {OUTPUT}: {len(codes)} glyphs, {len(bitmap)} bitmap bytes")


if __name__ == "__main__":
    main()
