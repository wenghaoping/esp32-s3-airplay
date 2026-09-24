# 首次启动

On its 首次 start 该 设备 has no WiFi credentials, so it brings up its own 网络 和
a captive portal 用于 you to configure it.

1. **Power 该 开发板** 通过 USB-C.
2. On a phone 或 laptop, join 该 WiFi 网络 **`ESP32-AirPlay-Setup`**.
3. A captive portal opens 自动. If it does not, browse to **`192.168.4.1`**.
4. Give 该 音箱 a name, 用于 示例 "Kitchen Speaker".
5. Select your home WiFi 网络 和 enter its password.
6. 该 设备 restarts 和 joins your 网络.
7. Open any 音乐 app, tap 该 AirPlay icon 和 pick your 音箱.

That's it. Settings 是 stored in NVS 和 survive reboots 和 firmware updates.

!!! tip "If 该 WiFi 连接 fails"

    After several failed attempts 该 设备 returns to setup mode 自动, so you
    可以 rejoin `ESP32-AirPlay-Setup` 和 correct 该 credentials.

## 该 web interface

Once 该 设备 是 on your 网络 you 可以 reach its web interface 从 a browser. Find
its IP address in your router's list of 已连接 clients, 或 via 该 serial monitor.

| Page | Purpose |
| --- | --- |
| `/` | Setup 和 控制 panel — 设备 name, WiFi, 音量 |
| `/logs` | Live log viewer |
| `/bq` | Per-section biquad EQ 和 crossovers, on TAS5825M 开发板 |

该 相同 interface 是 used 用于 [OTA firmware updates](../reference/ota.md), so USB 是 仅
needed 用于 该 very 首次 刷写.

## 遇到问题？

If 该 setup 网络 never appears, 该 portal 显示 "文件 not found", 或 you get silence
after connecting, see [故障排除](../troubleshooting.md).
