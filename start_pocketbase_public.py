#!/usr/bin/env python3
"""
启动PocketBase服务，允许外部访问管理界面
"""

import subprocess
import os
import signal
import sys
import time

def start_pocketbase():
    # 确保数据目录存在
    data_dir = "/home/admin/clawd/pb_data"
    os.makedirs(data_dir, exist_ok=True)
    
    print("Starting PocketBase with public access...")
    print("PocketBase will be available at: http://8.215.63.182:8090/")
    print("Admin interface will be available at: http://8.215.63.182:8090/_/")
    
    # 启动PocketBase，绑定到所有网络接口
    cmd = [
        "/home/admin/clawd/pocketbase", 
        "serve", 
        f"--dir={data_dir}",
        "--http=0.0.0.0:8090"  # 绑定到所有接口，允许外部访问
    ]
    
    try:
        # 启动PocketBase进程
        process = subprocess.Popen(cmd)
        
        # 等待一段时间让服务启动
        time.sleep(3)
        
        print(f"PocketBase is now running with PID {process.pid}")
        print("Access the admin interface at: http://8.215.63.182:8090/_/")
        
        # 等待进程结束
        process.wait()
        
    except KeyboardInterrupt:
        print("\nShutting down PocketBase...")
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
        print("PocketBase stopped.")
    except Exception as e:
        print(f"Error starting PocketBase: {e}")

if __name__ == "__main__":
    start_pocketbase()