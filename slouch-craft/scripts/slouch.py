#!/usr/bin/env python3
"""slouch - 摸鱼大师主入口"""

import sys
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

def print_help():
    """打印帮助信息"""
    print("""
🎣 摸鱼大师 Slouch-Craft - 职场摸鱼神器

用法: slouch <命令> [选项]

命令:
    fake-code [语言]     生成伪装代码 (python/js)
    terminal [类型]      启动伪终端 (upgrade/deploy/analytics/api)
    funny                生成趣味内容(颜文字、段子、运势)
    panic                紧急撤退模式
    countdown [小时] [分] 下班倒计时
    help                 显示帮助

示例:
    slouch fake-code python    # 生成 Python 伪装代码
    slouch terminal deploy      # 假装部署
    slouch funny              # 摸鱼雷达
    slouch panic              # 一键工作模式
    slouch countdown          # 默认18:00下班
    slouch countdown 17 30    # 17:30下班
""")

def main():
    if len(sys.argv) < 2:
        print_help()
        return
    
    command = sys.argv[1]
    args = sys.argv[2:]
    
    scripts = {
        'fake-code': 'fake_code.py',
        'code': 'fake_code.py',
        'terminal': 'fake_terminal.py',
        'term': 'fake_terminal.py',
        'funny': 'funny_generator.py',
        'f': 'funny_generator.py',
        'panic': 'panic_mode.py',
        'p': 'panic_mode.py',
        'countdown': 'countdown.py',
        'cd': 'countdown.py',
        'clock': 'countdown.py',
    }
    
    if command == 'help' or command == '-h' or command == '--help':
        print_help()
        return
    
    script = scripts.get(command)
    if script:
        script_path = SCRIPT_DIR / script
        cmd = [sys.executable, str(script_path)] + args
        subprocess.run(cmd)
    else:
        print(f"未知命令: {command}")
        print("使用 'slouch help' 查看帮助")

if __name__ == '__main__':
    main()
