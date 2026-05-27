#!/usr/bin/env python3
"""
Hermes Agent CLI 智能汉化脚本
根据当前版本的代码自动汉化，不会破坏代码结构
"""

import os
import sys
import shutil
import re
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

def safe_replace(content, old, new, filename=""):
    """安全替换字符串，保留上下文"""
    if old not in content:
        return content, False
    # 只替换字符串内容，不改变代码结构
    new_content = content.replace(old, new)
    return new_content, True

def translate_banner_py(filepath):
    """翻译 banner.py"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 翻译映射表
    translations = [
        # 版本标签
        ('Hermes Agent v{VERSION}', 'Hermes 智能代理 v{VERSION}'),
        
        # 启动界面
        ('Available Tools', '可用工具'),
        ('MCP Servers', 'MCP 服务器'),
        ('Available Skills', '可用技能'),
        
        # 会话信息
        ('Session: {session_id}', '会话: {session_id}'),
        
        # YOLO 模式
        ('YOLO mode', 'YOLO 模式'),
        ('— all approval prompts bypassed', '— 已跳过所有审批提示'),
        
        # 工具/技能统计
        ('{len(tools)} tools', '{len(tools)} 个工具'),
        ('{total_skills} skills', '{total_skills} 个技能'),
        ('{mcp_connected} MCP servers', '{mcp_connected} 个 MCP 服务器'),
        ('/help for commands', '/help 查看命令'),
        
        # MCP 服务器状态
        ('{srv[\'tools\']} tool(s)', '{srv[\'tools\']} 个工具'),
        ('— failed', '— 连接失败'),
        
        # 工具集
        ('(and {remaining_toolsets} more toolsets...)', '(还有 {remaining_toolsets} 个工具集...)'),
        
        # 技能显示
        ('+{len(skill_names) - 8} more', '+{len(skill_names) - 8} 更多'),
        ('No skills installed', '未安装技能'),
        
        # 运行时
        ('Runtime:', '运行时:'),
        ('terminal/file ops/MCP run inside codex', '终端/文件操作/MCP 在 codex 内运行'),
    ]
    
    changed = 0
    for old, new in translations:
        content, success = safe_replace(content, old, new, "banner.py")
        if success:
            changed += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return changed

def translate_cli_py(filepath):
    """翻译 cli.py"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 翻译映射表
    translations = [
        # 框架名称
        ('⚕ NOUS HERMES - AI Agent Framework', '⚕ NOUS HERMES - AI 智能代理框架'),
        ('{agent_name} - AI Agent Framework', '{agent_name} - AI 智能代理框架'),
        
        # 工具状态
        ('{tool_count} tools', '{tool_count} 个工具'),
        ('toolsets:', '工具集:'),
        
        # 欢迎语
        ('Welcome to Hermes Agent! Type your message or /help for commands.', '欢迎使用 Hermes 智能代理！输入消息或 /help 查看命令。'),
        
        # 退出语
        ('Goodbye! ⚕', '再见! ⚕'),
        
        # 会话恢复
        ('Resume this session with:', '使用以下命令恢复此会话:'),
        
        # 会话信息标签
        ('Session:', '会话:'),
        ('Title:', '标题:'),
        ('Duration:', '持续时间:'),
        ('Messages:', '消息数量:'),
        
        # 工具显示
        ('(^_^)/ Available Tools', '(^_^)/ 可用工具'),
        ('(;_;) No tools available', '(;_;) 没有可用工具'),
        ('(^_^)b Available Toolsets', '(^_^)b 可用工具集'),
        
        # 命令提示
        ('Type /help for available commands', '输入 /help 查看可用命令'),
        ('Unknown command:', '未知命令:'),
        ('Ambiguous command:', '模糊命令:'),
        ('Did you mean:', '你是想输入:'),
    ]
    
    changed = 0
    for old, new in translations:
        content, success = safe_replace(content, old, new, "cli.py")
        if success:
            changed += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return changed

def translate_tips_py(filepath):
    """翻译 tips.py（使用翻译后的完整文件）"""
    # 检查是否有翻译后的 tips_zh.py
    tips_zh_path = Path(__file__).parent / "tips_zh.py"
    if not tips_zh_path.exists():
        print(f"  ⚠ 找不到 tips_zh.py，跳过 tips.py 翻译")
        return 0
    
    # 读取翻译后的文件
    with open(tips_zh_path, 'r', encoding='utf-8') as f:
        zh_content = f.read()
    
    # 读取原始文件，只替换 TIPS 列表部分
    with open(filepath, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # 找到 TIPS 列表的开始和结束
    tips_start = original_content.find('TIPS = [')
    if tips_start == -1:
        print(f"  ⚠ 找不到 TIPS 列表，跳过")
        return 0
    
    # 找到对应的 ]
    bracket_count = 0
    tips_end = -1
    for i in range(tips_start, len(original_content)):
        if original_content[i] == '[':
            bracket_count += 1
        elif original_content[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                tips_end = i + 1
                break
    
    if tips_end == -1:
        print(f"  ⚠ 无法解析 TIPS 列表，跳过")
        return 0
    
    # 从翻译文件中提取 TIPS 列表
    zh_tips_start = zh_content.find('TIPS = [')
    if zh_tips_start == -1:
        print(f"  ⚠ 翻译文件中找不到 TIPS 列表，跳过")
        return 0
    
    zh_tips_end = -1
    bracket_count = 0
    for i in range(zh_tips_start, len(zh_content)):
        if zh_content[i] == '[':
            bracket_count += 1
        elif zh_content[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                zh_tips_end = i + 1
                break
    
    if zh_tips_end == -1:
        print(f"  ⚠ 无法解析翻译文件中的 TIPS 列表，跳过")
        return 0
    
    # 替换 TIPS 列表
    zh_tips = zh_content[zh_tips_start:zh_tips_end]
    new_content = original_content[:tips_start] + zh_tips + original_content[tips_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return 1

def main():
    """主函数"""
    print("=" * 50)
    print("Hermes Agent CLI 智能汉化程序")
    print("=" * 50)
    print()
    
    hermes_dir = get_hermes_home()
    
    files_to_translate = [
        ("hermes_cli/banner.py", translate_banner_py),
        ("cli.py", translate_cli_py),
        ("hermes_cli/tips.py", translate_tips_py),
    ]
    
    total_changes = 0
    
    for filename, translate_func in files_to_translate:
        filepath = hermes_dir / filename
        if not filepath.exists():
            print(f"⚠ 跳过 {filename}: 文件不存在")
            continue
        
        print(f"处理 {filename}...")
        backup_path = backup_file(filepath)
        print(f"  已备份: {backup_path.name}")
        
        try:
            changes = translate_func(filepath)
            total_changes += changes
            print(f"  ✓ 已应用翻译 ({changes} 处)\n")
        except Exception as e:
            print(f"  ✗ 翻译失败: {e}\n")
    
    print("=" * 50)
    print(f"汉化安装完成！共修改 {total_changes} 处")
    print("=" * 50)
    print("\n请重启 Hermes 使更改生效：")
    print("  hermes gateway restart")
    print("\n或在 CLI 中输入：")
    print("  /reset")

if __name__ == "__main__":
    main()
