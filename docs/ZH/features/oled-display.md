# OLED 显示屏

A small OLED screen 可以 显示 该 当前 playing track: title, artist, album, a progress
bar 和 播放 time. Long text scrolls 自动 和 a pause indicator appears 当
播放 是 paused.

These panels 是 widely 可用 用于 $1–2. Search 用于 "0.96 inch OLED I2C SSD1306".

## Supported displays

| Controller | Resolution | Bus |
| --- | --- | --- |
| SSD1306 | 128×64 | I2C 或 SPI |
| SH1106 | 128×64 | I2C 或 SPI |
| SSD1309 | 128×64 | I2C 或 SPI |

128×32 panels (SSD1306 和 SH1106) 也 工作 和 switch to a compact two-line layout.

## Wiring (I2C, 该 默认)

| OLED pin | ESP32 GPIO | 功能 |
| --- | --- | --- |
| SDA | 21 | I2C data |
| SCL | 22 | I2C clock |
| VCC | 3.3 V | Power |
| GND | GND | Ground |

该 默认 I2C address 是 `0x3C`. If your panel 使用 `0x3D`, change it under
**AirPlay Receiver → Display 配置**.

## Enabling 该 显示

该 显示 是 **disabled by 默认**.

=== "ESP-IDF"

    ```bash
    idf.py menuconfig
    # AirPlay Receiver → Display Configuration
    #   Enable "Enable OLED display"
    #   Select your driver (SSD1306, SH1106 or SSD1309)
    #   Select bus type (I2C or SPI) and set GPIO pins if needed
    ```

=== "PlatformIO"

    Run menuconfig through PlatformIO:

    ```bash
    pio run -e esp32s3 -t menuconfig
    ```

    Or add 该 options to your sdkconfig defaults 直接:

    ```ini
    CONFIG_DISPLAY_ENABLED=y
    CONFIG_DISPLAY_I2C_SDA=21
    CONFIG_DISPLAY_I2C_SCL=22
    ```

## Options

| Option | Default | Description |
| --- | --- | --- |
| Display 驱动 | SSD1306 | SSD1306, SH1106 或 SSD1309 |
| Display height | 64 pixels | 64 或 32 |
| Bus type | I2C | I2C 或 SPI |
| I2C SDA GPIO | 21 | Data line, I2C mode |
| I2C SCL GPIO | 22 | Clock line, I2C mode |
| I2C address | 0x3C | 7-bit address, 0x3C 或 0x3D |
| Flip 显示 | No | Rotate output 180° |
| Refresh interval | 500 ms | How often 该 显示 redraws, 100–5000 ms |

SPI mode exposes additional GPIO 设置 用于 CLK, MOSI, CS, DC 和 RST.

!!! 注意 "Submodules 需要"

    OLED rendering 使用 该 `u8g2` 和 `u8g2-hal-esp-idf` git submodules. Clone 与
    `--recursive`, 或 run `git submodule update --init --recursive` in an existing
    checkout, otherwise 该 构建 fails.
