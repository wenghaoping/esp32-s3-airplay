<div align="center">

<img src="docs/assets/logo_airplay_esp32.png" alt="AirPlay ESP32" width="400">

# ESP32 AirPlay 2 接收器

**将 Apple 设备上的音乐，或任意手机通过蓝牙播放的音乐，传到任意音箱，成本约 10 美元**

[![GitHub stars](https://img.shields.io/github/stars/wenghaoping/esp32-s3-airplay?style=flat-square)](https://github.com/wenghaoping/esp32-s3-airplay/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/wenghaoping/esp32-s3-airplay?style=flat-square)](https://github.com/wenghaoping/esp32-s3-airplay/network)
[![许可证](https://img.shields.io/badge/license-Non--Commercial-blue?style=flat-square)](LICENSE)
[![ESP-IDF](https://img.shields.io/badge/ESP--IDF-v5.5+-red?style=flat-square)](https://docs.espressif.com/projects/esp-idf/)
[![平台](https://img.shields.io/badge/platform-ESP32%20%7C%20S2%20%7C%20S3%20%7C%20C5-green?style=flat-square)](https://www.espressif.com/en/products/socs)

### [文档](https://wenghaoping.github.io/esp32-s3-airplay/) · [浏览器安装](https://wenghaoping.github.io/esp32-s3-airplay/getting-started/flashing/) · [故障排除](https://wenghaoping.github.io/esp32-s3-airplay/troubleshooting/)

</div>

---

## 这是什么？

本项目可以将廉价的 ESP32 开发板变成无线 AirPlay 2 音箱。把它连接到任意功放或有源音箱后，它会像 HomePod 或支持 AirPlay 的电视一样出现在 iPhone、iPad 或 Mac 上。

支持 **ESP32**、**ESP32-S2**、**ESP32-S3** 和 **ESP32-C5** 芯片，包括内置功放的 [SqueezeAMP](https://github.com/philippe44/SqueezeAMP)（ESP32 + TAS5756）和 [Esparagus Audio Brick](https://sonocotta.com/espragus-audio-brick/)（ESP32 + TAS5825M）开发板。

基于 ESP32 的开发板还支持 **蓝牙 A2DP**。因此，只要设备能够与蓝牙音箱配对，就能在 AirPlay 空闲时向本项目播放音频。Esparagus Audio Brick 还可以通过可选的 W5500 模块支持**有线以太网**。

**无需云服务，无需 App，点击即可播放。**

## 快速开始

最快的方式是使用浏览器安装器，无需工具链或命令行：

**[→ 使用浏览器安装](https://wenghaoping.github.io/esp32-s3-airplay/getting-started/flashing/)**

如果你准备从零件组装，需要一块 ESP32-S3 开发板、一个 PCM5102A DAC 和一排母排针，总成本约 10 美元，而且无需焊接。请查看[快速开始指南](https://wenghaoping.github.io/esp32-s3-airplay/getting-started/)。

本项目所用 ESP32-S3 开发板的说明书请见 [ESP32-S3 板卡说明书](https://manuals.plus/ae/1005008669775924)。

从源码构建：

```bash
git clone --recursive https://github.com/wenghaoping/esp32-s3-airplay
cd esp32-s3-airplay
pio run -e esp32s3 -t upload
pio run -e esp32s3 -t uploadfs   # 必需：将网页界面写入 SPIFFS
```

## 功能特性

- **AirPlay 2**：原生出现在控制中心和所有支持 AirPlay 的 App 中
- **ALAC 和 AAC 解码**：支持实时流媒体（Siri、通话）和音乐播放
- **多房间播放**：基于 PTP 的时钟同步
- **蓝牙 A2DP**：接收手机和平板的音频（仅 ESP32 开发板）
- **W5500 以太网**：有线联网，并在必要时自动切换 Wi-Fi
- **网页配置和 OTA 更新**：首次刷写后通常无需 USB
- **48 kHz 输出**：可选的 44.1 → 48 kHz sinc 重采样
- **显示屏**：可选 OLED 或 320×170 彩色 TFT，显示曲目元数据
- **硬件按键**：可选播放/暂停、音量和切换曲目按键

仅支持音频，每块开发板连接一个音箱，并且需要良好的 Wi-Fi 信号。

## 文档

| | |
| --- | --- |
| [快速开始](https://wenghaoping.github.io/esp32-s3-airplay/getting-started/) | 采购清单、组装、刷写固件、首次启动 |
| [支持的开发板](https://wenghaoping.github.io/esp32-s3-airplay/boards/) | SqueezeAMP、Esparagus Audio Brick、XIAO ESP32-C5、自定义开发板 |
| [功能特性](https://wenghaoping.github.io/esp32-s3-airplay/features/bluetooth/) | 蓝牙、以太网、显示屏、按键、AirPlay 调优 |
| [参考资料](https://wenghaoping.github.io/esp32-s3-airplay/reference/build-environments/) | 构建环境、SPIFFS、OTA、系统架构 |
| [故障排除](https://wenghaoping.github.io/esp32-s3-airplay/troubleshooting/) | 没有声音、设置 Wi-Fi 不出现、播放断续、构建错误 |

## 参与贡献

请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 和[贡献指南](https://wenghaoping.github.io/esp32-s3-airplay/contributing/)。文档位于 [`docs/`](docs/) 中，使用 [Zensical](https://zensical.org/) 构建，网站上的每个页面都有编辑链接，可以直接打开 GitHub 编辑器。

## 致谢

- [Shairport Sync](https://github.com/mikebrady/shairport-sync)：参考 AirPlay 实现
- [openairplay/airplay2-receiver](https://github.com/openairplay/airplay2-receiver)：Python AirPlay 2 实现
- [Espressif](https://github.com/espressif)：ESP-IDF 框架和编解码库

## 许可与法律声明

**仅限非商业用途。**商业使用需要获得明确许可，请参阅 [LICENSE](LICENSE)。

这是一个基于协议分析的独立项目，与 Apple Inc. 没有隶属关系，不保证兼容未来版本的 iOS 或 macOS，按“现状”提供且不附带任何保证。
