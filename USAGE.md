# Hermes Agent CLI 汉化包 - 使用指南

## 📦 汉化包内容

```
hermes-zh-localization/
├── README.md              # 项目说明
├── install.py             # 安装脚本
├── uninstall.py           # 卸载脚本
├── translations.json      # 翻译映射（cli.py, banner.py）
├── tips_zh.py             # 翻译后的 tips.py（150条提示）
└── quick_install.sh       # 快速安装脚本
```

## 🚀 在其他电脑上使用

### 方法1：直接复制文件夹

1. **复制汉化包到目标电脑**
   ```bash
   # 在源电脑打包
   cd ~
   tar -czf hermes-zh-localization.tar.gz hermes-zh-localization/
   
   # 传输到目标电脑（可以用 scp、U盘、网盘等）
   scp hermes-zh-localization.tar.gz user@target-pc:~/
   ```

2. **在目标电脑解压并安装**
   ```bash
   cd ~
   tar -xzf hermes-zh-localization.tar.gz
   cd hermes-zh-localization
   python3 install.py
   ```

3. **重启 Hermes**
   ```bash
   hermes gateway restart
   # 或者在 CLI 中输入 /reset
   ```

### 方法2：使用 Git 仓库

1. **将汉化包推送到 Git 仓库**
   ```bash
   cd ~/hermes-zh-localization
   git init
   git add .
   git commit -m "Hermes CLI 中文汉化包"
   git remote add origin https://github.com/yourusername/hermes-zh-localization.git
   git push -u origin main
   ```

2. **在目标电脑克隆并安装**
   ```bash
   git clone https://github.com/yourusername/hermes-zh-localization.git
   cd hermes-zh-localization
   python3 install.py
   ```

### 方法3：使用一键安装脚本

1. **在目标电脑下载并运行**
   ```bash
   # 如果汉化包在本地
   cd ~/hermes-zh-localization
   chmod +x quick_install.sh
   ./quick_install.sh
   ```

## 🔄 升级后重新汉化

Hermes 升级后，汉化可能被覆盖。重新运行安装脚本即可：

```bash
cd ~/hermes-zh-localization
python3 install.py
```

## 🗑️ 卸载汉化

```bash
cd ~/hermes-zh-localization
python3 uninstall.py
```

或者手动恢复：
```bash
cd ~/.hermes/hermes-agent
git checkout cli.py hermes_cli/banner.py hermes_cli/tips.py
hermes gateway restart
```

## 📝 汉化内容

### 启动界面
- ✅ 版本标签：Hermes 智能代理 v{x.x.x}
- ✅ 工具/技能/MCP服务器标题
- ✅ 会话信息标签
- ✅ YOLO模式提示
- ✅ 运行时信息

### 交互提示
- ✅ 退出语：再见! ⚕
- ✅ 恢复命令提示
- ✅ 未知命令提示
- ✅ 工具集显示

### 随机提示（约150条）
- ✅ 斜杠命令说明
- ✅ CLI标志说明
- ✅ 配置选项说明
- ✅ 工具使用技巧
- ✅ 快捷键说明

## ⚠️ 注意事项

1. **Nous Research** 等专有名词保留不译
2. **ASCII art logo** 保留原样
3. **Rich markup 标签** 保持原样
4. **变量占位符**（如 {N}, {VERSION}）保持原样
5. 升级后可能需要重新应用汉化

## 🛠️ 故障排除

### 问题：安装后没有生效
```bash
# 1. 检查文件是否修改成功
cd ~/.hermes/hermes-agent
git status

# 2. 重启 Hermes
hermes gateway restart

# 3. 或者在 CLI 中重置
/reset
```

### 问题：汉化后出现乱码
```bash
# 恢复英文
cd ~/hermes-zh-localization
python3 uninstall.py
```

### 问题：找不到 Hermes 安装目录
```bash
# 检查 Hermes 是否安装
hermes --version

# 检查源码目录
ls -la ~/.hermes/hermes-agent/
```

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📧 联系方式

如有问题，请在 GitHub 上提 Issue。
