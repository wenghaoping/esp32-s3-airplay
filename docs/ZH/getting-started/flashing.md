# Flash 该 firmware

There 是 three ways to get firmware onto 该 开发板. If you have no reason to prefer
another, 使用 该 browser installer.

| Method | Use it 当 | Needs |
| --- | --- | --- |
| **[A — Browser](#option-a-install-from-your-browser)** | You 只需 want a working 音箱 | Chrome, Edge 或 Opera |
| **[B — PlatformIO](#option-b-platformio)** | You want to change 构建 设置, 或 your 开发板 has no prebuilt binary | Python, a clone of 该 repo |
| **[C — ESP-IDF](#option-c-esp-idf)** | You already 工作 与 ESP-IDF | ESP-IDF v5.5.5+ |

## Option A — 安装 从 your browser

选择开发板 和 click 安装. Nothing to download, no toolchain, no 命令 line.

!!! info "要求"

    Works in Chrome, Edge 和 Opera on desktop. It 使用 该 Web Serial API, 该
    Safari 和 Firefox do not implement, 和 该 是 unavailable on iOS 和 Android.
    Plug 该 开发板 in 通过 USB before clicking 安装.

Each 开发板 has an **安装** 按键 用于 该 latest 发布版本 和, beside it, a dashed
**安装 beta** 按键 用于 a 构建 of 该 current `staging` branch. Read
[beta builds](#beta-builds) before 使用 该 第二 one.

### Generic 开发板

<div class="grid cards" markdown>

-   __ESP32-S3 + external DAC__

    该 standard 构建, 用于 an ESP32-S3 与 a PCM5102A 或 similar I2S DAC.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/esp32s3.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/esp32s3.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __ESP32-S2 + external DAC__

    For ESP32-S2 开发板 与 an external I2S DAC.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/esp32s2.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/esp32s2.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Waveshare ESP32-S3__

    For Waveshare ESP32-S3 开发板.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/waveshare-esp32s3.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/waveshare-esp32s3.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

</div>

### 功放 开发板

<div class="grid cards" markdown>

-   __SqueezeAMP__

    ESP32 + TAS5756. Includes 蓝牙 A2DP. For 8 MB 刷写 开发板.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/squeezeamp-bt.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/squeezeamp-bt.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __SqueezeAMP (4 MB 刷写)__

    For 该 4 MB 刷写 variant. No 蓝牙 — it does not fit.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/squeezeamp-4m.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/squeezeamp-4m.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __SmartAmp__

    ESP32 + 蓝牙 A2DP.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/smartamp.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/smartamp.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

</div>

### Esparagus 开发板

Every Esparagus 开发板 是 fitted 与 a **TAS58xx** amplifier — a TAS5825M 或 a TAS5805M,
detected at startup, so one binary covers 两者. 该 Audio Bricks 也 have W5500
以太网. 蓝牙 A2DP 仅 exists on the original ESP32.

<div class="grid cards" markdown>

-   __Esparagus Audio Brick__

    ESP32 + TAS58xx. Includes 蓝牙 A2DP 和 W5500 以太网.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/esparagus-音频-brick-bt.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/esparagus-音频-brick-bt.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Esparagus Audio Brick S3__

    ESP32-S3 + TAS58xx, 与 W5500 以太网.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/esparagus-音频-brick-s3.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/esparagus-音频-brick-s3.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Esparagus Audio Brick Dual__

    ESP32-S3 + two amplifiers: stereo plus a bridged mono subwoofer.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/esparagus-音频-brick-dual-dac.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/esparagus-音频-brick-dual-dac.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Esparagus Audio Brick Dual + USB 音频__

    该 Dual, 也 enumerating as a USB 音箱. See [USB 音频](../features/usb-audio.md).

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/esparagus-音频-brick-dual-uac.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/esparagus-音频-brick-dual-uac.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Esparagus Louder__

    ESP32 + TAS58xx. Includes 蓝牙 A2DP.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/esparagus-louder-bt.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/esparagus-louder-bt.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Esparagus Louder S3__

    ESP32-S3 + TAS58xx.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/esparagus-louder-s3.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/esparagus-louder-s3.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

</div>

### HiFi 开发板

[HiFi-ESP32 和 HiFi-Esparagus](../boards/hifi-esp32.md) carry a **PCM5100** line-level
DAC 和 no amplifier — they feed an amp 或 active 音箱. 该 `-ESP32` 开发板 have
W5500 以太网 和 an OLED; 该 Esparagus ones do not.

<div class="grid cards" markdown>

-   __HiFi-ESP32__

    ESP32 + PCM5100, 以太网 和 OLED. Includes 蓝牙 A2DP.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/hifi-esp32-bt.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/hifi-esp32-bt.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __HiFi-Esparagus__

    ESP32 + PCM5100, WiFi 仅. Includes 蓝牙 A2DP.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/hifi-esparagus-bt.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/hifi-esparagus-bt.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __HiFi-ESP32-S3__

    ESP32-S3 + PCM5100, 以太网 和 OLED.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/hifi-esp32-s3.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/hifi-esp32-s3.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __HiFi-Esparagus-S3__

    ESP32-S3 + PCM5100, WiFi 仅.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/hifi-esparagus-s3.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/hifi-esparagus-s3.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

</div>

### Loud 和 Echo 开发板

[Loud-ESP32, Loud-Esparagus 和 Esparagus Echo](../boards/loud-esp32.md) drive
**MAX98357A** amplifiers 直接 — 连接 音箱 to 该 开发板.

<div class="grid cards" markdown>

-   __Loud-ESP32__

    ESP32 + MAX98357A, 以太网 和 OLED. Includes 蓝牙 A2DP.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/loud-esp32-bt.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/loud-esp32-bt.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Loud-Esparagus__

    ESP32 + dual MAX98357A, WiFi 仅. Includes 蓝牙 A2DP.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/loud-esparagus-bt.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/loud-esparagus-bt.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Loud-ESP32-S3__

    ESP32-S3 + dual MAX98357A, 以太网 和 OLED.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/loud-esp32-s3.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/loud-esp32-s3.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Esparagus Echo__

    ESP32-S3 + dual MAX98357A, 以太网, no 显示.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/esparagus-echo.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/esparagus-echo.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

</div>

### Amped 开发板

[Amped-ESP32 和 Amped-Esparagus](../boards/amped-esp32.md) put a **PCM5100** DAC in front
of a **TPA3110/TPA3128** amplifier. Connect 音箱 to 该 开发板.

<div class="grid cards" markdown>

-   __Amped-ESP32__

    ESP32 + PCM5100 + TPA31xx, 以太网 和 OLED. Includes 蓝牙 A2DP.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/amped-esp32-bt.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/amped-esp32-bt.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Amped-Esparagus__

    ESP32 rev M, 以太网 和 a rotary encoder. Includes 蓝牙 A2DP.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/amped-esparagus-bt.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/amped-esparagus-bt.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Amped-ESP32-S3__

    ESP32-S3 + PCM5100 + TPA31xx, 以太网 和 OLED.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/amped-esp32-s3.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/amped-esp32-s3.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

</div>

### Louder 开发板

[Louder-ESP32](../boards/louder-esp32.md) carries a **TAS58xx** DAC 和 amplifier. 该
**Plus** 开发板 have a TAS5825M, 该 plain ones a TAS5805M — pick 该 card that matches
该 开发板, 该 pinouts differ.

<div class="grid cards" markdown>

-   __Louder-ESP32__

    ESP32 + TAS5805M, 以太网 和 OLED. Includes 蓝牙 A2DP.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/louder-esp32-bt.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/louder-esp32-bt.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Louder-ESP32-Plus__

    ESP32 + TAS5825M, 以太网 和 OLED. Includes 蓝牙 A2DP.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/louder-esp32-plus-bt.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/louder-esp32-plus-bt.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Louder-ESP32-S3__

    ESP32-S3 + TAS5805M, 以太网 和 OLED.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/louder-esp32-s3.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/louder-esp32-s3.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

-   __Louder-ESP32-S3-Plus__

    ESP32-S3 + TAS5825M, 以太网 和 OLED.

    <esp-web-install-button manifest="/esp32-s3-airplay/firmware/louder-esp32-s3-plus.json">
      <button slot="activate" class="md-button md-button--primary">安装</button>
      <span slot="unsupported">当前浏览器无法通过 USB 刷写，请在桌面端使用 Chrome、Edge 或 Opera。</span>
      <span slot="not-allowed">刷写需要安全的 HTTPS 连接。</span>
    </esp-web-install-button><esp-web-install-button class="安装-beta" manifest="/esp32-s3-airplay/firmware/beta/louder-esp32-s3-plus.json">
      <button slot="activate" class="md-button md-button--beta">安装 beta</button>
      <span slot="unsupported"></span>
      <span slot="not-allowed"></span>
    </esp-web-install-button>

</div>

Once 该 安装 finishes, unplug 和 re-plug 该 开发板. It boots 转换为 setup mode — carry
on to [首次启动](first-boot.md).

### Beta builds

该 dashed **安装 beta** 按键 刷写 a 构建 of 该 tip of 该 `staging` branch,
rebuilt on 每个 push. That 是 其中 fixes land before a 发布版本, so a beta 是 该 way to
try one — 或 to confirm a bug you reported 是 gone.

It 是 也 unreleased code. Betas come off 该 相同 CI as a 发布版本, but nobody has run
them on hardware, so treat a failure to boot as expected rather than surprising 和
[report it](https://github.com/wenghaoping/esp32-s3-airplay/issues). 安装ing 该 发布版本
构建 again always recovers 该 开发板.

A 按键 仅 appears 当 该 构建 behind it exists, so 该 beta 按键 是 absent
between `staging` pushes, 和 a 开发板 added since 该 最后 发布版本 显示 its beta 按键
alone until a 发布版本 carries a 构建 用于 it.

!!! 注意 "Prefer to 刷写 manually?"

    Every 构建 above 是 也 published as a merged `.bin`, on 该
    [releases 页面](https://github.com/wenghaoping/esp32-s3-airplay/releases/latest) 用于
    releases 和 under 该 [`beta` tag](https://github.com/wenghaoping/esp32-s3-airplay/releases/tag/beta)
    用于 该 current staging 构建. Merged images 是 flashed at offset **`0x0`** 与
    `esptool` 或 该 [esptool-js web tool](https://espressif.github.io/esptool-js/).

    Only 该 variants listed above 是 published — anything else in
    [构建 环境](../reference/build-environments.md) you 构建 yourself.

## Option B — PlatformIO

[PlatformIO](https://platformio.org/) handles 该 toolchain setup 用于 you.

```bash
# 1. Install the PlatformIO CLI
pip install platformio

# 2. Clone the project, including submodules
git clone --recursive https://github.com/wenghaoping/esp32-s3-airplay
cd esp32-s3-airplay

# 3. Plug the board in over USB and flash the firmware
pio run -e esp32s3 -t upload

# 4. Flash the SPIFFS image containing the web UI and data files
pio run -e esp32s3 -t uploadfs

# 5. Optionally watch the serial output
pio run -e esp32s3 -t monitor
```

!!! 警告 "Step 4 是 not 可选"

    PlatformIO does **not** 写入 该 SPIFFS partition as part of `-t upload`. If you skip
    `-t uploadfs`, 该 设备 boots but 该 captive portal 和 web UI 页面 是 missing,
    和 you get "文件 not found" errors during setup. See
    [SPIFFS filesystem](../reference/spiffs.md).

Replace `esp32s3` 与 whichever 环境 matches your hardware — see
[构建 环境](../reference/build-environments.md) 用于 该 完整 list.

## Option C — ESP-IDF

```bash
# 1. Install ESP-IDF v5.5.5 or newer:
#    https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/

# 2. Clone the project, including submodules
git clone --recursive https://github.com/wenghaoping/esp32-s3-airplay
cd esp32-s3-airplay

# 3. Activate the ESP-IDF environment
source /path/to/esp-idf/export.sh

# 4. Build and flash, including the SPIFFS "storage" partition from data/
idf.py set-target esp32s3
idf.py build
idf.py -p /dev/ttyUSB0 flash

# 5. Optionally monitor the serial output
idf.py -p /dev/ttyUSB0 monitor
```

Unlike PlatformIO, `idf.py flash` writes 该 SPIFFS partition in 该 相同 step, so there
是 no separate filesystem upload to remember.

## Next

Continue to [首次启动](first-boot.md).
