#!/bin/bash
# Hermes Agent CLI 汉化快速安装脚本
# 用法: curl -fsSL https://raw.githubusercontent.com/your-repo/hermes-zh/main/quick_install.sh | bash

set -e

echo "========================================"
echo "  Hermes Agent CLI 汉化安装程序"
echo "========================================"
echo

# 检查 Hermes 是否安装
if ! command -v hermes &> /dev/null; then
    echo "错误: 找不到 hermes 命令"
    echo "请先安装 Hermes Agent: https://github.com/NousResearch/hermes-agent"
    exit 1
fi

HERMES_HOME="$HOME/.hermes/hermes-agent"
if [ ! -d "$HERMES_HOME" ]; then
    echo "错误: 找不到 Hermes 源码目录: $HERMES_HOME"
    exit 1
fi

# 创建临时目录
TEMP_DIR=$(mktemp -d)
echo "创建临时目录: $TEMP_DIR"

# 下载汉化包（如果从远程安装）
# 如果是本地安装，跳过下载步骤
if [ -f "hermes-zh-localization.tar.gz" ]; then
    echo "使用本地汉化包..."
    tar -xzf hermes-zh-localization.tar.gz -C "$TEMP_DIR"
else
    echo "下载汉化包..."
    # 替换为实际的下载链接
    # curl -fsSL "https://github.com/your-repo/hermes-zh/releases/latest/download/hermes-zh-localization.tar.gz" -o "$TEMP_DIR/hermes-zh-localization.tar.gz"
    # tar -xzf "$TEMP_DIR/hermes-zh-localization.tar.gz" -C "$TEMP_DIR"
    echo "错误: 请提供汉化包文件"
    exit 1
fi

# 运行安装脚本
cd "$TEMP_DIR/hermes-zh-localization"
python3 install.py

# 清理
rm -rf "$TEMP_DIR"

echo
echo "安装完成！"
