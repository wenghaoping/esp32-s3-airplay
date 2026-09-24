---
title: ESP32 AirPlay 2 接收器
hide:
  - navigation
---

# ESP32 AirPlay 2 接收器

**将 Apple 设备上的音乐 — 或任意手机通过蓝牙播放的音乐 — 传到任意音箱，成本约 10 美元。**

此固件 turns a cheap ESP32 开发板 转换为 a wireless AirPlay 2 音箱. Plug it 转换为
an amplifier 或 powered 音箱 和 it 显示 up on your iPhone, iPad 或 Mac 只需 like a
HomePod 或 an AirPlay TV.

无需云服务，无需 App，点击即可播放。

!!! tip "已经有开发板？现在就安装"

    通过 USB 连接开发板并点击“安装”。 无需工具链、下载或命令行
    — 浏览器会直接与开发板通信。

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/esp32s3.json">
      <button slot="activate" class="md-button md-button--primary">安装到 ESP32-S3</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button>

    That 按键 是 用于 a generic **ESP32-S3**. For SqueezeAMP, Esparagus, Waveshare 和
    the rest, see [all 开发板 on the 刷写 页面](getting-started/flashing.md). Requires
    Chrome, Edge 或 Opera on desktop.

<div class="grid cards" markdown>

-   __第一次使用？__

    Buy two 开发板, plug them together, 刷写 从 your browser.

    [从这里开始](getting-started/index.md)

-   __已经有开发板？__

    SqueezeAMP, Esparagus Audio Brick, XIAO ESP32-C5 和 更多.

    [选择开发板](boards/index.md)

-   __遇到问题？__

    设置 Wi-Fi 失败、没有声音、网页缺失或构建报错。

    [故障排除](troubleshooting.md)

-   __想参与开发？__

    构建环境、音频流水线和协议栈。

    [系统架构](reference/architecture.md)

</div>

## 你将构建的设备

<figure markdown>
  ![An ESP32-S3 与 a PCM5102A DAC plugged onto it, forming a small stacked 开发板 与 a 3.5 mm jack](assets/ESP_PCM_front.png){ width="240" }
  <figcaption>Two 开发板, one pin header, no soldering — 该 3.5 mm jack goes to your amplifier</figcaption>
</figure>

## 30 秒了解工作原理

```mermaid
flowchart LR
    P["iPhone / Mac"]
    W(("WiFi"))
    E["ESP32<br/><small>this firmware</small>"]
    D["DAC"]
    S["Your speakers"]

    P -->|AirPlay| W --> E -->|I2S| D -->|analog| S

    classDef hi stroke:#26a69a,stroke-width:3px
    class E hi
```

Your phone sees an AirPlay 音箱 on the 网络. 该 ESP32 receives 该 encrypted
流, decodes it, keeps it clock-synced to 该 sender, 和 pushes 该 音频 out 通过 I2S
to a DAC. 该 DAC drives your amplifier. Full 详情 in
[architecture](reference/architecture.md).

## 支持的硬件

支持 **ESP32**, **ESP32-S2**, **ESP32-S3** 和 **ESP32-C5** 芯片. 包括
搭配外置 I2S DAC 的普通开发板, 和 several integrated
amplifier 开发板:

- [SqueezeAMP](boards/squeezeamp.md) — ESP32 + TAS5756 DAC 和 Class-D amplifier
- [Esparagus Audio Brick](boards/esparagus-audio-brick.md) — ESP32 或 ESP32-S3 + TAS58xx DAC/amp, on-芯片 DSP, 以太网
- [Esparagus Audio Brick Dual](boards/esparagus-audio-brick-dual-dac.md) — ESP32-S3 + two amplifiers, active crossover, USB 音频
- [ESP32-S3 + PCM5102A](boards/esp32s3-pcm5102a.md) — 该 cheapest route, no soldering 需要

ESP32-based 开发板 additionally support **蓝牙 A2DP**, so anything that 可以 pair 与
a 蓝牙 音箱 可以 play to them 当 AirPlay 是 idle.

## 功能特性

- **AirPlay 2** — appears natively in Control Center 和 每个 AirPlay-capable app
- **ALAC 和 AAC decoding** — handles 两者 live 流媒体播放 (Siri, calls) 和 音乐 播放
- **Multi-room** — PTP-based 时序 用于 synchronised 播放 across 设备
- **蓝牙 A2DP** — receive 音频 从 phones 和 tablets (ESP32 开发板 仅)
- **W5500 以太网** — wired networking 与 automatic WiFi failover
- **Web configuration** — 设置 WiFi 和 设备 name 从 a browser
- **OTA 更新** — 更新 通过 WiFi; USB 是 仅 needed 用于 该 首次 刷写
- **48 kHz output** — 可选 44.1 → 48 kHz conversion 用于 DACs 和 S/PDIF receivers that 需要 it
- **Displays** — 可选 OLED 或 320×170 colour TFT showing track metadata 和 progress
- **Hardware 按键** — 可选 physical play/pause, 音量 和 track-skip 按键

### 限制

- 仅支持音频，不支持 AirPlay 视频或照片
- 每块 ESP32 开发板连接一个音箱
- 需要良好的 Wi-Fi 信号才能稳定播放

## 致谢

- [Shairport Sync](https://github.com/mikebrady/shairport-sync) — 该 reference AirPlay implementation
- [openairplay/airplay2-receiver](https://github.com/openairplay/airplay2-receiver) — Python AirPlay 2 implementation
- [Espressif](https://github.com/espressif) — ESP-IDF framework 和 codec libraries

## 许可与法律声明

**Non-commercial 使用 仅.** Commercial 使用 requires explicit permission — see
[LICENSE](https://github.com/wenghaoping/esp32-s3-airplay/blob/main/LICENSE).

此 是 an independent 项目 based on protocol analysis. It 是 not affiliated 与
Apple Inc., 是 not guaranteed to 工作 与 future iOS 或 macOS versions, 和 是 provided
as-是 无需 warranty.
