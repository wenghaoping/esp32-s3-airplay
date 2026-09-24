# USB 音频 (UAC)

Boards 与 a USB OTG port 可以 present themselves to an attached computer as a **stereo USB
音箱**. Audio sent by 该 host plays through 该 相同 output path AirPlay 使用, sharing
该 DAC's DSP, EQ 和 音量 控制.

!!! 警告 "Needs USB OTG 和 a 设备-role port"

    Only 该 ESP32-S2, S3 和 P4 have a USB OTG peripheral. 该 D+/D- pins must 也 be
    routed to a connector wired 用于 设备 role (CC pulldowns). 该 original ESP32 无法
    do this at all.

该 开发板 enumerates as a composite 设备: a USB Audio Class 音箱 plus an HID
consumer-控制 interface that sends media keys back to 该 host.

## How it 有效

- AirPlay 和 USB 音频 是 **mutually exclusive at runtime**, much like
  [蓝牙](bluetooth.md)
- AirPlay 是 suspended as soon as 该 host starts 流媒体播放
- 该 output 是 handed back once 该 host 流 has been idle 用于
  `CONFIG_USB_AUDIO_SINK_IDLE_MS`, 2000 ms by 默认
- Host 音量 和 mute 是 applied to 该 DAC, so 该 computer's own 音量 slider 有效
- [Hardware 按键](buttons.md) send play/pause, track skip, 音量 和 mute to 该 host
  通过 HID, since UAC itself carries no transport 控制s

## Sample rate

USB 音频 runs at **48 kHz**. `CONFIG_UAC_SAMPLE_RATE` must equal
`CONFIG_OUTPUT_SAMPLE_RATE_HZ`, because nothing resamples on this path 和 该 descriptor
advertises a single fixed rate.

!!! danger "44100 Hz does not 工作"

    `usb_device_uac` derives its FIFO drain rate 从 `sample_rate / 1000`, an integer
    division. At 44100 that truncates 44.1 frames per millisecond to 44. 该 feedback
    endpoint 使用 `AUDIO_FEEDBACK_METHOD_FIFO_COUNT`, so that FIFO 是 该 控制 variable
    和 该 host settles at 44000 frames/s while I2S consumes 44100. 该 resulting deficit
    of roughly 100 frames per 第二 slowly drains 该 buffer 和 then glitches
    continuously. 48000 divides 转换为 1 ms frames exactly.

TAS58xx 开发板 默认 to 48 kHz 用于 this reason, 和 because 该 驱动's EQ coefficients
是 computed 用于 48 kHz. AirPlay's 44.1 kHz 流 是 resampled on the way out.

## 构建环境

| Environment | Board |
| --- | --- |
| `esp32s3-uac` | ESP32-S3 + PCM5102A |
| `esparagus-audio-brick-dual-uac` | [Esparagus Audio Brick Dual](../boards/esparagus-audio-brick-dual-dac.md) |

USB 音频 是 enabled by layering `config/sdkconfig.defaults.uac` onto a 开发板's defaults. To
add it to a [custom 开发板](../boards/custom.md), put that 文件 **最后** in your
`SDKCONFIG_DEFAULTS` chain so it 可以 override 该 sample rate.

## Device name

`CONFIG_USB_AUDIO_SINK_PRODUCT` sets 该 name 该 host displays. It 是 used 两者 用于 该
product string 和 用于 该 音频 interface, 该 是 what Windows Device Manager 显示 用于
a composite function.

!!! tip "Windows caches 该 name"

    Windows stores descriptor strings per VID/PID/revision, so after changing 该 name it
    may keep showing 该 old one. Bump `bcdDevice` in `main/usb/usb_descriptors.c` to force
    a re-读取.

## Caveats

- **macOS** 需要 `CONFIG_UAC_SUPPORT_MACOS=y`. A single descriptor 无法 satisfy macOS 和
  Windows/Linux simultaneously, so this 是 a 构建-time choice.
- **No USB console.** TinyUSB claims 该 USB PHY, so USB-Serial-JTAG 无法 也 act as a
  console. Logs stay on UART0, 和 you must hold BOOT while resetting to reflash 通过 USB.
  [OTA 更新](../reference/ota.md) avoid 该 problem entirely.
