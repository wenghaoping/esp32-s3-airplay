# Seeed XIAO ESP32-C5

该 Seeed XIAO ESP32-C5 是 a RISC-V 开发板 与 8 MB 刷写, 8 MB PSRAM 和 **dual-band
WiFi 6**, 该 使 it attractive 其中 2.4 GHz 是 congested. Wire an external I2S DAC
such as a PCM5102A.

!!! 警告 "No 蓝牙 A2DP"

    该 ESP32-C5 has 蓝牙 LE 仅, not 蓝牙 Classic, so A2DP 音频 是 not
    可用 on this 开发板.

## Default I2S pins

| 功能 | GPIO | XIAO label |
| --- | --- | --- |
| 位时钟 (BCK) | 8 | D8 |
| 字选择时钟 (WS / LRCK) | 9 | D9 |
| Data in (DIN) | 10 | D10 |

Change them under **Board 配置 → Pin 配置** in `menuconfig`.

## 构建ing

There 是 no prebuilt binary 用于 this 开发板 — 构建 it yourself.

=== "PlatformIO"

    该 official `platformio/espressif32` platform does **not** support 该 ESP32-C5, so
    每个 环境 使用 该 community
    [pioarduino](https://github.com/pioarduino/platform-espressif32) platform, pinned in
    `platformio.ini`. It bundles ESP-IDF 5.5.5 和 PlatformIO downloads it 自动
    on the 首次 构建 — no extra setup needed.

    ```bash
    pio run -e esp32c5-xiao -t upload
    pio run -e esp32c5-xiao -t uploadfs
    ```

=== "ESP-IDF"

    ```bash
    idf.py set-target esp32c5
    idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.esp32c5" build flash monitor
    ```

## Related

- [构建环境](../reference/build-environments.md)
- [自定义开发板 configuration](custom.md)
