# 构建环境

Every PlatformIO 环境 defined in `platformio.ini`. 该 默认 是 `esp32s3`.

## Generic 开发板

| Environment | Chip | Flash | 说明 |
| --- | --- | --- | --- |
| `esp32s3` | ESP32-S3 | 16 MB | Default. External I2S DAC such as a PCM5102A |
| `esp32s3-jtag` | ESP32-S3 | 16 MB | Extends `esp32s3`, uploads 通过 构建-in USB JTAG |
| `waveshare-esp32s3` | ESP32-S3 | 16 MB | Waveshare ESP32-S3 pin arrangement |
| `esp32c5-xiao` | ESP32-C5 | 8 MB | Seeed XIAO, 需要 该 community pioarduino platform |
| `esp32wrover-dev` | ESP32 | 4 MB | Freenove WROVER, includes 蓝牙 |

## 功放 开发板

| Environment | Chip | DAC | Flash | 蓝牙 |
| --- | --- | --- | --- | :-: |
| `squeezeamp` | ESP32 | TAS5756 | 8 MB | — |
| `squeezeamp-bt` | ESP32 | TAS5756 | 8 MB | yes |
| `squeezeamp-4m` | ESP32 | TAS5756 | 4 MB | — |
| `esparagus-audio-brick` | ESP32 | TAS58xx | 8 MB | — |
| `esparagus-audio-brick-bt` | ESP32 | TAS58xx | 8 MB | yes |
| `esparagus-audio-brick-s3` | ESP32-S3 | TAS58xx | 8 MB | — |
| `esparagus-audio-brick-dual-dac` | ESP32-S3 | 2× TAS58xx | 8 MB | — |
| `esparagus-audio-brick-dual-uac` | ESP32-S3 | 2× TAS58xx | 8 MB | — |
| `esparagus-louder` | ESP32 | TAS58xx | 8 MB | — |
| `esparagus-louder-bt` | ESP32 | TAS58xx | 8 MB | yes |
| `esparagus-louder-s3` | ESP32-S3 | TAS58xx | 8 MB | — |
| `smartamp` | ESP32 | — | 4 MB | yes |

Every Esparagus 开发板 是 fitted 与 a TAS58xx amplifier, either a TAS5825M 或 a TAS5805M.
该 驱动 reads 该 die ID at startup 和 configures whichever it finds, so 该
环境 does not have to know 该 part 是 on the 开发板.

该 dual-DAC 环境 drive an [Audio Brick Dual](../boards/esparagus-audio-brick-dual-dac.md)
与 two amplifiers: stereo at I2C address 0x4C 和 a 第二 at 0x4D, wired either as a
bridged (PBTL) mono output 或 as a 第二 stereo pair. `-dual-uac` adds USB 音频 to 该
相同 开发板.

## Sonocotta 音频 dock 开发板

该 [HiFi](../boards/hifi-esp32.md), [Loud](../boards/loud-esp32.md),
[Amped](../boards/amped-esp32.md) 和 [Louder](../boards/louder-esp32.md) families all
come in an `-esp32` form 与 an 以太网 jack 和 an OLED header, 和 an `-esparagus`
form 无需 either. 蓝牙 Classic exists 仅 on the original ESP32, so no S3
环境 has a `-bt` variant.

| Environment | Chip | DAC / amp | Flash | 蓝牙 |
| --- | --- | --- | --- | :-: |
| `hifi-esp32` | ESP32 | PCM5100 | 8 MB | — |
| `hifi-esp32-bt` | ESP32 | PCM5100 | 8 MB | yes |
| `hifi-esparagus` | ESP32 | PCM5100 | 8 MB | — |
| `hifi-esparagus-bt` | ESP32 | PCM5100 | 8 MB | yes |
| `hifi-esp32-s3` | ESP32-S3 | PCM5100 | 8 MB | — |
| `hifi-esparagus-s3` | ESP32-S3 | PCM5100 | 8 MB | — |
| `loud-esp32` | ESP32 | MAX98357A | 8 MB | — |
| `loud-esp32-bt` | ESP32 | MAX98357A | 8 MB | yes |
| `loud-esparagus` | ESP32 | 2× MAX98357A | 8 MB | — |
| `loud-esparagus-bt` | ESP32 | 2× MAX98357A | 8 MB | yes |
| `loud-esp32-s3` | ESP32-S3 | 2× MAX98357A | 8 MB | — |
| `esparagus-echo` | ESP32-S3 | 2× MAX98357A | 8 MB | — |
| `amped-esp32` | ESP32 | PCM5100 + TPA31xx | 8 MB | — |
| `amped-esp32-bt` | ESP32 | PCM5100 + TPA31xx | 8 MB | yes |
| `amped-esparagus` | ESP32 | PCM5100 + TPA31xx | 8 MB | — |
| `amped-esparagus-bt` | ESP32 | PCM5100 + TPA31xx | 8 MB | yes |
| `amped-esp32-s3` | ESP32-S3 | PCM5100 + TPA31xx | 8 MB | — |
| `louder-esp32` | ESP32 | TAS5805M | 8 MB | — |
| `louder-esp32-bt` | ESP32 | TAS5805M | 8 MB | yes |
| `louder-esp32-plus` | ESP32 | TAS5825M | 8 MB | — |
| `louder-esp32-plus-bt` | ESP32 | TAS5825M | 8 MB | yes |
| `louder-esp32-s3` | ESP32-S3 | TAS5805M | 8 MB | — |
| `louder-esp32-s3-plus` | ESP32-S3 | TAS5825M | 8 MB | — |

## Targets 无需 a PlatformIO 环境

These have sdkconfig defaults 和 是 构建 through ESP-IDF 直接.

| Target | Sdkconfig | Status |
| --- | --- | --- |
| ESP32-S2 | `config/sdkconfig.defaults.esp32s2` | Built in CI, prebuilt binary published |
| ESP32-P4 | `config/sdkconfig.defaults.esp32p4` | Experimental |

```bash
idf.py set-target esp32s2
idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.esp32s2" build
```

## Which builds get a prebuilt binary

CI builds a subset of 环境 和 attaches them to 每个 发布版本. These 是 该 ones
可用 in 该 [browser installer](../getting-started/flashing.md):

`esp32s3`, `waveshare-esp32s3`, `esp32s2`, `squeezeamp-bt`, `squeezeamp-4m`, `smartamp`,
`esparagus-audio-brick-bt`, `esparagus-audio-brick-s3`, `esparagus-audio-brick-dual-dac`,
`esparagus-audio-brick-dual-uac`, `esparagus-louder-bt`, `esparagus-louder-s3`,
`esparagus-echo`, `hifi-esp32-bt`, `hifi-esparagus-bt`, `hifi-esp32-s3`,
`hifi-esparagus-s3`, `loud-esp32-bt`, `loud-esparagus-bt`, `loud-esp32-s3`,
`amped-esp32-bt`, `amped-esparagus-bt`, `amped-esp32-s3`, `louder-esp32-bt`,
`louder-esp32-plus-bt`, `louder-esp32-s3`, `louder-esp32-s3-plus`.

该 list lives in `.github/workflows/targets.json`, 和 每个 entry 需要 a matching
`docs/firmware/<name>.json` manifest 用于 该 installer to offer it.

Everything else you 构建 yourself. On an ESP32 开发板 that 可以 do 蓝牙 该 published
binary always includes it, so there 是 no prebuilt `squeezeamp`, `esparagus-audio-brick`,
`esparagus-louder`, `hifi-esp32`, `loud-esp32`, `amped-esp32` 或 `louder-esp32` — 构建
one of those yourself if you want 该 RAM 和 刷写 back.

该 相同 list runs on 每个 push to `staging` 和 publishes a rolling
[beta](../getting-started/flashing.md#beta-builds) pre-发布版本, so 每个 of these 开发板
has an untested 构建 of 该 current development tip 可用 too. A pull request builds
仅 该 entries flagged `"core": true`, 该 cover 每个 芯片 和 每个 开发板 support
目录 无需 a job per variant, 和 该 matrix does not fail fast, so one 开发板
failing to compile no longer stops 该 others being published.

## How sdkconfig layering 有效

All 开发板 configuration lives in **`config/`**. 该 generated `sdkconfig` stays at 该
项目 root — that one 是 a 构建 artifact 和 是 gitignored.

Environments compose their configuration by chaining sdkconfig 文件 left to right, 与
later 文件 overriding earlier ones:

```ini
board_build.cmake_extra_args =
    "-DSDKCONFIG_DEFAULTS=config/sdkconfig.defaults;config/sdkconfig.defaults.squeezeamp;config/sdkconfig.defaults.bt"
```

Here 该 常用 defaults come 首次, then 该 SqueezeAMP 开发板 configuration, then 该
蓝牙 overlay. Adding `config/sdkconfig.defaults.bt` to 该 end of any ESP32 开发板's chain 是
how 蓝牙 gets enabled.

!!! 警告 "Delete 该 cached sdkconfig after changing defaults"

    A generated `sdkconfig.<env>` 文件 是 cached in 该 项目 root. If you change any
    defaults, delete it before rebuilding 或 该 old values 是 silently reused.

## 常用命令

```bash
pio run -e <env> -t build      # Build
pio run -e <env> -t upload     # Build and flash over USB
pio run -e <env> -t uploadfs   # Flash the SPIFFS image from data/
pio run -e <env> -t monitor    # Serial monitor at 115200 baud
pio run -e <env> -t menuconfig # Kconfig configuration
```

To define your own 环境 无需 touching `platformio.ini`, see
[custom 开发板 configuration](../boards/custom.md).
