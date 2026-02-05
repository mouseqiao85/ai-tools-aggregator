# AI工具聚合网站

这是一个功能丰富的AI工具聚合网站，专为海外推广而设计，支持多语言和全面的SEO优化，特别集成了ClawDBot个人AI助理系统、GitHub热门项目和ClawdHub技能的推荐。

## 功能特性

### 国际化功能
- 支持中文、英文、日文、韩文四种语言
- 动态语言切换器
- 本地化存储用户语言偏好
- 文化适应性界面设计

### SEO优化
- 完整的元数据（标题、描述、关键词）
- 结构化数据标记（Schema.org JSON-LD）
- 多语言sitemap（en、zh、ja、ko）
- Open Graph和Twitter Card协议
- hreflang国际化链接标签
- RSS订阅功能

### 用户体验
- 响应式设计，适配各种设备
- 搜索和筛选功能
- 社交分享按钮（Twitter、Facebook、LinkedIn、Reddit）
- 详细的工具信息展示

### 集成服务
- ClawDBot推荐横幅和介绍
- GitHub Star Top 10板块
- ClawdHub技能Top 10板块
- 个人AI助理类别
- 专门的ClawDBot介绍页面
- 多语言描述

### 工具覆盖范围
- **文本生成**: ChatGPT, Claude, Gemini, ChatGPT Edu, Microsoft Copilot, HuggingChat
- **图像生成**: Midjourney, DALL-E 3, Stable Diffusion, Adobe Firefly, Leonardo AI
- **音频工具**: ElevenLabs, Descript
- **视频工具**: Runway ML, Synthesia
- **编程助手**: GitHub Copilot, Amazon CodeWhisperer, Tabnine
- **内容创作**: Jasper, Notion AI, Writesonic
- **商业工具**: Salesforce Einstein, IBM Watson
- **创意工具**: Adobe Sensei, Canva AI
- **搜索工具**: Perplexity AI, You.com
- **开源项目**: GitHub热门AI项目
- **技能扩展**: ClawdHub热门技能

### 技术特性
- 现代化CSS设计（渐变、毛玻璃效果、动画）
- JavaScript交互功能（搜索、筛选、排序）
- 健康监控系统
- 自动化部署

## 技术架构

- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **服务器**: Python HTTP Server
- **端口**: 8094
- **部署**: 直接文件服务

## 部署说明

1. 确保端口8094在服务器防火墙中开放
2. 启动服务器: `python basic_server.py`
3. 访问地址: `http://[SERVER_IP]:8094`

## 监控

网站健康状态会每30分钟自动检查一次，确保持续稳定运行。

## 域名

- 测试地址: http://8.215.63.182:8094
- 正式域名: https://chuansha.tech (待启用)

## 文件结构

```
ai_tools_website/
├── index.html          # 主页面
├── clawdbot.html       # ClawDBot专门介绍页面
├── css/                # 样式文件
│   └── international-style.css
├── js/                 # JavaScript文件
│   └── international-script.js
├── images/             # 图片资源
├── logs/               # 日志文件
├── basic_server.py     # Python服务器
├── health_monitor.py   # 健康监控脚本
├── sitemap.xml         # 网站地图
├── sitemap-*.xml       # 多语言网站地图
├── robots.txt          # 搜索引擎爬虫配置
├── README.md           # 项目说明
├── monetization_strategy.md  # 变现策略文档
├── github_clawdhub_integration.py  # GitHub和ClawdHub集成脚本
└── add_more_ai_tools.py  # 添加更多AI工具脚本
```

## 维护

- 定期检查服务器运行状态
- 监控访问日志
- 更新工具列表
- 优化SEO设置
- 保持多语言内容同步
- 更新ClawDBot、GitHub和ClawdHub相关信息

## 开发

如需添加新功能或修改现有功能，请遵循以下原则：

- 保持多语言兼容性
- 确保SEO友好
- 维护响应式设计
- 优化页面加载速度
- 遵循无障碍标准

## 许可证

此项目仅供学习和参考使用。

## 更新日志

### 2026年2月4日
- **GitHub Top 10和ClawdHub技能Top 10导入完成**
  - 成功将10个GitHub热门AI项目导入PocketBase数据库
  - 成功将10个ClawdHub技能导入PocketBase数据库
  - 网站现在总共包含54个精选项目：
    - 34个AI工具（包括原有的AI工具）
    - 10个GitHub热门项目
    - 10个ClawdHub技能
  - 前端已更新显示新的分类和统计数据
  - 完整的多语言支持已扩展至新添加的项目