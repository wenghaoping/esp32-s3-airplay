# SPIFFS filesystem

该 firmware keeps its web 页面 和 DAC configuration 文件 on a **SPIFFS partition** in
刷写, so you 可以 更新 该 web UI 和 DSP programs 无需 recompiling.

## Partition layout

A `storage` partition 是 added to 该 partition table:

| Board | Partition size | Address |
| --- | --- | --- |
| SqueezeAMP (8 MB 或 更多) | 316 KB | 0x5B1000 |
| SqueezeAMP 4M | 192 KB | 0x3D1000 |

It 是 mounted at `/spiffs` on boot.

## Data 目录

`data/` in 该 项目 root holds 该 文件 that get flashed to 该 partition:

```text
data/
├── www/               # Web interface pages
│   ├── index.html     # Setup and control panel
│   ├── logs.html      # Live log viewer
│   ├── bq.html        # Parametric biquad chains (TAS5825M boards)
│   ├── hf.html        # Hybrid flow tuning (SqueezeAMP)
│   └── speedtest.html # Network throughput test
├── hf/                # DSP programs loaded at boot
│   ├── base-hf1-44100.bin  # Hybrid flow 1 base image (SqueezeAMP)
│   ├── base-hf3-44100.bin  # Hybrid flow 3 base image (SqueezeAMP)
│   └── tas5825m_fw-44100.bin # PPC3 dump, if you supply one (TAS5825M boards)
└── bg/                # ST7789 background image
    └── background.bin  # if you supply one
```

该 `hf/` names carry 该 sample rate 该 DSP image 是 构建 用于, 和 a 48000 twin sits
beside 每个. Only 该 hybrid flow base images ship 与 该 repository; a PPC3 dump 是
yours to export 和 drop in, as 是 该 background image — at 106 KB it does not fit
alongside 该 web UI on a 4 MB 开发板.

## Compression

`data/` 是 not flashed verbatim. `scripts/gen_spiffs_image.py` stages it 首次 和 gzips
每个 `.html`, so 该 image holds `index.html.gz` rather than `index.html`. That takes 该
payload 从 256 KB to 101 KB, 该 matters because 该 smallest layout gives SPIFFS 仅
188 KB — 该 页面 alone overflow it uncompressed. Pages 也 load noticeably faster 通过
WiFi.

该 image 仅 ever stores 该 `.gz`, so 该 web server tries 该 plain name 首次 和 falls
back to `<path>.gz`, 设置 `Content-Encoding: gzip` 当 it serves one; browsers
decompress transparently. That order 是 what 使 `/api/fs/upload` useful — an uploaded
`index.html` replaces 该 页面 that shipped, 和 deleting it again restores 该 构建-in
one. 该 `hf/` 和 `bg/` binaries 是 读取 straight off 该 filesystem by 该 DAC 和
显示 drivers, 该 无法 decompress, so they 是 copied through untouched.

Staging 也 drops what a 构建 无法 使用. Both DAC drivers keep their DSP images in
`hf/`, so 每个 构建 carries 仅 该 family it 可以 load: `base-hf*.bin` 和
`tas57xx_fw*.bin` 需要 `CONFIG_DAC_TAS57XX`, `tas5825m_fw*.bin` 需要 `CONFIG_DAC_TAS58XX`.
That hands another 24 KB back to any 开发板 无需 a TAS57xx, taking 该 image to 78 KB.

Both 构建 systems go through that staging step. ESP-IDF runs it 从 `CMakeLists.txt`
before `spiffs_create_partition_image`, 和 PlatformIO — 该 packs `data/` itself rather
than 使用 该 image CMake builds — runs it 从 `scripts/pio_stage_spiffs.py`, wired in as
an `extra_scripts` hook. So `idf.py flash`, `pio run -t uploadfs` 和 该 prebuilt 发布版本
binaries all end up 与 该 相同 filesystem.

## 刷写固件 该 image

!!! 警告 "PlatformIO does not do this 用于 you"

    `pio run -t upload` writes 该 firmware 仅. Without a separate `-t uploadfs`, 该
    设备 boots but 该 captive portal 和 web UI 是 missing, 该 显示 up as
    "文件 not found" during setup. 此 是 该 single most 常用 setup problem.

```bash
# PlatformIO — firmware first, then the filesystem
pio run -e <env> -t upload
pio run -e <env> -t uploadfs

# ESP-IDF — firmware, partition table and SPIFFS in one step
idf.py -p /dev/ttyUSB0 flash
```

**Upgrading 从 a 构建 无需 该 storage partition** must be done 通过 serial. 该
partition table itself changes, 和 OTA 无法 rewrite it.

Once 该 partition exists you 可以 更新 individual 文件 通过 WiFi 与 该 API below, 或
re-刷写 该 whole image 通过 serial.

## File management API

Three HTTP endpoints manage SPIFFS 文件 通过 WiFi 无需 reflashing.

**上传 a 文件:**

```bash
curl -X POST "http://<device-ip>/api/fs/upload?path=/spiffs/hf/my_flow.bin" \
     --data-binary @my_flow.bin
```

**Delete a 文件:**

```bash
curl -X POST "http://<device-ip>/api/fs/delete?path=/spiffs/hf/old_flow.bin"
```

**List a 目录:**

```bash
curl "http://<device-ip>/api/fs/list?dir=/spiffs/hf"
```

Paths 是 restricted to `/spiffs/` 和 目录 traversal via `..` 是 rejected. 该
maximum upload size 是 64 KB.

## What lives on SPIFFS

| Path | Used by |
| --- | --- |
| `/spiffs/www/` | Web server — setup portal, logs, equaliser |
| `/spiffs/hf/base-hf<n>-<rate>.bin` | [HybridFlow DSP](../features/hybridflow.md) |
| `/spiffs/hf/tas5825m_fw-<rate>.bin` | [Full PPC3 tuning](../boards/esparagus-audio-brick.md#full-ppc3-tuning) |
| `/spiffs/bg/background.bin` | [ST7789 background image](../features/tft-display.md#background-image) |
