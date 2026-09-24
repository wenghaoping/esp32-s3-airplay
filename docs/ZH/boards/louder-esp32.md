# Louder-ESP32 和 Louder-ESP32-Plus

该 Sonocotta [Louder-ESP32](https://github.com/sonocotta/esp32-audio-dock) 开发板 carry a
TI **TAS58xx** combined DAC 和 Class-D amplifier, 该 相同 family 该
[Esparagus Audio Brick](esparagus-audio-brick.md) 使用. Speakers 连接 直接.

该 **Plus** 开发板 是 fitted 与 a **TAS5825M**; 该 plain 开发板 与 a **TAS5805M**.
Both 是 driven by 该 相同 驱动, 该 reads 该 die ID at startup, so 该 difference
是 what 该 part 可以 do rather than 该 构建 you 刷写:

- 音量, mute 和 该 15-band parametric [Equaliser](esparagus-audio-brick.md#equaliser)
  工作 on 两者 parts.
- Process flows 和 完整 PPC3 dumps 是 a **TAS5825M** feature. A TAS5805M has no
  flow-选择 register, so 该 驱动 skips a dump rather than 写入 it to 该 wrong
  place. See [TAS5805M 开发板](esparagus-audio-brick.md#tas5805m-boards).

音量 是 done in 该 amplifier (`CONFIG_DAC_CONTROLS_VOLUME`) rather than in software.

## Variants

| Environment | Chip | 功放 | 蓝牙 | Prebuilt |
| --- | --- | --- | :-: | :-: |
| `louder-esp32` | ESP32 | TAS5805M | — | — |
| `louder-esp32-bt` | ESP32 | TAS5805M | yes | yes |
| `louder-esp32-plus` | ESP32 | TAS5825M | — | — |
| `louder-esp32-plus-bt` | ESP32 | TAS5825M | yes | yes |
| `louder-esp32-s3` | ESP32-S3 | TAS5805M | — | yes |
| `louder-esp32-s3-plus` | ESP32-S3 | TAS5825M | — | yes |

蓝牙 Classic exists 仅 on the original ESP32, so neither S3 开发板 has a `-bt`
构建. On an ESP32 该 published binary 是 该 蓝牙 one.

!!! 注意 "Esparagus Louder 是 a separate 开发板"

    该 [Esparagus Louder](esparagus-audio-brick.md#esparagus-louder) 是 该 相同
    amplifier family on Sonocotta's Esparagus form factor 和 has its own 环境
    (`esparagus-louder`, `-bt`, `-s3`). Its ESP32 构建 differs 从 `louder-esp32` in
    pinout: it has a FAULTZ line 和 an RGB LED, 和 no `PDN` pin.

## 功能特性

- TAS5825M 或 TAS5805M 与 on-芯片 DSP 和 a 15-band parametric EQ (25 Hz – 16 kHz)
- Hardware 音量 控制 与 a configurable maximum level
- Automatic power state management driven by AirPlay session state
- 8 MB 刷写
- [蓝牙 A2DP](../features/bluetooth.md) on the ESP32 variants
- [W5500 SPI 以太网](../features/ethernet.md) 与 automatic WiFi failover
- [SH1106 OLED](../features/oled-display.md) 通过 SPI, sharing 该 以太网 bus

## 刷写固件

=== "Browser"

    Use 该 Louder installer 用于 your 开发板 on 该
    [刷写 页面](../getting-started/flashing.md).

=== "PlatformIO"

    ```bash
    # ESP32 + TAS5805M
    pio run -e louder-esp32-bt -t upload
    pio run -e louder-esp32-bt -t uploadfs

    # ESP32 + TAS5825M
    pio run -e louder-esp32-plus-bt -t upload
    pio run -e louder-esp32-plus-bt -t uploadfs

    # ESP32-S3 + TAS5805M
    pio run -e louder-esp32-s3 -t upload
    pio run -e louder-esp32-s3 -t uploadfs

    # ESP32-S3 + TAS5825M
    pio run -e louder-esp32-s3-plus -t upload
    pio run -e louder-esp32-s3-plus -t uploadfs
    ```

=== "ESP-IDF"

    ```bash
    idf.py set-target esp32
    idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.louder-esp32-plus;config/sdkconfig.defaults.bt" build
    idf.py -p /dev/ttyUSB0 flash
    ```

    Swap in `config/sdkconfig.defaults.louder-esp32-s3-plus` after
    `idf.py set-target esp32s3` 用于 该 S3 revision.

## Default GPIO assignments

该 ESP32 和 S3 revisions share no pinout. 该 Plus 开发板 differ 从 该 plain ones
仅 in 该 以太网 芯片 选择 和 该 OLED 芯片 选择.

| 功能 | Louder-ESP32 | Louder-ESP32-Plus | ESP32-S3 (两者) |
| --- | :-: | :-: | :-: |
| I2S BCK | 26 | 26 | 14 |
| I2S WS | 25 | 25 | 15 |
| I2S DO | 22 | 22 | 16 |
| I2C SDA | 21 | 21 | 8 |
| I2C SCL | 27 | 27 | 9 |
| 功放 `PDN` | 33 | 33 | 17 |
| SPI SCLK | 18 | 18 | 12 |
| SPI MOSI | 23 | 23 | 11 |
| SPI MISO | 19 | 19 | 13 |
| 以太网 CS | 5 | 15 | 10 |
| 以太网 INT | 35 | 35 | 6 |
| 以太网 RST | 14 | 14 | 5 |
| Display CS | 15 | 5 | 47 |
| Display DC | 4 | 4 | 38 |
| Display RST | 32 | 32 | 48 |

`PDN` 是 driven high once at boot 和 then left alone — it 是 该 amplifier's power-down
pin, not 该 per-track mute 该 [Loud](loud-esp32.md) 和 [Amped](amped-esp32.md) 开发板
toggle 从 播放 events.

## Related

- [Esparagus Audio Brick](esparagus-audio-brick.md) — 该 相同 TAS58xx 驱动, EQ 和 PPC3 workflow
- [HybridFlow DSP](../features/hybridflow.md)
- [蓝牙 A2DP](../features/bluetooth.md)
- [以太网 (W5500)](../features/ethernet.md)
- [构建环境](../reference/build-environments.md)
