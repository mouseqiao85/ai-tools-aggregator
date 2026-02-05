#!/bin/bash

# AI Tools Website 部署脚本

echo "开始部署 AI Tools Website..."

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误: Python3 未安装"
    exit 1
fi

# 检查PocketBase是否可用
if [ ! -f "./pocketbase" ]; then
    echo "警告: PocketBase 未找到，请先下载并放置在当前目录"
    echo "请从 https://github.com/pocketbase/pocketbase/releases 下载对应系统的版本"
fi

# 启动PocketBase服务
echo "启动PocketBase数据库服务..."
./pocketbase serve --http=0.0.0.0:8090 > pb_logs.log 2>&1 &

# 等待PocketBase启动
sleep 5

# 启动网站服务
echo "启动网站服务..."
python3 server_with_pocketbase.py > server_logs.log 2>&1 &

echo "部署完成!"
echo "网站服务运行在端口 8094"
echo "数据库服务运行在端口 8090"
echo ""
echo "访问地址: http://localhost:8094"
echo "数据库管理: http://localhost:8090/_/"