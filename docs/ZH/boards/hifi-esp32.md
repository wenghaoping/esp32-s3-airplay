# HiFi-ESP32 和 HiFi-Esparagus

该 Sonocotta [HiFi-ESP32](https://github.com/sonocotta/esp32-audio-dock) 开发板 pair an
ESP32 或 ESP32-S3 与 a TI **PCM5100** I2S DAC 和 a line-level output. There 是 no
amplifier on 开发板, so these feed an existing amp 或 a pair of active 音箱.

该 PCM5100 是 a plain I2S DAC: no I2C 控制 port, no mute pin 和 no hardware 音量
register. 该 firmware therefore does 音量 in software 和 该 开发板 support code has
nothing to do beyond bringing up 该 SPI bus that 以太网 和 该 显示 share.

## Variants

| Environment | Chip | 以太网 | Display | 蓝牙 | Prebuilt |
| --- | --- | :-: | :-: | :-: | :-: |
| `hifi-esp32` | ESP32 | yes | SH1106 OLED | — | — |
| `hifi-esp32-bt` | ESP32 | yes | SH1106 OLED | yes | yes |
| `hifi-esparagus` | ESP32 | — | — | — | — |
| `hifi-esparagus-bt` | ESP32 | — | — | yes | yes |
| `hifi-esp32-s3` | ESP32-S3 | yes | SH1106 OLED | — | yes |
| `hifi-esparagus-s3` | ESP32-S3 | — | — | — | yes |

该 **Esparagus** variants 是 该 相同 音频 design 无需 该 以太网 jack 和 该
显示 header; they carry a WS2812 status LED instead. 蓝牙 Classic exists 仅 on
该 original ESP32, so there 是 no `-bt` 构建 用于 either S3 variant.

On an ESP32 该 published binary 是 该 蓝牙 one. 构建 `hifi-esp32` 或
`hifi-esparagus` yourself if you would rather have 该 RAM 和 刷写 back.

## 功能特性

- PCM5100 line-level DAC, all 8 MB 刷写
- Software 音量 控制 — 该 DAC has no 音量 register
- [蓝牙 A2DP](../features/bluetooth.md) on the ESP32 variants
- [W5500 SPI 以太网](../features/ethernet.md) 与 automatic WiFi failover, on 该
  non-Esparagus variants
- [SH1106 OLED](../features/oled-display.md) 通过 SPI, sharing 该 以太网 bus, on 该
  non-Esparagus variants

## 刷写固件

=== "Browser"

    Use 该 HiFi installer 用于 your 开发板 on 该
    [刷写 页面](../getting-started/flashing.md).

=== "PlatformIO"

    ```bash
    # ESP32 — AirPlay + Bluetooth + Ethernet + OLED
    pio run -e hifi-esp32-bt -t upload
    pio run -e hifi-esp32-bt -t uploadfs

    # ESP32 — Esparagus variant, AirPlay + Bluetooth over WiFi
    pio run -e hifi-esparagus-bt -t upload
    pio run -e hifi-esparagus-bt -t uploadfs

    # ESP32-S3 — AirPlay + Ethernet + OLED
    pio run -e hifi-esp32-s3 -t upload
    pio run -e hifi-esp32-s3 -t uploadfs

    # ESP32-S3 — Esparagus variant
    pio run -e hifi-esparagus-s3 -t upload
    pio run -e hifi-esparagus-s3 -t uploadfs
    ```

=== "ESP-IDF"

    ```bash
    idf.py set-target esp32
    idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.hifi-esp32;config/sdkconfig.defaults.bt" build
    idf.py -p /dev/ttyUSB0 flash
    ```

    Swap in `config/sdkconfig.defaults.hifi-esp32-s3` after `idf.py set-target esp32s3`
    用于 该 S3 revision, 和 drop `config/sdkconfig.defaults.bt` 用于 a 构建 无需
    蓝牙.

## Default GPIO assignments

| 功能 | ESP32 | ESP32-S3 | 说明 |
| --- | :-: | :-: | --- |
| I2S BCK | 26 | 14 | 位时钟 |
| I2S WS | 25 | 15 | 字选择时钟 (LRCLK) |
| I2S DO | 22 | 16 | 串行音频数据 |
| I2S MCLK | — | — | Not used; 该 PCM5100 recovers its own clock |
| Status LED | 33 | 9 | Addressable RGB, Esparagus variants 仅 |
| SPI SCLK | 18 | 12 | Shared by 以太网 和 显示 |
| SPI MOSI | 23 | 11 | Shared by 以太网 和 显示 |
| SPI MISO | 19 | 13 | 以太网 仅 |
| 以太网 CS | 5 | 10 | W5500 |
| 以太网 INT | 35 | 6 | W5500 |
| 以太网 RST | 14 | 5 | W5500 |
| Display CS | 15 | 39 | SH1106 OLED |
| Display DC | 4 | 40 | SH1106 OLED |
| Display RST | 32 | 38 | SH1106 OLED |

该 Esparagus variants 使用 该 相同 I2S pins 和 leave 该 SPI block unconfigured.

## Related

- [Loud-ESP32](loud-esp32.md) — 该 相同 layout 与 MAX98357A amplifiers on 开发板
- [Amped-ESP32](amped-esp32.md) — a PCM5100 与 a TPA31xx amplifier behind it
- [蓝牙 A2DP](../features/bluetooth.md)
- [以太网 (W5500)](../features/ethernet.md)
- [构建环境](../reference/build-environments.md)
