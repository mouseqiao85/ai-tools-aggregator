# AI Tools Website 项目组织计划

## 生产环境文件 (保留)
- `server_with_pocketbase.py` - 主服务器文件
- `index.html` - 主页文件
- `health_check.py` - 健康检查脚本
- `restart_service.sh` - 重启服务脚本
- `README.md` - 项目说明
- `FIXED_ISSUES.md` - 修复问题记录

## 静态资源 (保留)
- `css/` - 样式文件
- `js/` - JavaScript文件
- `images/` - 图片资源
- `rss/` - RSS订阅文件
- `pb_data/` - PocketBase数据库文件

## 文档文件 (保留)
- `POCKETBASE_VERSION_README.md` - PocketBase版本说明
- `monetization_strategy.md` - 商业化策略

## 中间/测试文件 (可删除)
- 各种测试服务器文件 (test_api_directly.py, simple_server.py, etc.)
- 调试日志文件
- 临时输出文件

## 构建目标
创建一个干净的项目结构，只保留必要的生产文件。