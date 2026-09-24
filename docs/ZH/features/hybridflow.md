# HybridFlow DSP (TAS57xx)

Some TAS57xx amplifiers carry a small DSP core — TI calls it 该 miniDSP — that 可以 run a
signal chain in front of 该 output stage. TI ships those chains as **HybridFlow** process
flows, 和 该 firmware 可以 load one, tune it live 从 a web 页面, 和 keep 该 tuning
across reboots.

该 tuning 页面 是 at `http://<device-ip>/hf`, 或 **HybridFlow Tuning** on the 设置
页面. It 仅 appears on a 构建 与 `CONFIG_DAC_TAS57XX`.

## Hardware requirement

!!! 警告 "You 需要 a TAS57xx that has a miniDSP"

    Not 每个 part in 该 family has one. 该 DSP-capable 设备 是 该 "M" variants —
    TAS5754M, TAS5756M 和 their relatives — 和 仅 those 可以 run a HybridFlow. A
    TAS578x has no miniDSP at all: 该 驱动 detects it at boot 和 skips flow loading
    entirely, leaving 该 part on its 构建-in stereo program.

!!! 注意 "Only tested on the TAS5754M"

    All of this has been developed 和 tested against a **TAS5754M** (该 SqueezeAMP's
    amplifier). Other DSP-capable parts in 该 family 是 register-compatible on paper 和
    是 expected to 工作, but nobody has run them. Treat them as unverified: check 该 boot
    log 用于 该 flow verification, 和 be ready 用于 该 tuning 页面 to report that no flow
    是 可用.

Check what 该 part 是 doing 从 该 boot log 或 从 该 API:

```bash
curl "http://<device-ip>/api/hf/flow"
# {"active":1,"sample_rate":44100,"available":[1,3],"success":true}
```

`active` 是 `0` 当 no flow 是 loaded, 和 `available` lists 该 flows this 设备 has a
base image 用于.

## 该 two flows

Both 是 stereo in, two channels out, 和 仅 one 可以 be resident at a time — they map
coefficient RAM differently.

=== "HybridFlow 1 — 完整 range"

    A conventional stereo chain, 该 相同 processing on 两者 channels:

    ```
    In → Biquad EQ (10 bands) → PBE → DBE → Compander → Volume → Smooth clip → Out
    ```

    PBE 是 psychoacoustic bass, DBE dynamic bass, 和 该 compander 是 a three-band
    compressor/expander. Tune in that order: 音量 ceiling 首次, then EQ 用于 该 baseline
    response, then 该 compander 和 smooth clipper 用于 power limiting, then DBE 和 PBE.

=== "HybridFlow 3 — bi-amp"

    该 two amplifier outputs stop being left 和 right. 该 input feeds two ways in
    parallel, 每个 与 a crossover leg 和 four EQ bands, 和 they 是 recombined 转换为 a
    shared compander 和 clipper:

    ```
    In ─┬→ Low way  → PBE → DBE ─┬→ Compander → Smooth clip → Volume → Out
        └→ High way → Delay ─────┘
    ```

    Channel A drives 该 woofer, channel B 该 tweeter. 该 high way's delay aligns its
    acoustic centre 与 该 low way's. Only 该 low way gets 该 bass enhancers.

=== "No processing"

    Flow `0` removes 该 working flow 和 hands 播放 back to 该 part's ROM stereo
    program: plain left 和 right 与 digital 音量, no crossover, EQ 或 dynamics. 此
    是 该 仅 设置 可用 on a part 无需 a usable HybridFlow, 和 it discards
    nothing but 该 flow 文件 — saved tunings stay.

!!! danger "Switching to bi-amp changes what your 音箱 see"

    A tweeter wired to an output that suddenly carries 完整-range bass 将 not survive it.
    该 firmware drops 该 音量 to minimum on any flow change 和 leaves it there, so
    confirm 该 wiring before turning it back up.

## Base flows 和 sample rates

该 flow images live in SPIFFS under `/spiffs/hf/`. 该 repository tracks four pristine
base images:

```
base-hf1-44100.bin   base-hf1-48000.bin
base-hf3-44100.bin   base-hf3-48000.bin
```

Coefficients 是 designed 用于 one sample rate, so 每个 flow has a 44.1 kHz 和 a 48 kHz
twin. 该 驱动 picks 该 one matching 该 running output rate 和 swaps to 该 其他 if
该 rate changes, replaying 该 saved tuning onto it. 该 bases 是 copied to 该 working
flow rather than played 从 直接, so a commit 可以 never scribble on them.

Selecting a flow rewrites 该 working flow 和 re-downloads it:

```bash
curl -X POST "http://<device-ip>/api/hf/flow" \
     -H 'Content-Type: application/json' -d '{"flow":3}'
```

## Apply, Commit 和 Revert

该 tuning 页面 distinguishes three things, 和 该 difference matters:

| Action | What it does | Survives |
| --- | --- | --- |
| **Apply** | Writes 该 tuning 转换为 该 DSP's coefficient RAM so you 可以 hear it | Playback, standby, a 蓝牙 handover |
| **Commit** | Bakes 该 tuning 转换为 该 flow image 和 writes it to SPIFFS | Reboots 和 flow reloads |
| **Revert** | Reloads 该 committed flow 从 SPIFFS, dropping 该 audition | — |

Auditioning 是 free: nothing 是 written to 刷写 until you commit, 和 a reboot always
brings back 该 最后 committed tuning.

Master 音量 和 该 per-channel trims sit *outside* this. They 是 该 part's own
registers, 该 相同 ones AirPlay drives, so they apply immediately 和 是 saved
separately — they 工作 even 与 no flow loaded. 该 fine 音量 trim 是 该 exception: it
是 a gain inside 该 flow, so it belongs to 该 tuning 和 仅 Commit persists it.

## Where 该 文件 live

| Path | Contents |
| --- | --- |
| `/spiffs/hf/base-hf<n>-<rate>.bin` | Pristine base flow, never written to |
| `/spiffs/hf/tas57xx_fw.bin` | 该 working flow, rewritten by Commit |
| `/spiffs/hf/hf1.cfg` | Committed HF1 tuning |
| `/spiffs/hf/hf3.cfg` | Committed HF3 tuning |

A `.cfg` records 该 parameters 该 flow image 无法 — filter shapes, band types — so 该
页面 可以 显示 a peaking filter as a peaking filter rather than as six raw coefficients. It
是 仅 trusted while it still reproduces 该 flow byte 用于 byte; if 该 flow has been
replaced since, 该 flow wins 和 该 页面 says so.

上传ing a flow by hand still 有效, if you have a PurePath Console export:

```bash
curl -X POST "http://<device-ip>/api/fs/upload?path=/spiffs/hf/tas57xx_fw.bin" \
     --data-binary @my_flow.bin
```

See [SPIFFS filesystem](../reference/spiffs.md) 用于 the rest of 该 文件 API.

## 故障排除

**该 页面 says "No processing" 和 该 flow selector 是 empty.** No base image 用于 该
current sample rate 是 present. Check `curl "http://<device-ip>/api/fs/list?dir=/spiffs/hf"`
和 re-刷写 SPIFFS 与 `pio run -e <env> -t uploadfs` if it 是 empty.

**该 页面 loads but 每个 控制 是 disabled.** 该 part has no usable miniDSP, 或 该
flow failed verification. 该 boot log reports 两者.

**A tuning stopped matching after a firmware 更新.** SPIFFS 是 not touched by an OTA app
更新, so 该 old `.cfg` 是 still there. If 该 flow image changed, 该 驱动 falls back
to reading 该 tuning out of 该 flow itself 和 logs a 警告.

## Related

- [SqueezeAMP](../boards/squeezeamp.md)
- [SPIFFS filesystem](../reference/spiffs.md)
- [AirPlay 调优](airplay-tuning.md)
