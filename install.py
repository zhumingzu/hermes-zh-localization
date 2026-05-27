#!/usr/bin/env python3
"""
Hermes Agent CLI 汉化安装脚本
自动将 Hermes 启动界面翻译为简体中文
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

def get_hermes_home():
    """获取 Hermes 源码目录"""
    home = Path.home()
    hermes_dir = home / ".hermes" / "hermes-agent"
    if not hermes_dir.exists():
        print(f"错误: 找不到 Hermes 安装目录: {hermes_dir}")
        print("请先安装 Hermes Agent: https://github.com/NousResearch/hermes-agent")
        sys.exit(1)
    return hermes_dir

def backup_file(filepath):
    """备份文件"""
    backup_path = filepath.with_suffix(filepath.suffix + f".bak.{datetime.now().strftime('%Y%m%d%H%M%S')}")
    shutil.copy2(filepath, backup_path)
    return backup_path

def apply_translation(content, old, new):
    """应用翻译，保留变量占位符"""
    import re
    # 将 {N} 等变量转为正则表达式
    pattern = re.escape(old).replace(r'\{N\}', r'(\d+)')
    replacement = new.replace('{N}', r'\1')
    return re.sub(pattern, replacement, content)

def install_translations():
    """安装汉化翻译"""
    hermes_dir = get_hermes_home()
    translations_file = Path(__file__).parent / "translations.json"
    tips_zh_file = Path(__file__).parent / "tips_zh.py"
    
    if not translations_file.exists():
        print(f"错误: 找不到翻译文件: {translations_file}")
        sys.exit(1)
    
    with open(translations_file, 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    files_to_translate = {
        "cli.py": hermes_dir / "cli.py",
        "hermes_cli/banner.py": hermes_dir / "hermes_cli" / "banner.py",
    }
    
    print("正在应用汉化翻译...\n")
    
    # 处理 cli.py 和 banner.py
    for file_key, filepath in files_to_translate.items():
        if not filepath.exists():
            print(f"⚠ 跳过 {file_key}: 文件不存在")
            continue
        
        print(f"处理 {file_key}...")
        backup_path = backup_file(filepath)
        print(f"  已备份: {backup_path.name}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if file_key in translations:
            for old, new in translations[file_key].items():
                content = apply_translation(content, old, new)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ 已应用翻译\n")
    
    # 处理 tips.py（直接替换整个文件）
    tips_filepath = hermes_dir / "hermes_cli" / "tips.py"
    if tips_zh_file.exists() and tips_filepath.exists():
        print("处理 hermes_cli/tips.py...")
        backup_path = backup_file(tips_filepath)
        print(f"  已备份: {backup_path.name}")
        
        shutil.copy2(tips_zh_file, tips_filepath)
        print(f"  ✓ 已应用翻译\n")
    else:
        if not tips_zh_file.exists():
            print(f"⚠ 跳过 tips.py: 找不到翻译文件 {tips_zh_file}")
        if not tips_filepath.exists():
            print(f"⚠ 跳过 tips.py: 文件不存在 {tips_filepath}")
    
    print("=" * 50)
    print("汉化安装完成！")
    print("=" * 50)
    print("\n请重启 Hermes 使更改生效：")
    print("  hermes gateway restart")
    print("\n或在 CLI 中输入：")
    print("  /reset")

def main():
    """主函数"""
    print("=" * 50)
    print("Hermes Agent CLI 汉化安装程序")
    print("=" * 50)
    print()
    
    try:
        install_translations()
    except Exception as e:
        print(f"\n错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
