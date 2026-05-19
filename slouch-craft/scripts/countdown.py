#!/usr/bin/env python3
"""下班倒计时 - 摸鱼人的必备工具"""

from datetime import datetime, timedelta
import sys

def countdown(off_hour=18, off_minute=0):
    """计算距离下班的时间"""
    now = datetime.now()
    off_time = now.replace(hour=off_hour, minute=off_minute, second=0, microsecond=0)
    
    # 如果已经过了下班时间，算到明天
    if off_time < now:
        off_time += timedelta(days=1)
    
    remaining = off_time - now
    total_seconds = int(remaining.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    # 计算摸鱼进度
    work_start = now.replace(hour=9, minute=0, second=0)  # 假设9点上班
    if work_start > now:
        work_start = now.replace(hour=9, minute=0) - timedelta(days=1)
    
    work_day_hours = off_hour - 9  # 下班时间 - 上班时间
    work_day_seconds = work_day_hours * 3600
    elapsed = now - work_start
    progress = min(100, (elapsed.total_seconds() / work_day_seconds) * 100)
    
    # 根据进度给出评价
    if progress < 30:
        status = "⌛ 早起摸鱼人，加油！"
        emoji = "☕"
    elif progress < 50:
        status = "📈 上午摸鱼很顺利，下午继续！"
        emoji = "🐟"
    elif progress < 75:
        status = "⏳ 熬过下午3点就是胜利！"
        emoji = "🕒"
    elif progress < 90:
        status = "💪 胜利就在眼前！坚持住！"
        emoji = "🚀"
    else:
        status = "🏃 快跑！马上自由了！"
        emoji = "✨"
    
    # 生成艺术化倒计时
    result = f"""
╔══════════════════════════════════════════╗
║           🎣 下班倒计时 🎣               ║
╠══════════════════════════════════════════╣

   {emoji} 距离 {off_hour}:{off_minute:02d} 还有：
   
            {hours:>2} 小时
            {minutes:>2} 分钟  
            {seconds:>2} 秒

   ╔{'='*int(progress/5)}{'░'*(20-int(progress/5))}╗ {progress:.1f}%
   
   状态：{status}

"""
    
    # 加一些摸鱼小贴士
    if hours < 1:
        result += "   💡 小贴士：开始整理桌面，准备冲刺！\n"
    elif hours < 2:
        result += "   💡 小贴士：去喝杯咖啡，眺望远方\n"
    elif hours < 4:
        result += "   💡 小贴士：午餐后正是摸鱼好时光\n"
    else:
        result += "   💡 小贴士：刚刚上班，先熟悉一下今天的任务\n"
    
    result += "\n╚══════════════════════════════════════════╝"
    
    return result

def weekend_countdown():
    """倒计时到周末"""
    now = datetime.now()
    days_to_friday = 4 - now.weekday()  # 周五是4
    if days_to_friday < 0 or (days_to_friday == 0 and now.hour >= 18):
        return "🎉 周末啦！尽情享受自由时光！"
    
    friday_6pm = now + timedelta(days=days_to_friday)
    friday_6pm = friday_6pm.replace(hour=18, minute=0, second=0)
    remaining = friday_6pm - now
    total_days = remaining.days
    total_hours = int(remaining.total_seconds() // 3600)
    
    messages = [
        "再坚持一下，周末就在眼前！",
        "周末正在向你招手！",
        "熬过今天，胜利属于摸鱼人！",
        "想象周末的美好，今天就有动力了！"
    ]
    
    return f"""
🏖️ 周末倒计时

距离周五 18:00 还有：
⏰ {total_days} 天 {total_hours - total_days*24} 小时

{random.choice(messages) if 'random' in dir() else messages[0]}
"""

if __name__ == '__main__':
    # 支持自定义下班时间
    if len(sys.argv) > 2:
        off_hour = int(sys.argv[1])
        off_minute = int(sys.argv[2])
    elif len(sys.argv) > 1:
        off_hour = int(sys.argv[1])
        off_minute = 0
    else:
        off_hour, off_minute = 18, 0
    
    print(countdown(off_hour, off_minute))
    print("\n" + weekend_countdown())
