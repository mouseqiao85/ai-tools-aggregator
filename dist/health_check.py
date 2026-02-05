#!/usr/bin/env python3
"""
AI工具网站健康检查脚本
检查所有AI工具网站的状态
"""

import requests
import sys
from datetime import datetime

def check_website_health():
    """检查所有AI工具网站的健康状况"""
    websites = [
        {"name": "AI工具大全", "url": "http://localhost:8091", "port": 8091},
        {"name": "AI设计师工具", "url": "http://localhost:8092", "port": 8092},
        {"name": "AI程序员助手", "url": "http://localhost:8093", "port": 8093},
        {"name": "AI写作神器", "url": "http://localhost:8094", "port": 8094},
        {"name": "AI教育工具", "url": "http://localhost:8095", "port": 8095}
    ]
    
    results = []
    
    print(f"开始检查AI工具网站健康状况 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    for site in websites:
        try:
            response = requests.get(site['url'], timeout=10)
            status = "正常" if response.status_code == 200 else "异常"
            results.append({
                "name": site['name'],
                "port": site['port'],
                "status_code": response.status_code,
                "status": status
            })
            
            print(f"{site['name']} ({site['port']}) - HTTP {response.status_code} - {status}")
            
        except requests.exceptions.RequestException as e:
            results.append({
                "name": site['name'],
                "port": site['port'],
                "status_code": None,
                "status": "连接失败"
            })
            print(f"{site['name']} ({site['port']}) - 连接失败 - {str(e)}")
    
    print("="*60)
    
    # 统计结果
    total_sites = len(results)
    healthy_sites = sum(1 for r in results if r['status'] == '正常')
    
    print(f"总计: {total_sites}, 正常: {healthy_sites}, 异常: {total_sites - healthy_sites}")
    
    if healthy_sites == total_sites:
        print("✅ 所有AI工具网站运行正常")
        return True
    else:
        print("❌ 部分AI工具网站存在问题")
        return False

if __name__ == "__main__":
    success = check_website_health()
    sys.exit(0 if success else 1)