# Loud-ESP32, Loud-Esparagus 和 Esparagus Echo

该 Sonocotta [Loud-ESP32](https://github.com/sonocotta/esp32-audio-dock) 开发板 drive
**MAX98357A** I2S amplifiers 直接 — no DAC in front, no I2C 控制 port. Speakers
连接 straight to 该 开发板.

A MAX98357A has exactly one 控制 line: an active-high `SD_MODE` enable. 该 firmware
registers a minimal DAC 驱动 whose 仅 job 是 to drive that pin 从 RTSP 播放
events, so 该 amplifier 是 held muted until a client actually presses play 和 drops
back to standby on pause. That 是 该 相同 power-state handling 该
[Esparagus Audio Brick](esparagus-audio-brick.md) does 通过 I2C, reduced to one GPIO.

## Variants

| Environment | Chip | Amps | 以太网 | Display | 蓝牙 | Prebuilt |
| --- | --- | :-: | :-: | :-: | :-: | :-: |
| `loud-esp32` | ESP32 | 1 | yes | SH1106 OLED | — | — |
| `loud-esp32-bt` | ESP32 | 1 | yes | SH1106 OLED | yes | yes |
| `loud-esparagus` | ESP32 | 2 | — | — | — | — |
| `loud-esparagus-bt` | ESP32 | 2 | — | — | yes | yes |
| `loud-esp32-s3` | ESP32-S3 | 2 | yes | SH1106 OLED | — | yes |
| `esparagus-echo` | ESP32-S3 | 2 | yes | — | — | yes |

Both amplifiers share 该 one enable pin, so a dual-amp 开发板 mutes 和 unmutes as a
unit. 蓝牙 Classic exists 仅 on the original ESP32, so neither S3 开发板 has a
`-bt` 构建; on an ESP32 该 published binary 是 该 蓝牙 one.

[Esparagus Echo](https://github.com/sonocotta/esparagus-echo) 是 该 相同 amplifier
arrangement on the Echo's S3 开发板 — 以太网, an RGB status LED 和 no 显示 header.

## 功能特性

- One 或 two MAX98357A Class-D amplifiers, 音箱 已连接 直接
- 功放 held muted until 播放 starts, standby on pause, off on disconnect
- Software 音量 控制 — 该 MAX98357A has no 音量 register
- 8 MB 刷写
- [蓝牙 A2DP](../features/bluetooth.md) on the ESP32 variants
- [W5500 SPI 以太网](../features/ethernet.md) 与 automatic WiFi failover, except on
  Loud-Esparagus
- [SH1106 OLED](../features/oled-display.md) 通过 SPI, sharing 该 以太网 bus, on
  Loud-ESP32 和 Loud-ESP32-S3

## 刷写固件

=== "Browser"

    Use 该 Loud 或 Esparagus Echo installer on 该
    [刷写 页面](../getting-started/flashing.md).

=== "PlatformIO"

    ```bash
    # ESP32 — AirPlay + Bluetooth + Ethernet + OLED
    pio run -e loud-esp32-bt -t upload
    pio run -e loud-esp32-bt -t uploadfs

    # ESP32 — Esparagus variant, dual amp over WiFi
    pio run -e loud-esparagus-bt -t upload
    pio run -e loud-esparagus-bt -t uploadfs

    # ESP32-S3 — dual amp, Ethernet + OLED
    pio run -e loud-esp32-s3 -t upload
    pio run -e loud-esp32-s3 -t uploadfs

    # ESP32-S3 — Esparagus Echo
    pio run -e esparagus-echo -t upload
    pio run -e esparagus-echo -t uploadfs
    ```

=== "ESP-IDF"

    ```bash
    idf.py set-target esp32
    idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.loud-esp32;config/sdkconfig.defaults.bt" build
    idf.py -p /dev/ttyUSB0 flash
    ```

    Swap in `config/sdkconfig.defaults.loud-esp32-s3` 或
    `config/sdkconfig.defaults.esparagus-echo` after `idf.py set-target esp32s3` 用于 该
    S3 开发板.

## Default GPIO assignments

| 功能 | Loud-ESP32 | Loud-Esparagus | Loud-ESP32-S3 | Esparagus Echo |
| --- | :-: | :-: | :-: | :-: |
| I2S BCK | 26 | 26 | 14 | 18 |
| I2S WS | 25 | 25 | 15 | 8 |
| I2S DO | 22 | 22 | 16 | 17 |
| Amp enable (`SD_MODE`) | 13 | 13 | 17 | 9 |
| Status LED | — | 33 | — | 42 |
| SPI SCLK | 18 | — | 12 | 12 |
| SPI MOSI | 23 | — | 11 | 11 |
| SPI MISO | 19 | — | 13 | 13 |
| 以太网 CS | 5 | — | 10 | 10 |
| 以太网 INT | 35 | — | 6 | 6 |
| 以太网 RST | 14 | — | 5 | 5 |
| Display CS | 15 | — | 39 | — |
| Display DC | 4 | — | 40 | — |
| Display RST | 32 | — | 38 | — |

!!! 警告 "该 Loud-ESP32-S3 enable pin moved"

    `CONFIG_DAC_ENABLE_GPIO` 是 GPIO 17 用于 rev G 和 later hardware. Rev F used GPIO 8.
    On a rev F 开发板, override it in a
    [custom configuration](custom.md) 或 nothing 将 ever unmute.

## Related

- [HiFi-ESP32](hifi-esp32.md) — 该 相同 layout 与 a line-level PCM5100 instead
- [Amped-ESP32](amped-esp32.md) — PCM5100 与 a TPA31xx amplifier
- [蓝牙 A2DP](../features/bluetooth.md)
- [以太网 (W5500)](../features/ethernet.md)
- [构建环境](../reference/build-environments.md)
