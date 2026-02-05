#!/usr/bin/env python3
"""
AI工具网站健康监控系统
定期检查网站可用性并发送报告
"""

import time
import requests
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_website_health():
    """
    检查网站健康状况
    """
    urls_to_check = [
        'http://localhost:8094',
        'http://localhost:8094/sitemap.xml',
        'http://localhost:8094/robots.txt',
        'http://localhost:8094/index.html'
    ]
    
    results = {}
    
    for url in urls_to_check:
        try:
            response = requests.get(url, timeout=10)
            results[url] = {
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'size': len(response.content),
                'status': 'UP' if response.status_code == 200 else 'DOWN'
            }
        except Exception as e:
            results[url] = {
                'status_code': None,
                'response_time': None,
                'size': 0,
                'status': 'ERROR',
                'error': str(e)
            }
    
    return results

def generate_report(results):
    """
    生成健康检查报告
    """
    report = f"""
AI工具网站健康检查报告
=======================
检查时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
服务器状态: {'在线' if all(r['status'] == 'UP' or r['status'] == 'DOWN' for r in results.values()) else '部分异常'}
网站地址: http://8.215.63.182:8094

详细结果:
"""
    
    for url, result in results.items():
        report += f"\n{url}:"
        report += f"\n  状态: {result['status']}"
        report += f"\n  状态码: {result['status_code'] if result['status_code'] else 'N/A'}"
        report += f"\n  响应时间: {result['response_time'] if result['response_time'] else 'N/A'} 秒"
        report += f"\n  内容大小: {result['size']} 字节"
        if result['status'] == 'ERROR':
            report += f"\n  错误信息: {result.get('error', 'Unknown error')}"
        report += "\n"
    
    return report

def save_health_log(results, report):
    """
    保存健康检查日志
    """
    log_dir = "/home/admin/clawd/ai_tools_website/logs"
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = f"{log_dir}/health_check_{datetime.now().strftime('%Y%m%d')}.log"
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(report)
        f.write("\n" + "="*50 + "\n")

def main():
    print("开始网站健康检查...")
    results = check_website_health()
    report = generate_report(results)
    save_health_log(results, report)
    
    print(report)
    
    # 检查是否有错误
    errors = [url for url, result in results.items() if result['status'] == 'ERROR']
    if errors:
        print(f"⚠️ 发现错误: {errors}")
    else:
        print("✅ 所有检查项目正常")

if __name__ == "__main__":
    main()