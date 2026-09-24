# 自定义开发板 configuration

If you 是 porting to your own hardware, you 可以 define a custom 构建 环境 无需
touching `platformio.ini`. Create a **`user_platformio.ini`** 文件 — 该 main config
already pulls it in via `extra_configs`, so PlatformIO picks it up 自动.

## How it 有效

1. Pick an existing 环境 to extend, 用于 示例 `esp32s3` 或 `esp32wrover-dev`.
2. Create a `config/sdkconfig.user.<your_board>` 文件 holding your 开发板-specific Kconfig
   overrides: GPIO pins, DAC selection, 显示 设置 和 so on.
3. Add an 环境 to `user_platformio.ini` that chains your sdkconfig 文件 after 该
   base defaults.

## 示例

Say you have a custom ESP32 开发板 called "myboard" 与 a SqueezeAMP-compatible DAC, but
不同 GPIO assignments 和 an OLED 显示屏. Create two 文件.

`config/sdkconfig.user.myboard` — your 开发板-specific overrides:

```ini
# I2S pin assignments
CONFIG_I2S_BCK_PIN=5
CONFIG_I2S_WS_PIN=18
CONFIG_I2S_DO_PIN=19

# Enable OLED display
CONFIG_DISPLAY_ENABLED=y
CONFIG_DISPLAY_I2C_SDA=21
CONFIG_DISPLAY_I2C_SCL=22
```

`user_platformio.ini` — your 构建 环境:

```ini
[env:myboard]
extends = env:esp32s3
board_build.cmake_extra_args =
    "-DSDKCONFIG_DEFAULTS=config/sdkconfig.defaults;config/sdkconfig.defaults.esp32s3;config/sdkconfig.user.myboard"
```

Then 构建 和 刷写:

```bash
pio run -e myboard -t upload
pio run -e myboard -t uploadfs
```

## 说明

- Sdkconfig defaults 是 applied **left to right** — later 文件 override earlier ones, so
  your `config/sdkconfig.user.*` must come 最后.
- `config/sdkconfig.user.*` 文件 是 gitignored, so they 将 not pollute 该 repository.
- If you change any sdkconfig defaults, delete 该 cached `sdkconfig.<env>` 文件 before
  rebuilding, otherwise 该 old values 是 reused.
- You 可以 extend any base 环境: 使用 `squeezeamp` 或 `squeezeamp-bt` 用于 TAS57xx
  开发板, `esparagus-audio-brick` 或 `esparagus-audio-brick-bt` 用于 TAS58xx 开发板, 和
  `esp32s3` 用于 S3-based 开发板.

## Related

- [构建环境](../reference/build-environments.md)
- [系统架构](../reference/architecture.md)
