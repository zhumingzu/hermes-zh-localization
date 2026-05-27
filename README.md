# Hermes Agent CLI 汉化包

将 Hermes Agent CLI 启动界面全部汉化为简体中文。

## 快速安装

```bash
# 1. 下载或克隆本项目
# 2. 运行安装脚本
python install.py

# 3. 重启 Hermes
hermes gateway restart
```

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
python uninstall.py

# 方法2：手动回滚
cd ~/.hermes/hermes-agent
git checkout cli.py hermes_cli/banner.py hermes_cli/tips.py
```

## 升级后重新应用

Hermes 升级后需要重新运行汉化：

```bash
python install.py
```

## 文件说明

- `install.py` - 安装脚本
- `uninstall.py` - 卸载脚本
- `translations.json` - 所有翻译映射
- `README.md` - 本文档

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
