# OTA 更新

Once 该 设备 是 on your 网络 you 可以 更新 its firmware 通过 WiFi 无需
unplugging anything. USB 是 仅 needed 用于 该 very 首次 刷写.

1. Get 该 new firmware — either 构建 it (`pio run -e <env>` 或 `idf.py build`) 或
   download a `.bin` 从 该
   [releases 页面](https://github.com/wenghaoping/esp32-s3-airplay/releases/latest).
2. Open 该 设备's web interface. Find its IP in your router's list of 已连接 clients.
3. Use 该 firmware upload 页面 to 刷写 该 new version.

该 设备 reboots 转换为 该 new firmware 自动. Settings stored in NVS — 设备
name, WiFi credentials, 音量, EQ — survive 该 更新.

!!! 警告 "OTA 无法 change 该 partition table"

    If you 是 upgrading 从 a firmware 构建 before 该 SPIFFS `storage` partition
    existed, 该 首次 刷写 has to happen 通过 serial, because 该 partition layout
    itself changes. See [SPIFFS filesystem](spiffs.md#flashing-the-image).

## Updating 文件 无需 reflashing

Web 页面, 该 ST7789 background image 和 TAS57xx hybrid flow programs live on SPIFFS 和
可以 be replaced individually 通过 HTTP, 无需 touching 该 firmware:

```bash
curl -X POST "http://<device-ip>/api/fs/upload?path=/spiffs/www/index.html" \
     --data-binary @data/www/index.html
```

See 该 [文件 management API](spiffs.md#file-management-api) 用于 该 完整 设置 of endpoints.
