#!/bin/bash
# AI工具网站服务管理脚本

# 停止现有服务
pids=$(ps aux | grep "completely_fixed_server.py" | grep -v grep | awk '{print $2}')
if [ ! -z "$pids" ]; then
    echo "停止现有的AI工具网站服务..."
    kill -9 $pids
fi

# 等待确保端口释放
sleep 2

# 启动服务
echo "启动AI工具网站服务..."
cd /home/admin/clawd/ai_tools_website && python3 completely_fixed_server.py > server_start.log 2>&1 &

# 等待服务启动
sleep 5

# 检查服务是否成功启动
if lsof -Pi :8094 -sTCP:LISTEN -t >/dev/null; then
    echo "✅ AI工具网站服务已在端口8094上成功启动"
else
    echo "❌ 服务启动失败，请检查错误"
fi