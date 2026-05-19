#!/usr/bin/env python3
"""趣味内容生成器 - 生成摸鱼时的轻松内容"""

import random

KAOMOJI = [
    "(つ✧ω✧)つ", "(￣︶￣)", "(｡･ω･｡)ﾉ♡",
    "(｀・ω・´)", "(๑•̀ㅂ•́)و✧", "(｡ŏ﹏ŏ)",
    "( ◡‿◡ )", "( ͡° ͜ʖ ͡°)", "(╯°□°)╯︵ ┻━┻",
    "¯\\_(ツ)_/¯", "(⌐■_■)", "(ﾉಥ益ಥ)ﾉ",
    "(づ｡◕‿‿◕｡)づ", "(ノ°▽°)ノ", "(¬‿¬)",
    "(⚆_⚆)", "╰(*°▽°*)╯", "( ಠ ͜ʖ ಠ )"
]

JOKES = [
    "为什么程序员喜欢摸鱼？\n因为 'console.log(fish)' 不需要编译",
    "老板问我为什么上班打哈欠\n我说我在进行深呼吸优化",
    "写代码和摸鱼的区别:\n一个需要思考，一个需要假装思考",
    "上班就是一场马拉松\n偶尔摸鱼是为了更好地冲刺...到下班",
    "为什么工位的椅子那么舒服？\n那是老板留给我们摸鱼的诱饵",
    "我的工作效率如何？\n就像Ctrl+C和Ctrl+V，看着很快，其实都在重复",
    "开会的时候我在做什么？\n把嗯嗯啊啊练成了顺嘴的本能反应",
    "配置环境两小时，写代码两分钟\n程序员的一天就这么过去了",
    "世界上最远的距离\n是'按下运行'到'看到结果'之间的那条加载条",
    "咖啡☕是程序员的续命水\n摸鱼🐟是程序员的灵魂养料",
]

FORTUNES = {
    '大吉': '今天的你简直是天选打工人，摸鱼都能摸出一等奖！',
    '吉': '工作顺利，今天适合假装很忙然后提前下班',
    '中吉': '普通的一天，但摸鱼的快乐不普通',
    '小吉': '小心驶得万年船，摸鱼要低调',
    '末吉': '今天可能要加班了（但摸鱼还是要摸的）',
    '凶': '老板今天心情不太好，建议认真工作',
}

EXCUSES = [
    "我在等这个编译完成...",
    "刚在和客户对齐需求...",
    "数据正在同步中...",
    "刚刚在解决一个线上问题...",
    "正在调试一个棘手的bug...",
    "刚开完一个重要会议...",
]

def get_kaomoji():
    """随机颜文字"""
    return random.choice(KAOMOJI)

def get_joke():
    """随机段子"""
    return random.choice(JOKES)

def get_fortune():
    """今日运势"""
    level = random.choices(
        list(FORTUNES.keys()),
        weights=[5, 15, 30, 30, 15, 5],
        k=1
    )[0]
    return f"【{level}】{FORTUNES[level]}"

def get_excuse():
    """摸鱼借口"""
    return random.choice(EXCUSES)

def get_timewaster():
    """推荐一个摸鱼网站"""
    sites = [
        "aidn.jp/mikutap/ - 音乐游戏，超解压",
        "theuselessweb.com - 随机无用网站",
        "paper-io.com - 贪吃蛇风格游戏",
        "slither.io - 蛇蛇大作战",
        "neal.fun - 各种有趣小实验",
        "pointerpointer.com - 找到你的鼠标",
    ]
    return random.choice(sites)

def main():
    """主函数"""
    print("=== 摸鱼雷达 🎣 ===\n")
    print(f"今日颜文字: {get_kaomoji()}")
    print(f"\n今日运势: {get_fortune()}")
    print(f"\n摸鱼段子:\n{get_joke()}")
    print(f"\n摸鱼借口储备: {get_excuse()}")
    print(f"\n今日推荐: {get_timewaster()}")

if __name__ == '__main__':
    main()
