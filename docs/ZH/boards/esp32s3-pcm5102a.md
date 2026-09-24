# ESP32-S3 + PCM5102A

该 cheapest 和 most 常用 构建: a generic ESP32-S3 dev 开发板 与 an external
PCM5102A I2S DAC plugged straight onto its pins. 此 是 该 默认 构建 环境
(`esp32s3`) 和 该 configuration 该 项目 是 developed against.

For 该 parts list 和 step-by-step assembly, see
[shopping list](../getting-started/shopping-list.md) 和
[assembly](../getting-started/assembly.md).

## Default I2S pins

| 功能 | GPIO | PCM5102A pin |
| --- | --- | --- |
| 位时钟 | 11 | BCK |
| Audio data | 12 | DIN |
| 字选择时钟 (LRCLK) | 13 | LCK |
| Software ground | 14 | GND |
| Power | 5V | VIN |

MCLK 是 not needed by 该 PCM5102A, 该 generates it internally. It 是 nonetheless
routed to GPIO8 by 默认, 该 是 useful if you want to drive a 不同 converter
such as a WM8805 I2S-to-S/PDIF bridge.

Pins 可以 be changed under **Board 配置 → Pin 配置** in `menuconfig`.

!!! 警告 "Bridge VIN/VOUT"

    Most ESP32-S3 开发板 ship 与 该 VIN/VOUT solder pads open. Bridge them, 或 该
    DAC gets no 5 V power 和 you hear nothing.

## 刷写固件

=== "Browser"

    Use 该 installer on the [刷写 页面](../getting-started/flashing.md).

=== "PlatformIO"

    ```bash
    pio run -e esp32s3 -t upload
    pio run -e esp32s3 -t uploadfs
    ```

    该 第二 命令 是 需要 — it writes 该 web UI to SPIFFS.

=== "ESP-IDF"

    ```bash
    idf.py set-target esp32s3
    idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.esp32s3" build
    idf.py -p /dev/ttyUSB0 flash
    ```

## No 蓝牙 on the S3

该 ESP32-S3 has 蓝牙 LE 仅, not 蓝牙 Classic, so A2DP 音频 是 not 可用.
该 `esp32s3` 构建 contains no 蓝牙 support at all. Use an ESP32-based 开发板 such as
该 [SqueezeAMP](squeezeamp.md) 或 [Esparagus Audio Brick](esparagus-audio-brick.md) if you
want to 流 通过 蓝牙.

## Variants

### Waveshare ESP32-S3

Waveshare's ESP32-S3 开发板 使用 a 不同 pin arrangement 和 have their own 环境
和 prebuilt binary:

```bash
pio run -e waveshare-esp32s3 -t upload
pio run -e waveshare-esp32s3 -t uploadfs
```

### JTAG debugging

`esp32s3-jtag` extends 该 `esp32s3` 环境 和 uploads 通过 该 构建-in USB JTAG
bridge instead of 该 serial bootloader:

```bash
pio run -e esp32s3-jtag -t upload
```

### ESP32-S2

An ESP32-S2 构建 是 produced in CI 和 published as
`airplay2-receiver-esp32s2.bin`, flashable 从 该
[browser installer](../getting-started/flashing.md). There 是 no PlatformIO 环境 用于
it — 构建 it through ESP-IDF:

```bash
idf.py set-target esp32s2
idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.esp32s2" build
```

### ESP32-WROVER

For older WROVER modules 与 4 MB 刷写, `esp32wrover-dev` targets 该 Freenove WROVER
开发板 和 includes 蓝牙:

```bash
pio run -e esp32wrover-dev -t upload
```
