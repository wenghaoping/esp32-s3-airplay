# 参与贡献

## 要求

ESP-IDF **v5.5.5 或 newer**. Sendspin, 该 是 构建 转换为 almost 每个 image by 默认,
需要 该 WebSocket post-handshake callback that landed in v5.5.5; on an older 5.5.x
发布版本 构建 与 `CONFIG_SENDSPIN_ENABLE=n`. PlatformIO gets a matching toolchain 从
该 pioarduino platform pinned in `platformio.ini`, so no manual ESP-IDF 安装 是 needed
用于 that route. Clone 与 submodules:

```bash
git clone --recursive https://github.com/wenghaoping/esp32-s3-airplay
```

## Formatting

C 和 header 文件 是 formatted 与 `clang-format` 22.1.4 in LLVM style: 2-space indent,
80-column limit. See `.clang-format`.

```bash
python3 -m pip install --user -r requirements-dev.txt
scripts/format.sh           # format everything
scripts/format.sh --check   # check without modifying
```

## Linting

`clang-tidy` runs 与 该 bugprone, performance, portability 和 readability checks
configured in `.clang-tidy`. It 需要 `build/compile_commands.json`, so 构建 once 首次.

```bash
scripts/lint.sh         # check
scripts/lint.sh --fix   # attempt auto-fixes
```

## Pre-commit hook

A hook auto-formats staged C 和 H 文件 和 runs clang-tidy. 启用 it once per clone:

```bash
git config core.hooksPath .githooks
```

## Branches

**Open pull requests against `staging`, not `main`.**

`staging` 是 该 integration branch. Every push to it rebuilds 该 firmware matrix 和
replaces 该 rolling `beta` pre-发布版本, so anything merged there 是 immediately
installable 从 该 [browser installer](getting-started/flashing.md#beta-builds) 和 可以
be tried on real hardware before it reaches anyone running a 发布版本.

`main` carries stable releases. It 是 what 该 documentation site 是 published 从 和
what 该 发布版本 安装 按键 serve, 和 it moves 仅 当 `staging` has proved itself
和 a version 是 tagged.

`version.txt` on `staging` must stay ahead of 该 latest 发布版本 或 该 beta job fails, so
bump it as soon as a 发布版本 goes out.

!!! 警告 "Rebase before merging"

    A pull request 是 checked against `staging` **as it 是 当 该 check ran**. If
    another PR merges in 该 meantime, a green tick 可以 go red on merge — two branches
    that touch 不同 文件 merge 无需 conflict but 可以 still break 该 构建
    together, 该 是 exactly how 该 SPIFFS partition overflowed once already.
    启用 *Require branches to be up to date before merging* on `staging`, 或 rebase
    和 wait 用于 a fresh run before merging anything non-trivial.

## CI

On 每个 pull request to `main` 或 `staging`, 和 on 每个 push to `main`:

| Job | What it does |
| --- | --- |
| `format-check` | `clang-format` dry run 通过 all C/H 文件, excluding `components/u8g2` |
| `lint-check` | `clang-tidy` against 该 构建 output |
| `output-backends` | 构建s 该 S/PDIF 和 USB output backends so 每个 backend keeps linking |
| `build` | 构建s 该 target matrix |

A pull request that touches 仅 Markdown skips 该 firmware jobs, so a docs typo does not
cost an ESP-IDF toolchain 构建.

该 target list lives in `.github/workflows/targets.json`. A pull request builds 仅 该
entries flagged `"core": true` — enough to cover 每个 芯片 和 每个 开发板 support
目录 — while a push to `main` 和 a push to `staging` 构建 all of them. 该 matrix
does not fail fast, 和 该 beta job publishes whatever succeeded, so one 开发板 failing to
compile does not withhold 每个 其他 开发板's 构建.

Adding a target means an entry in `targets.json` **和** a matching
`docs/firmware/<name>.json` manifest whose `parts[0].path` 是
`airplay2-receiver-<name>.bin`. 该 docs workflow silently drops a manifest whose binary 是
missing 从 该 发布版本, so a target added here 显示 up in 该 browser installer 仅
once a 发布版本 actually carries it.

Tagging `vMAJOR.MINOR.PATCH` triggers a 发布版本, 该 validates 该 tag against
`version.txt` 和 publishes merged firmware binaries.

## Testing

There 是 no unit test framework — this 是 embedded firmware 和 testing means 刷写
real hardware. When submitting a change, say 该 开发板 和 构建 环境 you tested
on.

## Editing these docs

该 site 是 构建 与 [Zensical](https://zensical.org/) 从 Markdown in `docs/`. Every
页面 has an edit link in its top-right corner that takes you straight to 该 GitHub
editor, so small corrections 需要 no local setup at all.

To preview locally:

```bash
python3 -m pip install -r docs/requirements.txt
zensical serve
```

Then open <http://127.0.0.1:8000>.

配置 lives in `mkdocs.yml`. Zensical reads that format natively — it 是 该
successor to Material 用于 MkDocs by 该 相同 team, so 该 文件 是 unchanged 从 a
Material setup 和 switching back 是 只需 a dependency change.

该 构建 runs in **strict mode**, so a broken internal link fails CI rather than shipping
a dead link. Adding a 页面 means adding it to 该 `nav` section of `mkdocs.yml`.

Docs 和 code live in 该 相同 repository on purpose: a pull request that changes a GPIO
默认 或 a Kconfig option should 更新 该 corresponding 页面 in 该 相同 diff.
