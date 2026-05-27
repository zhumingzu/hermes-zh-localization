#!/usr/bin/env python3
"""
Hermes Agent CLI 汉化卸载脚本
恢复 Hermes 启动界面为英文
"""

import os
import sys
import shutil
from pathlib import Path
from datetime import datetime

def get_hermes_home():
    """获取 Hermes 源码目录"""
    home = Path.home()
    hermes_dir = home / ".hermes" / "hermes-agent"
    if not hermes_dir.exists():
        print(f"错误: 找不到 Hermes 安装目录: {hermes_dir}")
        sys.exit(1)
    return hermes_dir

def backup_file(filepath):
    """备份文件"""
    backup_path = filepath.with_suffix(filepath.suffix + f".bak.{datetime.now().strftime('%Y%m%d%H%M%S')}")
    shutil.copy2(filepath, backup_path)
    return backup_path

def uninstall_translations():
    """卸载汉化翻译"""
    hermes_dir = get_hermes_home()
    
    files_to_restore = [
        hermes_dir / "cli.py",
        hermes_dir / "hermes_cli" / "banner.py",
        hermes_dir / "hermes_cli" / "tips.py"
    ]
    
    print("正在恢复英文界面...\n")
    
    for filepath in files_to_restore:
        if not filepath.exists():
            print(f"⚠ 跳过 {filepath.name}: 文件不存在")
            continue
        
        print(f"处理 {filepath.name}...")
        backup_path = backup_file(filepath)
        print(f"  已备份: {backup_path.name}")
        
        # 使用 git checkout 恢复原始文件
        try:
            import subprocess
            result = subprocess.run(
                ["git", "checkout", filepath.name],
                cwd=hermes_dir,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"  ✓ 已恢复为英文\n")
            else:
                print(f"  ⚠ 恢复失败: {result.stderr}\n")
        except Exception as e:
            print(f"  ⚠ 恢复失败: {e}\n")
    
    print("=" * 50)
    print("汉化已卸载！")
    print("=" * 50)
    print("\n请重启 Hermes 使更改生效：")
    print("  hermes gateway restart")
    print("\n或在 CLI 中输入：")
    print("  /reset")

def main():
    """主函数"""
    print("=" * 50)
    print("Hermes Agent CLI 汉化卸载程序")
    print("=" * 50)
    print()
    
    try:
        uninstall_translations()
    except Exception as e:
        print(f"\n错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
