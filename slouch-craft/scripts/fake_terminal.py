#!/usr/bin/env python3
"""伪终端生成器 - 模拟各种假装很忙的场景"""

import random
import time
import sys

TERMINAL_TYPES = {
    'upgrade': {
        'title': '正在升级系统组件...',
        'steps': [
            ('Downloading', 100, 'MB'),
            ('Extracting', 50, 'files'),
            ('Compiling', 120, 'packages'),
            ('Optimizing', 30, 's'),
            ('Cleaning up', 10, 'items'),
        ]
    },
    'deploy': {
        'title': '正在部署生产环境...',
        'steps': [
            ('Building', 50, '%'),
            ('Pushing to', 5, 'registries'),
            ('Rolling update', 3, 'pods'),
            ('Health check', 10, 'services'),
            ('Verifying', 100, '%'),
        ]
    },
    'analytics': {
        'title': '正在生成数据报告...',
        'steps': [
            ('Fetching', 10000, 'rows'),
            ('Processing', 85, '%'),
            ('Analyzing', 50, 'metrics'),
            ('Rendering', 20, 'charts'),
            ('Exporting', 5, 'formats'),
        ]
    },
    'api': {
        'title': '正在测试 API 性能...',
        'steps': [
            ('Sending requests', 1000, 'req/s'),
            ('Measuring latency', 50, 'ms'),
            ('Checking', 99.9, '% uptime'),
            ('Validating', 200, 'endpoints'),
            ('Generating report', 1, 'file'),
        ]
    }
}

def generate_bar(percent, width=30):
    """生成进度条"""
    filled = int(width * percent / 100)
    bar = '█' * filled + '░' * (width - filled)
    return bar

def fake_terminal(terminal_type='upgrade', simulate=True):
    """生成伪终端输出"""
    config = TERMINAL_TYPES.get(terminal_type, TERMINAL_TYPES['upgrade'])
    output = []
    
    # Header
    output.append(f"\n{'=' * 60}")
    output.append(f"  {config['title']}")
    output.append(f"{'=' * 60}\n")
    
    # 模拟步骤
    for i, (action, count, unit) in enumerate(config['steps']):
        progress = random.randint(30, 95)
        bar = generate_bar(progress)
        line = f"[{i+1}/{len(config['steps'])}] {action:20} {bar} {count} {unit}"
        output.append(line)
        if simulate:
            import time
            time.sleep(0.5)
            print(line, flush=True)
    
    # Footer
    output.append(f"\n{'=' * 60}")
    output.append("  ✓ 任务完成")
    output.append(f"{'=' * 60}\n")
    
    return '\n'.join(output)

def fake_logs(lines=20):
    """生成假的系统日志"""
    log_levels = ['INFO', 'DEBUG', 'WARN', 'SUCCESS']
    services = [
        'auth-service', 'user-api', 'payment-gateway',
        'analytics-engine', 'cache-layer', 'queue-worker'
    ]
    messages = [
        'Processing user request',
        'Cache hit ratio: 94.5%',
        'Database connection established',
        'Batch job completed',
        'Syncing data to S3',
        'Optimizing query cache',
        'Health check passed',
        'Metrics sent to Prometheus'
    ]
    
    output = []
    for i in range(lines):
        timestamp = f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d} "
        timestamp += f"{random.randint(9,18):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"
        level = random.choice(log_levels)
        service = random.choice(services)
        msg = random.choice(messages)
        output.append(f"[{timestamp}] [{level}] {service} | {msg}")
    
    return '\n'.join(output)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        terminal_type = sys.argv[1]
    else:
        terminal_type = 'upgrade'
    
    print(fake_terminal(terminal_type, simulate=False))
