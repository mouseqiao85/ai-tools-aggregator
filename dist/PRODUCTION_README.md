# AI工具聚合网站 - 生产版本

这是一个功能丰富的AI工具聚合网站，专为海外推广而设计，支持多语言和全面的SEO优化。

## 项目概述

AI工具聚合网站是一个现代化的AI工具导航平台，集成了全球领先的AI工具、GitHub热门项目和ClawdHub技能，为用户提供一站式AI解决方案。

## 核心功能

### 国际化支持
- 支持中文、英文、日文、韩文四种语言
- 动态语言切换功能
- 本地化内容展示

### SEO优化
- 完整的元数据配置
- 结构化数据标记
- 多语言sitemap
- 社交媒体分享优化

### 工具分类
- 文本生成工具（ChatGPT, Claude, Gemini等）
- 图像生成工具（Midjourney, DALL-E 3, Stable Diffusion等）
- 编程助手（GitHub Copilot, Tabnine等）
- 内容创作工具
- 个人AI助理
- GitHub热门项目
- ClawdHub技能

## 技术架构

- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **后端**: Python HTTP Server
- **数据库**: PocketBase
- **API**: RESTful接口
- **部署**: Linux服务器

## 部署说明

### 环境要求
- Python 3.6+
- PocketBase 0.22.0+
- Linux/Unix服务器

### 部署步骤
1. 安装依赖
2. 启动PocketBase服务
3. 启动网站服务器
4. 配置反向代理（可选）
5. 设置SSL证书（可选）

### 启动服务
```bash
# 启动PocketBase数据库
./pocketbase serve --http=0.0.0.0:8090 &

# 启动网站服务
python3 server_with_pocketbase.py &
```

### 访问地址
- 默认端口: 8094
- API端点: `/api/tools`
- 健康检查: `/api/health`

## 项目结构

```
dist/
├── server_with_pocketbase.py    # 主服务器文件
├── index.html                   # 主页
├── health_check.py              # 健康检查脚本
├── restart_service.sh           # 重启脚本
├── css/                         # 样式文件
├── js/                          # JavaScript文件
├── images/                      # 图片资源
├── rss/                         # RSS订阅文件
├── logs/                        # 日志目录
├── README.md                    # 项目说明
└── FIXED_ISSUES.md              # 修复记录
```

## 维护说明

### 日常维护
- 监控服务器运行状态
- 检查API可用性
- 更新工具数据
- 查看访问日志

### 数据管理
- 工具数据存储在PocketBase数据库中
- 可通过管理面板添加/编辑工具
- 支持批量导入导出功能

## 版本信息

- **最后更新**: 2026年2月5日
- **版本**: v1.0.0
- **作者**: ClawDBot Team

## 许可证

此项目仅供学习和参考使用。