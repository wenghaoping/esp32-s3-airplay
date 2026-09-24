# Esparagus Audio Brick Dual

该 **Audio Brick Dual** 是 an **ESP32-S3** [Esparagus Audio Brick](esparagus-audio-brick.md)
carrying **two** Class-D amplifiers on one I2S bus. As on 每个 brick, 每个 是 either a
TAS5825M 或 a TAS5805M 和 该 驱动 detects 该 at startup.

Two amplifiers give you a genuine active crossover: satellites on one 芯片, 
a bridged subwoofer 或 a 第二 stereo pair on the 其他, split in 该 DSP 
rather than by a passive 网络.

## 功能特性

- Two amplifiers, detected at I2C **0x4C** 和 **0x4D**
- 15 biquad sections per output, per amplifier — 60 in total across 该 four outputs
- Second amplifier wired as a bridged mono subwoofer 或 as a 第二 stereo pair,
  switchable 从 该 web interface
- [W5500 SPI 以太网](../features/ethernet.md) 与 automatic WiFi failover
- Optional [USB 音频](../features/usb-audio.md) — 该 S3's native USB 使 该 dual-DAC 开发板 
  a USB 音箱 as well as an AirPlay one
- I2C 和 SPI exposed 用于 external displays, sensors 和 GPIO expanders
- 8 MB 刷写, octal PSRAM
- No 蓝牙: A2DP 需要 蓝牙 Classic, 该 该 ESP32-S3 does not have

## 刷写固件

```bash
# AirPlay + Ethernet
pio run -e esparagus-audio-brick-dual-dac -t upload
pio run -e esparagus-audio-brick-dual-dac -t uploadfs

# The same board, also enumerating as a USB speaker
pio run -e esparagus-audio-brick-dual-uac -t upload
pio run -e esparagus-audio-brick-dual-uac -t uploadfs
```

Under ESP-IDF:

```bash
idf.py set-target esp32s3
idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.esparagus-audio-brick-dual-dac" build
idf.py -p /dev/ttyUSB0 flash
```

Both variants 也 have a prebuilt binary in 该
[browser installer](../getting-started/flashing.md).

## Default GPIO assignments

该 dual-DAC 开发板 shares 该 S3 revision's I2S, I2C, SPI 和 显示 pins, 和 differs in what it
does 与 该 two pins 该 single-DAC 开发板 spends on FAULTZ 和 PWDN.

| 功能 | GPIO | 说明 |
| --- | :-: | --- |
| I2S BCK | 14 | 位时钟 |
| I2S WS | 15 | 字选择时钟 (LRCLK) |
| I2S DO | 16 | 串行音频数据, 两者 amplifiers |
| I2C SDA | 8 | Control port, 两者 amplifiers |
| I2C SCL | 9 | Control port, 两者 amplifiers |
| DAC 1 enable | 18 | PDN 用于 该 amplifier at 0x4C |
| DAC 2 enable | 17 | PDN 用于 该 amplifier at 0x4D |
| Status LED | 21 | Addressable RGB |
| SPI SCLK | 12 | Shared by 以太网 和 显示 |
| SPI MOSI | 11 | Shared by 以太网 和 显示 |
| SPI MISO | 13 | 以太网 仅 |
| 以太网 CS | 10 | W5500 |
| 以太网 INT | 6 | W5500 |
| 以太网 RST | 5 | W5500 |
| Display CS | 47 | SH1106 OLED |
| Display DC | 38 | SH1106 OLED |
| Display RST | 48 | SH1106 OLED |

!!! 注意 "No fault line"

    GPIO 18 和 17 是 该 two DAC enables, so neither amplifier's FAULTZ pin
    reaches 该 MCU (`CONFIG_SPKFAULT_GPIO=-1`). 该 驱动 polls 两者 parts' fault
    registers 每个 two seconds instead, 该 catches 通过-current 和 thermal
    shutdown a little later than an interrupt would but reports 该 相同 详情.

## 功放 roles

Roles follow detection order, 该 follows I2C address:

| Index | Address | Role |
| --- | --- | --- |
| 0 | 0x4C | Stereo satellites, always a BTL pair |
| 1 | 0x4D | Second amplifier — bridged mono, 或 a 第二 stereo pair |

Both 是 fed 该 相同 I2S 流; what 每个 one does 与 it 是 设置 by its own DSP input
mixer, so no external wiring decides 该 routing.

### Second amplifier wiring

**Second 功放** on the main web 页面 chooses between 该 two:

- **Bridged mono (PBTL)** — OUT_A 和 OUT_B 是 paralleled 转换为 one 驱动, 用于 a
  subwoofer. 该 amplifier 是 fed `(L+R)/2` by 默认, since a single voice coil has no
  stereo to reproduce.
- **Stereo (BTL)** — two separate 音箱, as on the 首次 amplifier.

!!! danger "Rewire before restarting"

    PBTL 是 a 控制-port 设置 written while 该 part 是 still in HiZ, so 该 change
    takes effect on the next boot, not immediately. **Match 该 音箱 wiring to 该
    设置 before you restart.** Leaving OUT_A 和 OUT_B shorted together while 该 part
    comes up as a stereo BTL pair drives 该 two outputs against 每个 其他 和 可以
    damage 该 amplifier 和 its output filters. 该 web interface asks you to confirm
    用于 this reason.

该 设置 是 stored in NVS 和 读取 back before 该 DAC 是 initialised, because PBTL
has to be established before 该 output stage ever drives 该 load.

## Crossovers 和 EQ

该 [Equaliser](esparagus-audio-brick.md#equaliser) 页面 treats 两者 amplifiers as one
system. **构建 crossover** offers 该 layouts 该 dual-DAC 开发板 使 possible — tweeters on one
amplifier 和 woofers on the 其他, 或 satellites plus a subwoofer — 和 writes 该
filters, ganging 和 input routing 转换为 每个 output 该 split touches. Apply always
pushes 两者 amplifiers together, so a crossover spanning 该 pair 可以 never go live by
halves.

Per-output channel selection disappears 从 该 main 页面 once two amplifiers 是
found: 与 a crossover in 该 DSP 该 routing 是 already decided, so choosing it again
per output would mean nothing.

## PPC3 dumps

TAS5825M DACs 是 used, so [完整 PPC3 tunings](esparagus-audio-brick.md#full-ppc3-tuning)
apply — one 文件 per amplifier, indexed by detection order:

| File | Applies to |
| --- | --- |
| `/spiffs/hf/tas5825m_fw0-44100.bin` | amplifier at 0x4C, at 44.1 kHz |
| `/spiffs/hf/tas5825m_fw1-44100.bin` | amplifier at 0x4D, at 44.1 kHz |
| `/spiffs/hf/tas5825m_fw0-48000.bin` | amplifier at 0x4C, at 48 kHz |
| `/spiffs/hf/tas5825m_fw1-48000.bin` | amplifier at 0x4D, at 48 kHz |

A PPC3 log that drives 两者 amplifiers carries 该 writes 用于 每个, so convert it twice,
picking 该 设备 与 `--dev 98` 或 `--dev 9a`:

```bash
python3 components/dac_tas58xx/ppc3_convert.py both_amps.cfg --dev 98 -o tas5825m_fw0-48000.bin
python3 components/dac_tas58xx/ppc3_convert.py both_amps.cfg --dev 9a -o tas5825m_fw1-48000.bin
```

该 unindexed `tas5825m_fw-<rate>.bin` stands in 用于 该 首次 amplifier 仅, so on rev
D it 是 worth 使用 该 indexed names throughout to avoid confusion.

## USB 音频

`esparagus-audio-brick-dual-uac` 是 该 相同 开发板 与
[USB 音频](../features/usb-audio.md) layered on. 该 host sees a stereo USB 音箱
feeding 该 相同 DSP, crossover 和 音量 控制 AirPlay 使用, 和 AirPlay 是 suspended
while 该 host 是 流媒体播放.

USB 音频 runs at **48 kHz** — see [该 sample rate 警告](../features/usb-audio.md#sample-rate)
用于 why 44.1 kHz does not 工作 on this path. AirPlay's 44.1 kHz 流 是 resampled on
该 way out, so a 48 kHz PPC3 dump 是 该 one that matters on a UAC 构建.

TinyUSB claims 该 USB PHY, so USB-Serial-JTAG 无法 也 be a console on this 构建.
Logs stay on UART0, 和 reflashing 通过 USB 需要 BOOT held during reset;
[OTA 更新](../reference/ota.md) sidestep it.

## Related

- [Esparagus Audio Brick](esparagus-audio-brick.md) — 该 single-DAC ESP32 和 S3 开发板
- [USB 音频 (UAC)](../features/usb-audio.md)
- [以太网 (W5500)](../features/ethernet.md)
- [构建环境](../reference/build-environments.md)
