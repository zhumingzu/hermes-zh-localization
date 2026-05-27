# Hermes Agent CLI 汉化包

将 Hermes Agent CLI 启动界面全部汉化为简体中文。

## 快速安装

```bash
# 1. 克隆仓库
git clone https://github.com/zhumingzu/hermes-zh-localization.git
cd hermes-zh-localization

# 2. 运行智能安装脚本
python3 smart_install.py

# 3. 重启 Hermes
hermes gateway restart
```

## 文件说明

| 文件 | 用途 |
|------|------|
| `smart_install.py` | 智能安装脚本（推荐） |
| `install.py` | 旧版安装脚本 |
| `uninstall.py` | 卸载脚本 |
| `translations.json` | 翻译映射 |
| `tips_zh.py` | 翻译后的提示语 |

## 智能安装 vs 旧版安装

### 智能安装（推荐） `smart_install.py`

- ✅ 只替换字符串内容，不修改代码结构
- ✅ 兼容不同版本的 Hermes
- ✅ 安全可靠，不会破坏代码
- ✅ 自动检测并翻译当前版本的内容

### 旧版安装 `install.py`

- ⚠️ 会覆盖整个文件
- ⚠️ 可能与不同版本的 Hermes 不兼容
- ⚠️ 可能破坏代码结构

## 支持的汉化内容

- ✅ 启动横幅版本标签
- ✅ 工具/技能/MCP服务器标题
- ✅ 会话信息标签
- ✅ YOLO模式提示
- ✅ 退出语和恢复命令提示
- ✅ 约150条随机提示语

## 卸载/回滚

```bash
# 方法1：使用卸载脚本
python3 uninstall.py

# 方法2：手动回滚
cd ~/.hermes/hermes-agent
git checkout cli.py hermes_cli/banner.py hermes_cli/tips.py
```

## 升级后重新应用

Hermes 升级后需要重新运行汉化：

```bash
cd hermes-zh-localization
git pull
python3 smart_install.py
```

## 兼容性

- Hermes Agent v0.14.0+
- macOS / Linux / Windows (WSL)

## 注意事项

- Nous Research 等专有名词保留不译
- ASCII art logo 保留原样
- Rich markup 标签保持原样
- 升级后可能需要重新应用汉化

## License

MIT
