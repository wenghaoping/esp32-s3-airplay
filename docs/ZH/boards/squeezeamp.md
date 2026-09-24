# SqueezeAMP

该 [SqueezeAMP](https://github.com/philippe44/SqueezeAMP) 是 an ESP32 开发板 与 a
TAS575xx (combined DAC 和 Class-D amplifier). Connect 音箱
直接 to 该 开发板.

## 刷写固件

=== "Browser"

    Use 该 SqueezeAMP installer on the [刷写 页面](../getting-started/flashing.md).
    Prebuilt binaries exist 用于 该 蓝牙 构建 和 该 4 MB variant.

=== "PlatformIO"

    ```bash
    # AirPlay only
    pio run -e squeezeamp -t upload
    pio run -e squeezeamp -t uploadfs

    # AirPlay + Bluetooth A2DP
    pio run -e squeezeamp-bt -t upload
    pio run -e squeezeamp-bt -t uploadfs
    ```

=== "ESP-IDF"

    ```bash
    idf.py set-target esp32
    idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.squeezeamp" build
    idf.py -p /dev/ttyUSB0 flash
    ```

    `idf.py flash` 也 writes 该 SPIFFS `storage` partition 从 `data/`, so 该
    captive-portal 页面 是 present on 首次 boot.

## 构建 variants

| Environment | Flash | 蓝牙 | 说明 |
| --- | --- | :-: | --- |
| `squeezeamp` | 8 MB | — | AirPlay 仅 |
| `squeezeamp-bt` | 8 MB | yes | Prebuilt binary published |
| `squeezeamp-4m` | 4 MB | — | Smaller partition table, prebuilt binary published |

蓝牙 does not fit alongside AirPlay in 4 MB of 刷写, 该 是 why there 是 no
`squeezeamp-4m-bt`.

## What 该 构建 configures

该 SqueezeAMP 构建 selects 该 TAS57xx DAC 驱动 自动 through Kconfig
(`CONFIG_DAC_TAS57XX`) 和 sets 该 correct I2S 和 I2C pins. 音频缓冲区s 是 reduced
从 5000 to 2500 frames to fit 该 original ESP32's 更多 limited PSRAM bandwidth.

## Hybrid flow DSP

该 SqueezeAMP's TAS5754M has a miniDSP core, so it 可以 run a TI **HybridFlow** process
flow: a 完整-range stereo chain 与 EQ, bass enhancement 和 a compander, 或 a two-way
bi-amp crossover. 该 firmware ships 该 base flows 和 tunes them live 从 该
`/hf` 页面.

该 TAS5754M 是 该 part all of this has been tested on. See
[HybridFlow DSP](../features/hybridflow.md) 用于 该 flows, 该 tuning workflow 和 该
文件 layout.

!!! 注意

    HybridFlow 需要 a TAS57xx 与 a miniDSP. 该 驱动 detects 该 芯片 family at boot
    和 skips flow loading on TAS578x 设备, 该 have no DSP core.

See [SPIFFS filesystem](../reference/spiffs.md) 用于 该 文件 management API.

## Related

- [HybridFlow DSP](../features/hybridflow.md)
- [蓝牙 A2DP](../features/bluetooth.md)
- [构建环境](../reference/build-environments.md)
