# Esparagus Audio Brick

该 [Esparagus Audio Brick](https://github.com/sonocotta/esparagus-media-center/?tab=readme-ov-file#esparagus-audio-brick-prototype)
是 构建 around a TI **TAS5825M** Class-D DAC 和 amplifier. Like 该 SqueezeAMP, it
需要 no external DAC — 连接 音箱 直接.

该 开发板 exists as an **ESP32** revision 和 an **ESP32-S3** revision. 该 音频 design
是 该 相同; 该 pinout 是 not, 和 neither 是 what 该 two 芯片 可以 do — see
[Default GPIO assignments](#default-gpio-assignments) 和 [Variants](#variants).

Some bricks 是 fitted 与 a TI **TAS5805M** rather than 该 TAS5825M. It 是 该 相同
family 和 该 相同 驱动, but it 是 not 该 相同 part: see
[TAS5805M 开发板](#tas5805m-boards) 用于 what it does 和 does not do here.

## 功能特性

- TAS5825M 与 on-芯片 DSP 和 a 15-band parametric EQ (25 Hz – 16 kHz)
- Hardware 音量 控制 与 a configurable maximum level
- Speaker fault detection 与 automatic mute 和 recovery
- Automatic power state management (deep sleep / standby / play) driven by AirPlay session state
- 8 MB 刷写
- [蓝牙 A2DP](../features/bluetooth.md) on the **ESP32 revision 仅** — 该 S3 has no
  蓝牙 Classic radio, so there 是 no `-bt` 构建 用于 it
- [W5500 SPI 以太网](../features/ethernet.md) 与 automatic WiFi failover, on 两者
  revisions

## 刷写固件

=== "Browser"

    Use 该 Esparagus Audio Brick installer on 该
    [刷写 页面](../getting-started/flashing.md). 该 published binary 是 该
    蓝牙 + 以太网 构建.

=== "PlatformIO"

    ```bash
    # ESP32 — AirPlay + Ethernet
    pio run -e esparagus-audio-brick -t upload
    pio run -e esparagus-audio-brick -t uploadfs

    # ESP32 — AirPlay + Bluetooth + Ethernet
    pio run -e esparagus-audio-brick-bt -t upload
    pio run -e esparagus-audio-brick-bt -t uploadfs

    # ESP32-S3 — AirPlay + Ethernet (no Bluetooth on this chip)
    pio run -e esparagus-audio-brick-s3 -t upload
    pio run -e esparagus-audio-brick-s3 -t uploadfs

    # Serial monitor
    pio run -e esparagus-audio-brick -t monitor
    ```

=== "ESP-IDF"

    ```bash
    # ESP32 revision
    idf.py set-target esp32
    idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.esparagus-audio-brick" build

    # ESP32-S3 revision
    idf.py set-target esp32s3
    idf.py -DSDKCONFIG_DEFAULTS="config/sdkconfig.defaults;config/sdkconfig.defaults.esparagus-audio-brick-s3" build

    idf.py -p /dev/ttyUSB0 flash
    ```

## Default GPIO assignments

该 two revisions share no pinout, so pick 该 column matching your 开发板. 该 ESP32
column 是 `config/sdkconfig.defaults.esparagus-audio-brick`, 该 S3 column
`config/sdkconfig.defaults.esparagus-audio-brick-s3`.

| 功能 | ESP32 | ESP32-S3 | 说明 |
| --- | :-: | :-: | --- |
| I2S BCK | 26 | 14 | 位时钟 |
| I2S WS | 25 | 15 | 字选择时钟 (LRCLK) |
| I2S DO | 22 | 16 | 串行音频数据 |
| I2C SDA | 21 | 8 | DAC 控制 (TAS5825M) |
| I2C SCL | 27 | 9 | DAC 控制 (TAS5825M) |
| DAC 警告 | 36 | 4 | TAS5825M 警告 output, input |
| Speaker fault | 39 | 18 | TAS5825M FAULTZ, input |
| Status LED | 12 | 21 | Addressable RGB |
| SPI SCLK | 18 | 12 | Shared by 以太网 和 显示 |
| SPI MOSI | 23 | 11 | Shared by 以太网 和 显示 |
| SPI MISO | 19 | 13 | 以太网 仅 |
| 以太网 CS | 5 | 10 | W5500 |
| 以太网 INT | 35 | 6 | W5500 |
| 以太网 RST | 14 | 5 | W5500 |
| Display CS | 15 | 47 | SH1106 OLED |
| Display DC | 4 | 38 | SH1106 OLED |
| Display RST | 32 | 48 | SH1106 OLED |

!!! 注意 "GPIOs 34–39 是 input-仅 on the ESP32"

    On 该 ESP32 revision 该 fault, 警告 和 以太网 interrupt lines land on
    GPIOs 35–39, 该 是 input-仅 和 have no internal pull-up. 该 开发板 provides
    external pull-ups. 该 S3 revision has no such restriction on the pins it 使用.

该 Audio Brick Dual 是 an S3 开发板 与 a third pinout: it has two amplifiers 和 no
FAULTZ line back to 该 MCU, spending GPIO 18 和 17 on the two DAC enables instead. See
[Esparagus Audio Brick Dual](esparagus-audio-brick-dual-dac.md).

该 构建 selects 该 TAS58xx 驱动 自动 (`CONFIG_DAC_TAS58XX`). 该 驱动
auto-detects 该 amplifier at startup: 0x4C–0x4F 用于 a TAS5825M, 0x2C–0x2F 用于 a
TAS5805M. It then confirms 该 guess against 该 die ID 和 warns if 该 two disagree.

## TAS5805M 开发板

Some bricks carry a **TAS5805M** instead. 该 驱动 detects it, drives it 和 gives it
its own init sequence, so 该 开发板 plays 和 its 音量, mute 和 15-band biquad chain
all 工作 through 该 [Equaliser](#equaliser) 页面 exactly as on a TAS5825M.

Two things do not carry 通过:

!!! 警告 "No PPC3 dumps on a TAS5805M"

    A dump replays a *process flow*, 该 是 a TAS5825M feature — 该 TAS5805M has no
    flow-选择 register 和 lays its coefficients out differently, so a dump exported
    用于 one part would 写入 garbage 转换为 该 其他. 该 驱动 checks 该 model 和
    skips 该 文件 rather than risk it. There 是 no equivalent to load, so
    [Full PPC3 tuning](#full-ppc3-tuning) simply does not apply: 该
    [Equaliser](#equaliser) 页面 是 该 whole of 该 tuning 可用, 该 用于 most
    builds 是 该 whole signal path anyway.

该 **input mixer** 是 TAS5825M-仅 too. Summing to mono 或 feeding one channel to 两者
outputs 是 done in 该 DSP mixer, 和 仅 该 TAS5825M's mixer 是 implemented here, so
a TAS5805M passes 该 stereo pair straight through 和 logs a 警告 if asked 用于
anything else. That 也 means no crossover layout needing a summed 或 single-channel
feed — 该 ones that route 该 pair as-是 still 工作.

## Equaliser

TAS5825M 开发板 expose 该 DAC's 15 cascaded biquad sections through 该 设备's web
interface at `/bq`, one filter per section, per output 和 per amplifier. Each
section 可以 be a peaking filter, a shelf, a low 或 high pass in six alignments, a band
pass, a notch, a phase shift, 或 five raw coefficients. 该 filter models match
PurePath Console 3, 和 coefficients 是 recomputed whenever 该 I2S sample rate
changes. 该 芯片's two outputs 是 named A 和 B — 该 of them carries left, right
或 a sum 是 该 routing 设置, not a fixed assignment. A 和 B 可以 be ganged 或
tuned separately. Editing 仅 redraws 该 response graph: **Apply** sends 该 filters
to 该 amplifiers so you 可以 hear them, 和 **Commit to 刷写** 使 them survive a
reboot. **Revert** goes back to what 是 in 刷写. For plain tone shaping, **Load
15-band EQ** fills 该 chain 与 a flat graphic equaliser — one peaking section per
band 从 20 Hz to 16 kHz — leaving 仅 该 gains to 设置. It fills in 该 form 和
nothing 更多, so 该 amplifier hears it 仅 once applied.

Crossovers 是 构建 从 these 相同 sections, so a two-way 或 subwoofer split 是 只需
a high pass on one amplifier 和 a low pass on the 其他. **构建 crossover** does that
用于 you: pick how 该 drivers 是 wired — 两者 bands on one amplifier, one amplifier per
音箱, tweeters on one amplifier 和 woofers on the 其他, 或 satellites plus a
subwoofer — then a crossover frequency 和 an alignment: Linkwitz-Riley at 12 或
24 dB per octave, Butterworth at 6, 12 或 24, 或 Bessel at 12. It writes 该 filters
转换为 每个 output 该 split touches, sets ganging 和 input routing to match, 和
leaves 该 filters staged so nothing 是 heard until applied. Apply always pushes all
amplifiers, so a crossover spanning 两者 可以 never go live by halves. Layouts 该
wiring rules out 是 not offered — a bridged amplifier has no separate A 和 B to
split across.

Steeper alignments cost 更多 slots, because sections cascade. A Linkwitz-Riley 是 two
cascaded Butterworths of half its order, so LR2 是 two 1st-order Butterworths — real
poles, 该 collapse 转换为 a single biquad at Q 0.5 — while LR4 是 two Butterworth 2
sections at Q 0.707 和 无法 be folded 转换为 one. That 是 why a 24 dB per octave
split 显示 two Butterworth 2 sections rather than one Linkwitz-Riley 2: 两者 would
slope at 24 dB per octave, but 仅 该 Butterworth pair sits 6 dB down at 该 corner,
该 是 what lets 该 two branches sum flat. Two Linkwitz-Riley 2 sections would be
12 dB down there 和 sum 6 dB short.

Each section 也 has an **Inv** box that flips its polarity. 该 builder sets this
itself 和 does not offer it as a choice, because 该 alignment decides it: at 该
corner 该 branches sit 180° apart at 12 dB per octave 和 需要 opposite polarity to
sum flat, but they 是 back in phase at 24, 其中 inverting would instead dig a notch.
Only one section of a branch ever carries it — polarity belongs to 该 chain, 和
since sections multiply, inverting an even number of them cancels back to none. 该
box 是 still there by hand 用于 drivers wired out of phase. A section left on Bypass
与 Inv ticked 是 a plain polarity flip 和 costs nothing else.

### Fitting to a measurement

**Fit to a measurement…** turns a measured response 转换为 a correction. Load a frequency
response export — REW text, 或 any 文件 与 a frequency 和 a level in its 首次 two
columns — 和 该 fitter searches 用于 该 peaking filters 和 shelves that flatten it,
then writes them 转换为 该 chain. Only 该 shape 是 fitted, never 该 absolute level. 该
response graph gains two overlays, 该 measurement as it 是 和 as it would be once
corrected, so 该 fit 可以 be judged before anything 是 applied.

Three 设置 matter 更多 than the rest. 该 fit range decides 其中 该 effort goes: a
驱动 rolls off at its ends by 更多 than any filter 可以 undo, 和 leaving 该 range
wide spends filters fighting that instead of correcting 该 band 该 驱动 covers — 该
页面 says so 当 该 measurement 是 already well down at 该 low limit. Smoothing sets
how much 详情 是 chased, 和 a sixth of an octave keeps 该 room modes while ignoring
该 fine structure that moves 当 该 microphone does. 该 boost 和 cut limits apply
to 该 summed correction rather than to any one filter, 和 该 result reports how much
boost 是 used, so 该 相同 amount 可以 come off that output's level to keep 该
headroom.

**Keep 首次 N sections** protects 该 head of 该 chain. 该 fit replaces everything
past that count, so on a bi-amped 音箱 keep 该 crossover, measure 每个 way through
it, 和 fit 转换为 what 是 left; 该 count 是 filled in 从 any low 或 high passes
already sitting at 该 top of 该 chain. Kept sections 是 slots 该 fitter 无法 have,
so **Filters to 使用** caps itself at what remains — a 24 dB per octave crossover leaves
13 of 该 15. Fitted filters 是 staged like any 其他 edit — nothing 是 heard until
applied 和 nothing survives a reboot until committed.

Each amplifier carries its own input routing: 该 stereo pair as-是, summed to
`(L+R)/2`, 或 one channel fed to 两者 outputs. A bridged amplifier drives a single voice
coil, so it 是 always fed a single channel 和 defaults to 该 sum; ganging 是 implicit
和 该 stereo option 是 not offered. A combined response graph at 该 top of 该 页面
plots 每个 active output together, so a crossover spread across 两者 amplifiers 可以 be
读取 as one picture.

**Show what 该 outputs sum to** adds one 更多 trace to that graph. 输出s feeding
separate drivers add as vectors 和 not as curves, so two branches that 每个 look right
alone 可以 still cancel 其中 they overlap — 和 该 two curves look identical either
way round, 该 是 what 使 it easy to miss. 该 sum 是 taken on the complex
response instead: a crossover 是 right 当 it runs flat through 该 corner, 和 a dip
there means 该 branches 是 fighting, so one of them 需要 **Inv**. 该 trace knows
仅 该 filters, never 该 drivers, their spacing 或 该 room, so it 显示 what 该
crossover 是 aiming at rather than what a microphone would hear.

Levels 是 设置 in 该 音量 section. Master 是 该 AirPlay 音量 和 moves
everything together. Below it 每个 output has its own level 和 mute, applied in 该
DSP input mixer ahead of 该 filters — so they 仅 ever attenuate 和 cost no filter
headroom. Use them to match drivers of differing sensitivity. Levels 和 mutes take
effect immediately 和 是 stored in NVS, independently of 该 filter commit.

## Full PPC3 tuning

!!! info "TAS5825M 仅"

    此 whole section applies to 开发板 fitted 与 a TAS5825M. A TAS5805M brick has no
    process flow to replay 和 ignores these 文件 \u2014 see
    [TAS5805M 开发板](#tas5805m-boards).

该 Equaliser 页面 covers 该 fifteen biquads per channel, 该 crossover 和 该 levels,
该 是 该 whole signal path 用于 most builds. A tuned dump 从 TI PurePath Console 3
goes further: it 是 该 complete 设备 configuration — clocking, I2S format, 该 process
flow 选择 和 每个 coefficient — so it reaches blocks 该 web interface does not
expose. 包括 flows whose coefficient map TI never published, because a dump
replays TI's own register writes rather than addresses we would have to know.

At boot 该 驱动 looks 用于 a dump on SPIFFS 和, if one 是 present, replays it *instead
of* 该 构建-in init sequence. PPC3 bakes 每个 coefficient at 该 rate 该 flow 是
exported 用于, so a 48 kHz tuning played at 44.1 kHz puts 每个 corner about 8% low: name
该 文件 用于 its rate 和 该 驱动 picks 该 one matching what it 是 playing.

| File | Applies to |
| --- | --- |
| `/spiffs/hf/tas5825m_fw-44100.bin` | 该 仅 amplifier, 或 该 首次 of two, at 44.1 kHz |
| `/spiffs/hf/tas5825m_fw-48000.bin` | 该 相同, at 48 kHz |
| `/spiffs/hf/tas5825m_fw0-44100.bin` | 首次 amplifier on a dual-DAC 开发板, at 44.1 kHz |
| `/spiffs/hf/tas5825m_fw1-44100.bin` | 第二 amplifier on a dual-DAC 开发板, at 44.1 kHz |

Drop 该 `-<rate>` suffix — `tas5825m_fw.bin`, `tas5825m_fw0.bin` — 用于 a dump that
should serve 每个 rate. Those names 是 该 fallback, searched 仅 once no
rate-specific 文件 matches, so a single-rate 安装 keeps working untouched. A process
flow 是 a TAS5825M feature, so 该 驱动 仅 looks 用于 any of these on that part —
see [TAS5805M 开发板](#tas5805m-boards).

To 安装 one:

1. Tune 该 part in PPC3 和 export either 该 I2C log (`.cfg`) 或 该 C header, at 每个
   sample rate you want covered.
2. Convert it:
   ```bash
   python3 components/dac_tas58xx/ppc3_convert.py my_tuning_44k1.cfg -o tas5825m_fw-44100.bin
   ```
   A log that drives 两者 amplifiers carries writes 用于 每个, so pick one 与
   `--dev 98` 或 `--dev 9a` 和 convert it twice.
3. Copy 该 result to `data/hf/` 用于 a serial 刷写, 或 upload it 通过 WiFi:
   ```bash
   curl -X POST "http://<device-ip>/api/fs/upload?path=/spiffs/hf/tas5825m_fw-44100.bin" \
        --data-binary @tas5825m_fw-44100.bin
   ```
4. Reboot.

Delete 该 文件 to go back to 该 构建-in flow.

!!! 警告

    A dump owns 该 configuration, so 该 驱动 stops writing its own signal-path
    defaults 和 trusts 该 tuning instead. Get 该 clocking 或 该 I2S format wrong
    和 该 part 将 not play — keep a serial console attached 该 首次 time.

该 biquad addresses 是 identical in 每个 documented flow on 两者 该 TAS5825M 和 该
TAS5805M, so 该 Equaliser 页面 keeps working on top of a dump. A dump that selects an
undocumented flow 是 该 exception: nothing guarantees its coefficients live 其中 该
页面 expects them.

## Variants

| Environment | Chip | 蓝牙 | Prebuilt | 说明 |
| --- | --- | :-: | :-: | --- |
| `esparagus-audio-brick` | ESP32 | — | — | AirPlay + 以太网 |
| `esparagus-audio-brick-bt` | ESP32 | yes | yes | Adds 蓝牙 A2DP |
| `esparagus-audio-brick-s3` | ESP32-S3 | — | yes | S3 pinout, PSRAM, no 蓝牙 Classic on this 芯片 |
| `esparagus-audio-brick-dual-dac` | ESP32-S3 | — | yes | [Dual](esparagus-audio-brick-dual-dac.md), two amplifiers: stereo at 0x4C, 第二 at 0x4D |
| `esparagus-audio-brick-dual-uac` | ESP32-S3 | — | yes | [Dual](esparagus-audio-brick-dual-dac.md) as a USB 音频 设备 |

该 ones marked prebuilt 是 in 该
[browser installer](../getting-started/flashing.md). On 该 ESP32 该 published binary 是
该 蓝牙 one, so 构建 `esparagus-audio-brick` yourself if you want that RAM back.

蓝牙 Classic exists 仅 on the original ESP32, so 该 `-bt` 构建 has no S3
equivalent; an S3 brick reaches 该 网络 通过 以太网 或 WiFi. 该 Dual has two
amplifiers 和 a pinout of its own, 和 gets [its own 页面](esparagus-audio-brick-dual-dac.md).

### Esparagus Louder

该 Esparagus Louder 是 该 相同 amplifier design on a 开发板 of its own.

| Environment | Chip | 蓝牙 | Prebuilt |
| --- | --- | :-: | :-: |
| `esparagus-louder` | ESP32 | — | — |
| `esparagus-louder-bt` | ESP32 | yes | yes |
| `esparagus-louder-s3` | ESP32-S3 | — | yes |

```bash
pio run -e esparagus-louder-s3 -t upload
pio run -e esparagus-louder-s3 -t uploadfs
```

## Related

- [蓝牙 A2DP](../features/bluetooth.md)
- [以太网 (W5500)](../features/ethernet.md)
- [构建环境](../reference/build-environments.md)
