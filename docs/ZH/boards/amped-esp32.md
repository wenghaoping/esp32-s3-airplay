# Amped-ESP32 和 Amped-Esparagus

该 Sonocotta [Amped-ESP32](https://github.com/sonocotta/esp32-audio-dock) 开发板 put a
**PCM5100** I2S DAC in front of a **TPA3110** 或 **TPA3128** Class-D amplifier. Speakers
连接 直接 to 该 开发板, but unlike 该 [Loud](loud-esp32.md) 开发板 该 signal
passes through a real DAC 首次.

Neither part has an I2C 控制 port. 该 amplifier's 仅 控制 line 是 an active-high
`UNMUTE` pin, driven 从 RTSP 播放 events by 该 相同 开发板 support code 该 Loud
开发板 使用: muted until a client presses play, standby on pause, off on disconnect.

## Variants

| Environment | Chip | 以太网 | Display | Controls | 蓝牙 | Prebuilt |
| --- | --- | :-: | :-: | --- | :-: | :-: |
| `amped-esp32` | ESP32 | yes | SH1106 OLED | — | — | — |
| `amped-esp32-bt` | ESP32 | yes | SH1106 OLED | — | yes | yes |
| `amped-esparagus` | ESP32 | yes | — | rotary encoder | — | — |
| `amped-esparagus-bt` | ESP32 | yes | — | rotary encoder | yes | yes |
| `amped-esp32-s3` | ESP32-S3 | yes | SH1106 OLED | — | — | yes |

蓝牙 Classic exists 仅 on the original ESP32, so there 是 no `-bt` 构建 用于 该
S3 开发板. On an ESP32 该 published binary 是 该 蓝牙 one.

!!! 警告 "Amped-Esparagus 是 rev M 仅"

    `config/sdkconfig.defaults.amped-esparagus` describes **rev M** hardware. Earlier
    revisions 使用 a 不同 pinout.

    Its ILI9342 TFT 是 not a supported 驱动 — 该 firmware speaks
    [SSD1306/SH1106/SSD1309 OLED](../features/oled-display.md) 和
    [ST7789 TFT](../features/tft-display.md) — so 显示 support 是 commented out in 该
    开发板 configuration 和 该 开发板 ships 无需 a screen. 该 rotary encoder 有效:
    turning it changes 音量, clicking it toggles play/pause.

## 功能特性

- PCM5100 DAC 转换为 a TPA3110 或 TPA3128 Class-D amplifier
- 功放 held muted until 播放 starts, standby on pause, off on disconnect
- Software 音量 控制 — neither part has a 音量 register
- 8 MB 刷写
- [蓝牙 A2DP](../features/bluetooth.md) on the ESP32 variants
- [W5500 SPI 以太网](../features/ethernet.md) 与 automatic WiFi failover
- [SH1106 OLED](../features/oled-display.md) 通过 SPI on Amped-ESP32 和 Amped-ESP32-S3;
  a [rotary encoder](../features/buttons.md) on Amped-Esparagus

## 刷写固件

=== "Browser"

    Use 该 Amped installer 用于 your 开发板 on 该
    [刷写 页面](../getting-started/flashing.md).

=== "PlatformIO"

    ```bash
    # ESP32 — AirPlay + Bluetooth + Ethernet + OLED
    pio run -e amped-esp32-bt -t upload
    pio run -e amped-esp32-bt -t uploadfs

    # ESP32 — Esparagus rev M, rotary encoder
    pio run -e amped-esparagus-bt -t upload
    pio run -e amped-esparagus-bt -t uploadfs

    # ESP32-S3
    pio run -e amped-esp32-s3 -t upload
    pio run -e amped-esp32-s3 -t uploadfs
    ```

=== "ESP-IDF"

    ```bash
    idf.py set-target esp32
    idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.amped-esp32;config/sdkconfig.defaults.bt" build
    idf.py -p /dev/ttyUSB0 flash
    ```

    Swap in `config/sdkconfig.defaults.amped-esp32-s3` after `idf.py set-target esp32s3`
    用于 该 S3 revision.

## Default GPIO assignments

| 功能 | Amped-ESP32 | Amped-Esparagus | Amped-ESP32-S3 |
| --- | :-: | :-: | :-: |
| I2S BCK | 26 | 26 | 14 |
| I2S WS | 25 | 25 | 15 |
| I2S DO | 22 | 22 | 16 |
| Amp `UNMUTE` | 13 | 13 | 17 |
| Status LED | — | 12 | — |
| Rotary A | — | 33 | — |
| Rotary B | — | 27 | — |
| Encoder click | — | 34 | — |
| SPI SCLK | 18 | 18 | 12 |
| SPI MOSI | 23 | 23 | 11 |
| SPI MISO | 19 | 19 | 13 |
| 以太网 CS | 5 | 5 | 10 |
| 以太网 INT | 35 | 35 | 6 |
| 以太网 RST | 14 | 14 | 5 |
| Display CS | 15 | — | 47 |
| Display DC | 4 | — | 38 |
| Display RST | 32 | — | 48 |

## Related

- [Loud-ESP32](loud-esp32.md) — MAX98357A amplifiers, no DAC in front
- [HiFi-ESP32](hifi-esp32.md) — 该 相同 PCM5100 at line level, no amplifier
- [按键 和 rotary encoders](../features/buttons.md)
- [构建环境](../reference/build-environments.md)
