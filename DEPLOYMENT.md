# 部署和配置指南

## 系统要求

- Linux服务器 (推荐Ubuntu 20.04+ 或 CentOS 8+)
- Python 3.6+
- 至少512MB可用内存
- 至少1GB可用磁盘空间

## 安装依赖

### 1. 安装PocketBase

```bash
# 下载PocketBase (根据您的系统架构选择)
# 对于AMD64系统
wget https://github.com/pocketbase/pocketbase/releases/latest/download/pocketbase_0.22.13_linux_amd64.zip
unzip pocketbase_0.22.13_linux_amd64.zip

# 移动到项目目录
mv pocketbase /home/admin/clawd/pocketbase
chmod +x /home/admin/clawd/pocketbase
```

### 2. 安装Nginx (用于反向代理)

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nginx

# CentOS/RHEL
sudo yum install nginx
# 或者对于较新版本
sudo dnf install nginx
```

## 配置步骤

### 1. 数据库初始化

首次运行时，PocketBase会自动创建数据库文件。访问 `http://your-server-ip:8090/_/` 来设置管理员账户。

### 2. 启动服务

```bash
# 启动PocketBase
cd /home/admin/clawd
python3 start_pocketbase_public.py

# 在另一个终端启动网站服务器
cd /home/admin/clawd
python3 server_with_pocketbase.py
```

### 3. Nginx配置

创建Nginx配置文件：

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8094;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 环境变量配置

如果需要自定义端口或其他配置，可以修改 `server_with_pocketbase.py` 中的默认值：

- 默认网站端口: 8094
- 默认PocketBase端口: 8090
- 数据目录: ./pb_data

## 数据备份

定期备份PocketBase数据库文件：

```bash
# 备份数据
tar -czf pb_data_backup_$(date +%Y%m%d_%H%M%S).tar.gz pb_data/

# 恢复数据
tar -xzf pb_data_backup_YYYYMMDD_HHMMSS.tar.gz
```

## 监控和维护

### 服务状态检查

```bash
# 检查服务进程
ps aux | grep pocketbase
ps aux | grep server_with_pocketbase

# 检查端口占用
netstat -tlnp | grep :8090
netstat -tlnp | grep :8094
```

### 日志查看

```bash
# 查看服务器日志
tail -f server.log
tail -f pocketbase.log
```

## 域名配置

如果您有自己的域名，请进行以下配置：

1. 将域名指向服务器IP地址
2. 在Nginx配置中替换 `your-domain.com` 为您的实际域名
3. (可选) 配置SSL证书以启用HTTPS

## SSL证书配置

使用Let's Encrypt配置SSL：

```bash
# 安装certbot
sudo apt install certbot python3-certbot-nginx

# 获取SSL证书
sudo certbot --nginx -d your-domain.com
```

## 故障排除

### 常见问题

1. **无法访问管理面板**
   - 检查PocketBase是否正常运行
   - 确认端口8090是否开放

2. **工具数据不显示**
   - 检查服务器是否能连接到PocketBase
   - 确认数据库中有数据

3. **样式不正确**
   - 检查浏览器缓存
   - 确认CSS/JS文件是否正确加载