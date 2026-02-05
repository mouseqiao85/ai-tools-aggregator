# AI工具聚合网站 v1.0

## 项目概述

这是一个功能完整的AI工具聚合网站，具有以下特性：

- **赛博朋克视觉风格** - 独特的霓虹配色和现代UI设计
- **多语言支持** - 支持中文、英文、日文、韩文等语言
- **PocketBase集成** - 与数据库后端完全集成
- **评分排序** - 默认按评分从高到低排序
- **响应式设计** - 适配各种屏幕尺寸
- **SEO优化** - 完整的元数据和结构化数据支持
- **社交分享** - 集成多种社交平台分享功能

## 特性

### 视觉设计
- 赛博朋克风格UI，使用霓虹配色方案
- 毛玻璃效果和渐变背景
- 流畅的动画和过渡效果
- 响应式布局，支持移动设备

### 功能特性
- AI工具分类浏览（文本生成、图像生成、编程助手等）
- 按评分、名称、类别排序
- 搜索功能
- 多语言切换
- 工具评分系统
- 社交分享功能

### 技术栈
- **前端**: HTML5, CSS3, JavaScript
- **后端**: Python HTTP服务器
- **数据库**: PocketBase
- **部署**: Nginx反向代理

## 安装和运行

### 环境要求
- Python 3.6+
- PocketBase

### 安装步骤

1. 克隆或下载项目
2. 安装PocketBase（如果未安装）
3. 启动PocketBase服务
4. 运行Python服务器

### 启动命令

```bash
# 启动PocketBase（在后台运行）
python3 start_pocketbase_public.py

# 启动网站服务器
python3 server_with_pocketbase.py
```

## 项目结构

```
ai-tools-website-v1.0/
├── server_with_pocketbase.py     # 主服务器文件
├── start_pocketbase_public.py    # 启动PocketBase的脚本
├── README.md                     # 项目说明
└── pb_data/                      # PocketBase数据目录（首次运行时创建）
```

## 数据库配置

项目使用PocketBase作为数据库后端，需要：

1. 下载并安装PocketBase
2. 在项目根目录创建pb_data目录
3. 确保服务器能访问 http://localhost:8090

## API端点

- `GET /api/tools` - 获取所有AI工具
- `GET /api/tools/{id}` - 获取特定工具
- `GET /sitemap.xml` - 站点地图
- `GET /robots.txt` - robots.txt文件

## 自定义

您可以轻松地：

- 修改CSS变量来自定义颜色方案
- 添加新的AI工具到数据库
- 添加更多语言支持
- 扩展功能模块

## 许可证

此项目仅供学习和参考使用。