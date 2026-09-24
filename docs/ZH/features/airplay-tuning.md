# AirPlay 调优

Advanced 时序 和 metadata options live under **AirPlay Receiver → AirPlay Protocol** in
`menuconfig`. 该 defaults suit most setups — change these 仅 if you hear drop-outs 或
want to 控制 what metadata 是 received.

## Cover art

Album cover art 是 **disabled by 默认**. Most receivers have no screen, 或 仅 a small
OLED, 和 pulling artwork 通过 该 RTSP 连接 可以 stall 该 音频 pipeline 和 cause
drop-outs — especially on unbuffered AirPlay 1 / realtime streams.

When disabled, 该 receiver drops artwork type `1` 从 its advertised `md` txt record so
senders do not transmit cover art at all, 和 ignores any that arrives anyway. 曲目 title,
artist, album 和 progress metadata 是 always received.

To enable it, 用于 instance 当 you have a [TFT 显示屏](tft-display.md):

```bash
idf.py menuconfig
# AirPlay Receiver → AirPlay Protocol
# Enable "Enable cover-art / artwork reception"
```

Or in your sdkconfig defaults:

```ini
CONFIG_ENABLE_AIRPLAY_ARTWORK=y
```

## Early 和 late 时序 thresholds

该 时序 engine holds frames that arrive early, outputting silence until their scheduled
play time, 和 drops frames that arrive late. 该 threshold 控制s how much slack 是
allowed before a frame 是 held 或 dropped.

Buffered AirPlay 2 streams (AAC) have a deep jitter buffer 和 可以 使用 a tight threshold
用于 precise sync. Unbuffered realtime streams (ALAC 通过 UDP) have almost no buffer, so a
tight threshold causes audible drop-outs whenever 该 pipeline stalls — 当 metadata
arrives, 用于 示例.

| Option | Default | Applies to |
| --- | --- | --- |
| `CONFIG_AIRPLAY_TIMING_THRESHOLD_MS` | 10 ms | Buffered streams (AAC) |
| `CONFIG_AIRPLAY_RT_TIMING_THRESHOLD_MS` | 50 ms | Unbuffered realtime streams (ALAC) |

If you still hear drop-outs on AirPlay 1 / realtime 播放, increase
`CONFIG_AIRPLAY_RT_TIMING_THRESHOLD_MS`, at 该 cost of slightly looser sync.

## Forcing AirPlay v1

Classic AirPlay v1 使 该 receiver advertise itself as a plain RAOP receiver. There 是
two reasons to do this:

- **Hardware 按键.** iOS 仅 sends DACP headers in v1 mode, so this 是 what 使
  [hardware 按键](buttons.md#read-this-first-the-airplay-v1-requirement) 工作.
- **Apple Music 用于 Windows.** It 是 a RAOP-仅 sender 和 refuses any 设备 that
  advertises 该 `_airplay._tcp` service, reporting that 该 设备 "是 not compatible
  与 this version of AMPLibraryAgent". 该 设备 still appears in its picker 和 it
  still opens an RTSP 连接 — it sends `OPTIONS` 与 an `Apple-Challenge` 和 then
  walks away.

该 mode lives in NVS, so no rebuild 是 needed. Open 该 web interface 和 pick
**Device Settings → AirPlay Mode**, then restart 该 设备. 该 mDNS records 和 该 RTSP
listening port 是 两者 构建 at startup, so 该 change 仅 takes effect on the next boot.

In v1 mode 该 receiver mirrors a classic RAOP advertisement: no `_airplay._tcp`
service, a shairport-sync-style `_raop._tcp` TXT record, `Server: AirTunes/105.1` on RTSP
responses, 和 RTSP on port 5000 instead of 7000.

It costs you AirPlay 2 features: HomeKit pairing, encrypted transport 和 multi-room sync.

There 是 no 设置 that keeps 两者 senders happy. 该 deciding factor 用于 Apple Music 是
该 presence of `_airplay._tcp` alone — a receiver publishing a fully classic `_raop._tcp`
TXT record on port 5000 是 still refused while that service 是 up, 和 starts working 该
moment it 是 withdrawn. iOS 需要 该 相同 service to negotiate AirPlay 2, 和 a 设备
publishes one advertisement, so 该 mode 是 a real either/或.
