# ESP32-S3 AirPlay 音箱操作手册

本手册适用于本项目当前使用的 **ESP32-S3-N16R8** 开发板（16 MB Flash、8 MB PSRAM）和外接 I2S DAC（例如 PCM5102A）。

对应的 PlatformIO 构建环境为：`esp32s3`。

## 1. 它能做什么

烧录本项目后，开发板会成为一台局域网 AirPlay 接收器：

- iPhone、iPad、Mac 可在 AirPlay 列表中选择它并投放音频。
- 音频通过 I2S 输出到外接 DAC，再接有源音箱或功放。
- 设备提供网页管理页，可修改设备名、Wi-Fi、音量，查看运行日志和更新固件。
- ESP32-S3 不支持本项目中的经典蓝牙 A2DP 接收；如需该功能，应使用原版 ESP32 的 `*-bt` 构建。

## 2. 接线（PCM5102A 示例）

| ESP32-S3 | PCM5102A | 作用 |
| --- | --- | --- |
| 5V | VIN | DAC 供电 |
| GPIO11 | BCK | I2S 位时钟 |
| GPIO12 | DIN | I2S 音频数据 |
| GPIO13 | LCK / LRCK | 左右声道时钟 |
| GPIO14 | GND | 软件拉低的地线 |
| GND | GND | 建议额外连接的公共地线 |

> 如果 DAC 没有声音，先检查 ESP32-S3 板上 VIN/VOUT 焊盘是否已连通；部分板子默认未桥接，DAC 会得不到 5 V 供电。

## 3. 首次准备

### 3.1 获取项目（首次从 Git 克隆时）

```bash
git clone --recursive https://github.com/wenghaoping/esp32-s3-airplay
cd esp32-s3-airplay
```

如果项目已经下载，但构建提示缺少 `u8g2`，在项目根目录执行：

```bash
git submodule update --init --recursive
```

### 3.2 选择正确的构建环境

在 VS Code 的 PlatformIO 左侧栏中选择：

```text
Project Tasks → esp32s3
```

不要选择 `squeezeamp`、`esparagus-*` 或 `*-bt`，它们分别对应特定成品功放板或原版 ESP32。

## 4. 编译与首次写入

将开发板用**可传输数据**的 USB 线连接电脑，然后在项目根目录执行：

```bash
# 编译固件，不写入开发板
pio run -e esp32s3

# 编译并通过 USB 写入固件
pio run -e esp32s3 -t upload

# 写入网页设置界面和数据文件（首次写入必须执行）
pio run -e esp32s3 -t uploadfs
```

也可以在 PlatformIO 的 `esp32s3` 任务下依次点击：

1. `Upload`
2. `Upload Filesystem Image`

> `Upload` 只写入固件。漏掉 `Upload Filesystem Image` 时，设备能启动，但设置页会显示“file not found”。

### 常用命令说明

| 命令 | 用途 |
| --- | --- |
| `pio run -e esp32s3` | 仅编译，检查代码是否能通过构建。 |
| `pio run -e esp32s3 -t upload` | 编译并通过 USB 写入应用固件。 |
| `pio run -e esp32s3 -t uploadfs` | 写入 SPIFFS 文件系统：网页配置界面、图片等数据。 |
| `pio run -e esp32s3 -t monitor` | 打开 115200 波特率串口日志；按 `Ctrl+C` 退出。 |
| `pio run -e esp32s3 -t erase` | 清空整块 Flash，彻底重置设备；执行后必须重新写入固件和文件系统。 |

## 5. 首次联网与使用

1. 写入完成后，开发板会重启。
2. 在手机或电脑 Wi-Fi 列表中连接 **`ESP32-AirPlay-Setup`**。
3. 若没有自动弹出配置页，在浏览器访问 [http://192.168.4.1](http://192.168.4.1)。
4. 设置 AirPlay 设备名称，选择家中 Wi-Fi 并输入密码。
5. 保存后设备会自动重启并加入该 Wi-Fi；设置热点会关闭。
6. 在路由器的已连接设备列表找到它的 IP，或尝试访问：

```text
http://ESP32-AirPlay.local
```

7. iPhone / iPad / Mac 与设备接入同一局域网后，在音乐 App 或控制中心点击 AirPlay 图标，选择设置的设备名称即可播放。

本次配置成功时，串口会显示类似：

```text
wifi: Got IP: 192.168.x.x
main: AirPlay ready
```

## 6. 日常管理

设备联网后，打开它的 IP 地址或 `ESP32-AirPlay.local`：

- `/`：设备名称、Wi-Fi、音量等主控制页。
- `/logs`：实时日志页。
- `/bq`：仅特定 TAS58xx 功放板的 EQ / 分频设置页。

路由器重启后 IP 可能改变。优先用 `ESP32-AirPlay.local`；若无法打开，在路由器客户端列表按设备名或 MAC 地址查找新 IP。

## 7. 更换 Wi-Fi / 搬到新环境

### 情况 A：仍能连接旧网络

1. 让手机或电脑接入当前网络。
2. 打开设备网页管理页（IP 或 `ESP32-AirPlay.local`）。
3. 在 Wi-Fi 设置中选择新网络、输入密码并保存。
4. 设备会自动重启并加入新网络。
5. 电脑/手机也切换到新网络，再通过新路由器的客户端列表找到设备。

### 情况 B：已搬走，旧网络已不存在

无需刷机或清除设置：

1. 给设备上电，并等待约 30 秒到 1 分钟。
2. 它会尝试连接之前保存的 Wi-Fi；连续失败 5 次后，会重新开启 **`ESP32-AirPlay-Setup`**。
3. 连接该热点，访问 [http://192.168.4.1](http://192.168.4.1)。
4. 按首次联网流程设置新 Wi-Fi。

### 新网络要求

- 普通 ESP32-S3 仅支持 **2.4 GHz Wi-Fi**。
- 不支持仅 WPA3 的网络；路由器应设置为 WPA2，或 WPA2/WPA3 混合模式。

## 8. 重启与彻底重置

### 普通重启

按开发板上的 `EN` 或 `RST` 键，或拔插 USB 电源。

普通重启会保留 Wi-Fi、设备名、音量和其他设置。

### 恢复到未配置状态

项目没有单独的“只清 Wi-Fi”物理按钮。若自动回到设置热点仍无法解决问题，可执行彻底清除：

```bash
pio run -e esp32s3 -t erase
pio run -e esp32s3 -t upload
pio run -e esp32s3 -t uploadfs
```

这会清除固件、Wi-Fi、设备名、网页文件及所有持久化设置；重新写入后按“首次联网与使用”配置。

## 9. 快速排障

| 现象 | 优先检查 |
| --- | --- |
| 编译报 `Failed to resolve component 'u8g2'` | 执行 `git submodule update --init --recursive`。 |
| 串口报 `No module named 'intelhex'` | 修复 PlatformIO Python 依赖：`~/.platformio/penv/bin/python -m pip install intelhex`。 |
| 连上设置热点但网页显示 `file not found` | 再执行 `pio run -e esp32s3 -t uploadfs`。 |
| 看不到 `ESP32-AirPlay-Setup` | 等待至少 30 秒；若已有可用 Wi-Fi 凭据，设备会直接连旧网络。可开串口监视器查看状态。 |
| 设备不加入新 Wi-Fi | 确认使用 2.4 GHz，且不是 WPA3-only；等待多次重连失败后设置热点会恢复。 |
| AirPlay 能发现但没声音 | 检查 DAC 供电和 GPIO11/BCK、GPIO12/DIN、GPIO13/LCK 接线；同时检查网页设备音量和手机音量。 |

## 10. 更新固件

设备已联网后，可以在网页管理页上传新固件进行 OTA 更新，通常不需要重新接 USB。USB 写入仍适合首次安装、分区变化或彻底重置后的恢复。
