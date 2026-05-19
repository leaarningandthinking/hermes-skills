#!/usr/bin/env python3
"""紧急撤退模式 - 一键切换到工作状态"""

import random
from datetime import datetime, timedelta

URGENT_TITLES = [
    "【紧急】线上故障处理",
    "【P0】客户问题跟进",
    "【加急】需求变更评审",
    "【重要】项目进度同步",
    "【会议】跨部门协调会",
    "【汇报】月度数据复盘",
    "【紧急】系统性能优化",
    "【告警】服务器监控通知",
]

WORK_MESSAGES = [
    "刚处理完一个线上问题，稍等回复你",
    "在和老板开会讨论方案，先忙一下",
    "有个紧急需求要处理，待会找你",
    "正在对齐多个项目进度，晚点聊",
    "刚接了个加急任务，忙完再说",
]

BUSY_PHRASES = [
    "正在深度思考业务逻辑",
    "正在绘制系统架构图",
    "正在编写技术方案",
    "正在梳理产品需求",
    "正在调优核心算法",
    "正在搭建测试环境",
    "正在同步多方资源",
    "正在跟进客户反馈",
]

def generate_fake_email():
    """生成看起来很重要的邮件标题和内容"""
    title = random.choice(URGENT_TITLES)
    
    templates = [
        f"""主题：{title}

各位好：

关于今天的{random.choice(['故障', '需求变更', '性能问题'])}，我这边已经：
1. 定位了问题根因
2. 制定了初步方案
3. 联系了相关同事

预计{random.randint(30, 120)}分钟内可以完成修复/部署。

有任何问题随时找我。

BR,
你的名字""",
        f"""主题：{title}

紧急上线窗口：{datetime.now().strftime('%H:%M')}

- 修复内容：优化{random.choice(['数据库查询', '缓存策略', '响应速度'])}
- 影响范围：{random.choice(['部分用户', '全量用户', '核心功能'])}
- 操作人：你的名字
- 预计耗时：{random.randint(10, 60)}min

请周知，收到回复。
"""
    ]
    return random.choice(templates)

def generate_slack_message():
    """生成即时通讯里的工作消息"""
    return random.choice(WORK_MESSAGES)

def generate_busy_status():
    """生成"忙"的状态描述"""
    return random.choice(BUSY_PHRASES)

def generate_meeting_excuse():
    """生成开会借口"""
    meeting_types = ['需求评审', '技术方案讨论', '项目进度同步', '客户沟通会']
    return f"抱歉，我现在在「{random.choice(meeting_types)}」中，{random.randint(10, 60)}分钟后再聊"

def generate_task_list():
    """生成本周/今日任务列表"""
    tasks = [
        "[ ] 完成需求文档",
        "[ ] 同步客户进度",
        "[ ] 修复线上bug",
        "[ ] 准备周会汇报",
        "[ ] 配置测试环境",
    ]
    random.shuffle(tasks)
    top_tasks = tasks[:3]
    
    result = f"""今日任务清单
{'='*30}
"""
    for task in top_tasks:
        # 随机标记一个为完成
        if random.random() < 0.3:
            task = task.replace('[ ]', '[✓]')
        result += task + '\n'
    
    result += f"\n完成度: {random.randint(30, 80)}%"
    return result

def generate_panic_screen():
    """生成完整的"紧急工作模式"界面"""
    now = datetime.now()
    
    result = f"""
╔════════════════════════════════════════╗
║     🚨 紧急工作模式已启动 🚨            ║
╠════════════════════════════════════════╣
  当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}
  
  📧 发送给客户:
  {generate_slack_message()}
  
  📋 当前状态:
  {generate_busy_status()}
  
  🚪 临时应对:
  {generate_meeting_excuse()}
╚════════════════════════════════════════╝

{generate_task_list()}
"""
    return result

def main():
    print(generate_panic_screen())

if __name__ == '__main__':
    main()
