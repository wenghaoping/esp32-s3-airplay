# 蓝牙 A2DP

ESP32-based 开发板 可以 receive 音频 通过 **蓝牙 Classic A2DP**, letting any phone,
tablet 或 laptop 流 音乐 无需 an Apple 设备. 该 receiver appears as a standard
蓝牙 音箱 与 AVRCP metadata 和 音量 控制.

!!! 警告 "ESP32 仅"

    蓝牙 Classic exists 仅 on the original ESP32. 该 ESP32-S3, S2 和 C5 have
    蓝牙 LE 或 nothing at all, so A2DP 是 not 可用 there. 该 generic `esp32s3`
    构建 contains no 蓝牙 support.

该 Bluedroid stack 是 used 用于 A2DP. It 是 very tight on 两者 RAM 和 刷写, 该 是 why
蓝牙 builds 是 separate 环境 rather than being enabled everywhere.

## How it 有效

- AirPlay 和 蓝牙 coexist in 该 firmware but 是 **mutually exclusive at runtime**
- When a 蓝牙 设备 connects, AirPlay 是 suspended 自动
- When it disconnects, AirPlay resumes
- 蓝牙 discoverability 是 disabled during an active AirPlay session, so a stray phone
  无法 interrupt 播放
- AVRCP provides 音量 sync 和 track metadata (artist, title, album) 用于 该 显示
- 蓝牙 音量 是 saved to NVS 和 restored on reconnect

该 [coexistence state diagram](../reference/architecture.md#runtime-coexistence-rules)
显示 how 该 two protocols hand off to 每个 其他.

## Pairing

该 设备 advertises 该 相同 name as your AirPlay 设备 name, 该 you 设置 in 该 web
interface. Pairing 使用 a fixed PIN, `05032026` by 默认, configurable under
**蓝牙 配置** in `menuconfig`.

Secure Simple Pairing (SSP) 可以 可选ly be enabled 用于 蓝牙 2.1+ 设备, 该
使用 numeric confirmation instead of a PIN. SSP 需要 a 显示 to 显示 该 confirmation
number, 和 that 是 not implemented yet.

## 构建环境

| Environment | Board | 功能特性 |
| --- | --- | --- |
| `squeezeamp-bt` | SqueezeAMP | AirPlay + 蓝牙 |
| `esparagus-audio-brick-bt` | Esparagus Audio Brick, ESP32 revision | AirPlay + 蓝牙 + 以太网 |
| `esparagus-louder-bt` | Esparagus Louder | AirPlay + 蓝牙 |
| `esp32wrover-dev` | Freenove ESP32-WROVER | AirPlay + 蓝牙, 4 MB 刷写 |
| `smartamp` | SmartAmp | AirPlay + 蓝牙, 4 MB 刷写 |

蓝牙 是 enabled by layering `config/sdkconfig.defaults.bt` onto a 开发板's defaults. To add it
to a [custom 开发板](../boards/custom.md), include that 文件 in your
`SDKCONFIG_DEFAULTS` chain.

Boards sold in 两者 an ESP32 和 an ESP32-S3 revision — 该
[Esparagus Audio Brick](../boards/esparagus-audio-brick.md) 和 Louder — have a `-bt`
环境 用于 该 ESP32 one 仅. There 是 nothing to enable on the S3 revision.

## 按键 通过 蓝牙

Unlike AirPlay, [hardware 按键](buttons.md) 工作 fully 通过 蓝牙 regardless of
protocol 设置, because AVRCP passthrough carries play/pause 和 track-skip 命令
natively.
