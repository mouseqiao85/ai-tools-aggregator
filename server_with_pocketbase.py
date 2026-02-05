#!/usr/bin/env python3
"""
AI工具聚合网站服务器 - 与PocketBase集成
包含赛博朋克视觉风格和多语言支持
"""

import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import requests
import re


class AIToolsHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)
        
        # 处理API请求
        if path.startswith('/api/'):
            self.handle_api_request(path, query_params)
        # 处理静态资源
        elif path == '/' or path == '/index.html':
            self.serve_index_html()
        elif path.startswith('/css/') or path.startswith('/js/') or path.startswith('/images/') or path.startswith('/rss/'):
            self.serve_static_file(path)
        elif path == '/sitemap.xml' or path.endswith('.xml'):
            self.serve_sitemap(path)
        elif path.startswith('/robots.txt'):
            self.serve_robots_txt()
        else:
            self.send_error(404, "File not found")
    
    def handle_api_request(self, path, query_params):
        """处理API请求"""
        if path == '/api/tools':
            self.get_all_tools(query_params)
        elif path.startswith('/api/tools/'):
            tool_id = path.split('/')[-1]
            self.get_tool_by_id(tool_id)
        else:
            self.send_error(404, "API endpoint not found")
    
    def get_all_tools(self, query_params):
        """从PocketBase获取所有工具"""
        try:
            # 从PocketBase获取数据
            pb_response = requests.get(
                "http://localhost:8090/api/collections/ai_tools/records",
                params={"page": 1, "perPage": 100}
            )
            
            if pb_response.status_code == 200:
                pb_data = pb_response.json()
                tools = pb_data.get('items', [])
                
                # 转换数据格式以匹配前端期望
                formatted_tools = []
                for tool in tools:
                    formatted_tool = {
                        "id": tool.get('id'),
                        "name": tool.get('name', 'Unknown'),
                        "description": tool.get('description', ''),
                        "url": tool.get('url', '#'),
                        "category": tool.get('category', 'other'),
                        "rating": tool.get('rating', 0),
                        "is_free": tool.get('is_free', False),
                        "is_featured": tool.get('is_featured', False),
                        "language_support": tool.get('language_support', ''),
                        "tags": tool.get('tags', '').split(',') if tool.get('tags') else []
                    }
                    formatted_tools.append(formatted_tool)
                
                # 按评分排序（从高到低）
                formatted_tools.sort(key=lambda x: x['rating'], reverse=True)
                
                self.send_json_response(formatted_tools)
            else:
                # 如果PocketBase不可用，返回备用数据
                self.send_backup_tools()
        except Exception as e:
            print(f"Error fetching tools from PocketBase: {e}")
            # 如果PocketBase不可用，返回备用数据
            self.send_backup_tools()
    
    def get_tool_by_id(self, tool_id):
        """根据ID获取单个工具"""
        try:
            pb_response = requests.get(f"http://localhost:8090/api/collections/ai_tools/records/{tool_id}")
            
            if pb_response.status_code == 200:
                tool = pb_response.json()
                formatted_tool = {
                    "id": tool.get('id'),
                    "name": tool.get('name', 'Unknown'),
                    "description": tool.get('description', ''),
                    "url": tool.get('url', '#'),
                    "category": tool.get('category', 'other'),
                    "rating": tool.get('rating', 0),
                    "is_free": tool.get('is_free', False),
                    "is_featured": tool.get('is_featured', False),
                    "language_support": tool.get('language_support', ''),
                    "tags": tool.get('tags', '').split(',') if tool.get('tags') else []
                }
                self.send_json_response(formatted_tool)
            else:
                self.send_error(404, "Tool not found")
        except Exception as e:
            print(f"Error fetching tool from PocketBase: {e}")
            self.send_error(500, "Internal server error")
    
    def send_backup_tools(self):
        """发送备用工具数据"""
        backup_tools = [
            {
                "id": "1",
                "name": "ChatGPT",
                "description": "OpenAI开发的高级对话AI，能够回答问题、创作文字、编程等。强大的自然语言理解和生成能力，适用于各种文本创作场景。拥有GPT-4 Turbo等先进模型。",
                "url": "https://chat.openai.com",
                "category": "text",
                "rating": 4.9,
                "is_free": True,
                "is_featured": True,
                "language_support": "zh,en,ja,ko",
                "tags": ["chat", "gpt", "llm", "text-generation"]
            },
            {
                "id": "2",
                "name": "Midjourney",
                "description": "业界领先的AI图像生成工具，通过简单的文本描述就能创造出令人惊叹的艺术作品。拥有独特的艺术风格和强大的图像编辑功能。",
                "url": "https://www.midjourney.com",
                "category": "image",
                "rating": 4.9,
                "is_free": False,
                "is_featured": True,
                "language_support": "en",
                "tags": ["image", "art", "generation", "midjourney"]
            },
            {
                "id": "3",
                "name": "Claude 3.5 Sonnet",
                "description": "Anthropic公司开发的新一代AI助手，具有卓越的推理、视觉、代码生成能力。在复杂任务处理方面表现优异，是目前市场上最先进的AI模型之一。",
                "url": "https://claude.ai",
                "category": "text",
                "rating": 4.9,
                "is_free": False,
                "is_featured": True,
                "language_support": "en",
                "tags": ["anthropic", "claude", "ai", "assistant"]
            },
            {
                "id": "4",
                "name": "通义千问",
                "description": "阿里巴巴集团旗下的通义实验室自主研发的超大规模语言模型，能够回答问题、创作文字、表达观点、玩游戏等。具有强大的中文理解和生成能力。",
                "url": "https://tongyi.aliyun.com",
                "category": "chinese-ai",
                "rating": 4.8,
                "is_free": True,
                "is_featured": True,
                "language_support": "zh,en",
                "tags": ["chinese", "alibaba", "qwen", "llm"]
            },
            {
                "id": "5",
                "name": "GitHub Copilot",
                "description": "基于AI的编码助手，能够在多种编程语言中提供建议和自动完成。由OpenAI的Codex技术支持，集成在主流IDE中。",
                "url": "https://github.com/features/copilot",
                "category": "code",
                "rating": 4.8,
                "is_free": False,
                "is_featured": True,
                "language_support": "en",
                "tags": ["code", "programming", "assistant", "github"]
            },
            {
                "id": "6",
                "name": "DALL-E 3",
                "description": "OpenAI开发的先进图像生成AI，能够根据文本描述精确生成高质量图像。具有出色的细节控制能力和创意表达能力。",
                "url": "https://openai.com/dall-e-3",
                "category": "image",
                "rating": 4.8,
                "is_free": False,
                "is_featured": True,
                "language_support": "en",
                "tags": ["image", "openai", "dalle", "generation"]
            },
            {
                "id": "7",
                "name": "Stable Diffusion",
                "description": "开源的AI图像生成模型，允许用户在自己的设备上运行。具有高度可定制性和灵活性，社区支持强大。",
                "url": "https://stability.ai/stablediffusion",
                "category": "image",
                "rating": 4.6,
                "is_free": True,
                "is_featured": False,
                "language_support": "en",
                "tags": ["image", "open-source", "stability", "generation"]
            },
            {
                "id": "8",
                "name": "Kimi",
                "description": "月之暗面开发的大模型，具有强大的长文本理解和处理能力。能够处理长达数万字的输入，适合复杂的研究和分析任务。",
                "url": "https://kimi.moonshot.cn",
                "category": "search",
                "rating": 4.6,
                "is_free": True,
                "is_featured": False,
                "language_support": "zh",
                "tags": ["chinese", "long-context", "analysis"]
            },
            {
                "id": "9",
                "name": "ChatGPT-Next-Web",
                "description": "一键免费部署你的私人ChatGPT网页应用。支持多种AI服务提供商，界面简洁美观，易于部署和自定义。",
                "url": "https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web",
                "category": "github",
                "rating": 4.9,
                "is_free": True,
                "is_featured": True,
                "language_support": "zh,en",
                "tags": ["github", "open-source", "chatgpt", "web"]
            },
            {
                "id": "10",
                "name": "LangChain",
                "description": "用于开发由语言模型驱动的应用程序的框架。提供构建块来轻松创建LLM应用程序，支持多种模型和数据源集成。",
                "url": "https://github.com/langchain-ai/langchain",
                "category": "github",
                "rating": 4.8,
                "is_free": True,
                "is_featured": True,
                "language_support": "en",
                "tags": ["github", "llm", "framework", "ai"]
            },
            {
                "id": "11",
                "name": "ClawdHub Skill Creator",
                "description": "用于创建和发布AgentSkills的工具。帮助开发者轻松创建、测试和发布AI助手技能，提供完整的技能开发生态系统。",
                "url": "https://clawdhub.com/skill-creator",
                "category": "clawdhub",
                "rating": 4.9,
                "is_free": True,
                "is_featured": True,
                "language_support": "zh,en",
                "tags": ["clawdhub", "skills", "development", "tools"]
            },
            {
                "id": "12",
                "name": "AI Workflow Automation",
                "description": "自动化工作流技能，可将复杂的AI任务分解为可重复的工作流程。支持条件判断、循环和错误处理，提升AI助手的智能化水平。",
                "url": "https://clawdhub.com/workflow-automation",
                "category": "clawdhub",
                "rating": 4.8,
                "is_free": True,
                "is_featured": True,
                "language_support": "zh,en",
                "tags": ["clawdhub", "automation", "workflow", "ai"]
            },
            {
                "id": "13",
                "name": "ClawDBot",
                "description": "ClawDBot是一个功能强大的个人AI助理系统，能够帮您处理日常任务、管理信息、自动化工作流程。支持多种通信渠道，包括Telegram、WhatsApp、Signal等，可以成为您的专属AI助手，提升工作效率和生活品质。",
                "url": "https://clawdbot.com",
                "category": "personal-ai",
                "rating": 4.9,
                "is_free": False,
                "is_featured": True,
                "language_support": "zh,en",
                "tags": ["personal-ai", "assistant", "automation"]
            }
        ]
        
        # 按评分排序（从高到低）
        backup_tools.sort(key=lambda x: x['rating'], reverse=True)
        
        self.send_json_response(backup_tools)
    
    def serve_index_html(self):
        """提供带有赛博朋克风格的首页"""
        html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title data-i18n="pageTitle">AI工具大全 - 全球领先的AI工具聚合平台 | chuansha.tech</title>
    <meta name="description" content="全球领先的AI工具聚合平台，汇集全球最热门的AI工具，包括ChatGPT、Midjourney、Claude、Gemini等。提供一站式AI解决方案，涵盖文本生成、图像生成、编程助手、内容创作、商业应用等各类AI工具。">
    <meta name="keywords" content="AI工具,ChatGPT,Midjourney,Claude,Gemini,Stable Diffusion,通义千问,文心一言,LLaMA,Kimi,人工智能,文本生成,图像生成,编程助手,内容创作,商业AI,创意工具,搜索工具,个人AI助理,全球AI,海外AI工具,国际AI平台">
    <meta name="author" content="AI工具大全">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="CN">
    <meta name="geo.placename" content="China">
    <meta name="geo.position" content="39.9042;116.4074">
    <meta name="ICBM" content="39.9042, 116.4074">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://chuansha.tech/">
    <meta property="og:title" content="AI工具大全 - 全球领先的AI工具聚合平台">
    <meta property="og:description" content="全球领先的AI工具聚合平台，汇集全球最热门的AI工具，包括ChatGPT、Midjourney、Claude、Gemini等。一站式AI解决方案。">
    <meta property="og:image" content="https://chuansha.tech/images/ai-tools-og.jpg">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:locale:alternate" content="en_US">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="https://chuansha.tech/">
    <meta name="twitter:title" content="AI工具大全 - 全球领先的AI工具聚合平台">
    <meta name="twitter:description" content="全球领先的AI工具聚合平台，汇集全球最热门的AI工具，一站式AI解决方案">
    <meta name="twitter:image" content="https://chuansha.tech/images/ai-tools-twitter.jpg">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="https://chuansha.tech/">
    
    <!-- Alternate languages -->
    <link rel="alternate" hreflang="en" href="https://chuansha.tech/en">
    <link rel="alternate" hreflang="zh-CN" href="https://chuansha.tech/zh-cn">
    <link rel="alternate" hreflang="ja" href="https://chuansha.tech/ja">
    <link rel="alternate" hreflang="ko" href="https://chuansha.tech/ko">
    <link rel="alternate" hreflang="x-default" href="https://chuansha.tech/">
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "AI工具大全",
        "alternateName": ["AI Tools Hub", "AI工具中心", "AIツールハブ", "AI工具聚合平台"],
        "url": "https://chuansha.tech/",
        "description": "全球领先的AI工具聚合平台，汇集全球最热门的AI工具",
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://chuansha.tech/search?q={search_term}",
            "query-input": "required name=search_term"
        },
        "publisher": {
            "@type": "Organization",
            "name": "AI工具大全团队",
            "logo": {
                "@type": "ImageObject",
                "url": "https://chuansha.tech/images/logo.png"
            }
        }
    }
    </script>
    
    <style>
        /* 赛博朋克风格的CSS */
        :root {
            --cyber-primary: #0effc4; /* 青色霓虹 */
            --cyber-secondary: #ff00c8; /* 洋红色霓虹 */
            --cyber-accent: #00fffe; /* 青绿色霓虹 */
            --cyber-dark: #0a0a12; /* 深蓝黑色背景 */
            --cyber-darker: #050508; /* 更深的背景 */
            --cyber-light: #ffffff; /* 白色文字 */
            --cyber-gray: #1a1a2e; /* 深灰色 */
            --cyber-border: #ff00c8; /* 边框霓虹色 */
            --neon-glow: 0 0 10px #0effc4, 0 0 20px #0effc4, 0 0 30px #0effc4;
            --neon-glow-red: 0 0 10px #ff00c8, 0 0 20px #ff00c8, 0 0 30px #ff00c8;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Courier New', 'Monaco', 'Menlo', monospace;
            line-height: 1.6;
            color: var(--cyber-light);
            background: var(--cyber-dark);
            background-image: 
                radial-gradient(var(--cyber-secondary) 1px, transparent 1px),
                radial-gradient(var(--cyber-primary) 1px, transparent 1px);
            background-size: 50px 50px;
            background-position: 0 0, 25px 25px;
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }
        
        body::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                linear-gradient(transparent 50%, rgba(14, 255, 196, 0.05) 50%),
                linear-gradient(90deg, transparent 50%, rgba(255, 0, 200, 0.05) 50%);
            background-size: 8px 8px;
            z-index: -1;
            pointer-events: none;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* 赛博朋克风格的头部 */
        .main-header {
            background: rgba(10, 10, 18, 0.9);
            background-image: linear-gradient(to right, var(--cyber-secondary), var(--cyber-primary));
            color: white;
            padding: 40px 0;
            text-align: center;
            margin-bottom: 40px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(255, 0, 200, 0.5);
            border: 2px solid var(--cyber-secondary);
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        
        .main-header::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, var(--cyber-primary), var(--cyber-secondary), var(--cyber-accent), var(--cyber-primary));
            z-index: -1;
            border-radius: 12px;
            animation: gradientShift 3s ease infinite;
            background-size: 300% 300%;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .brand-section {
            position: relative;
            z-index: 2;
            margin-bottom: 30px;
        }
        
        .logo {
            width: 120px;
            height: 120px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            font-size: 3rem;
            backdrop-filter: blur(10px);
            border: 2px solid var(--cyber-primary);
            box-shadow: var(--neon-glow);
            animation: pulse 2s infinite alternate;
        }
        
        @keyframes pulse {
            from { box-shadow: var(--neon-glow); }
            to { box-shadow: 0 0 20px #0effc4, 0 0 40px #0effc4, 0 0 60px #0effc4; }
        }
        
        .site-title {
            font-size: 3.5rem;
            margin-bottom: 15px;
            font-weight: 800;
            letter-spacing: -1px;
            text-shadow: 0 0 10px var(--cyber-primary), 0 0 20px var(--cyber-primary);
            animation: titleGlow 3s ease-in-out infinite alternate;
            background: linear-gradient(to right, var(--cyber-primary), var(--cyber-secondary), var(--cyber-accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        @keyframes titleGlow {
            0% { text-shadow: 0 0 10px var(--cyber-primary); }
            100% { text-shadow: 0 0 20px var(--cyber-primary), 0 0 30px var(--cyber-secondary); }
        }
        
        .site-slogan {
            font-size: 1.5rem;
            margin-bottom: 10px;
            opacity: 0.9;
            text-shadow: 0 0 10px var(--cyber-accent);
            animation: fadeInUp 1s ease 0.2s both;
        }
        
        .site-subtitle {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto 15px; /* 减小间距 */
            opacity: 0.8;
            animation: fadeInUp 1s ease 0.4s both;
        }
        
        /* 新增：联系方式样式 */
        .contact-info {
            font-size: 1.1rem;
            max-width: 800px;
            margin: 15px auto 0;
            color: var(--cyber-primary);
            text-shadow: 0 0 10px var(--cyber-primary);
            animation: blink 2s infinite;
            position: relative;
            z-index: 2;
        }
        
        .contact-info a {
            color: var(--cyber-secondary);
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .contact-info a:hover {
            color: var(--cyber-accent);
            text-shadow: 0 0 10px var(--cyber-accent);
        }
        
        @keyframes blink {
            0%, 50% { opacity: 1; }
            51%, 100% { opacity: 0.8; }
        }
        
        /* 赛博朋克风格的导航 */
        .main-nav {
            background: rgba(26, 26, 46, 0.8);
            backdrop-filter: blur(10px);
            border-radius: 12px;
            padding: 20px;
            margin: 0 auto 40px;
            max-width: 1000px;
            animation: slideInUp 1s ease 0.6s both;
            border: 1px solid var(--cyber-primary);
            box-shadow: 0 0 15px rgba(14, 255, 196, 0.3);
        }
        
        .nav-container {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .search-section {
            display: flex;
            gap: 15px;
            align-items: center;
        }
        
        .search-input {
            flex: 1;
            padding: 15px 20px;
            border: 2px solid var(--cyber-primary);
            border-radius: 12px;
            background: rgba(10, 10, 18, 0.7);
            color: white;
            font-size: 1rem;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            font-family: inherit;
        }
        
        .search-input::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }
        
        .search-input:focus {
            outline: none;
            border-color: var(--cyber-secondary);
            box-shadow: 0 0 15px rgba(255, 0, 200, 0.5);
            background: rgba(10, 10, 18, 0.9);
        }
        
        .search-button {
            padding: 15px 25px;
            background: linear-gradient(45deg, var(--cyber-secondary), var(--cyber-primary));
            color: white;
            border: none;
            border-radius: 12px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: inherit;
        }
        
        .search-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 0, 200, 0.4);
        }
        
        .filter-section {
            display: flex;
            gap: 15px;
            align-items: center;
            flex-wrap: wrap;
        }
        
        .filter-label {
            color: var(--cyber-primary);
            font-weight: 500;
            white-space: nowrap;
            text-shadow: 0 0 5px var(--cyber-primary);
        }
        
        .filter-select {
            padding: 12px 15px;
            border: 2px solid var(--cyber-primary);
            border-radius: 12px;
            background: rgba(10, 10, 18, 0.7);
            color: white;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            font-family: inherit;
        }
        
        .filter-select:focus {
            outline: none;
            border-color: var(--cyber-secondary);
            box-shadow: 0 0 15px rgba(255, 0, 200, 0.5);
        }
        
        /* 赛博朋克风格的分类导航 */
        .category-nav {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 12px;
            margin: 30px 0 40px;
            padding: 0 20px;
        }
        
        .category-btn {
            padding: 12px 24px;
            border: 2px solid var(--cyber-primary);
            background: rgba(10, 10, 18, 0.7);
            color: var(--cyber-primary);
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: inherit;
            font-size: 1rem;
            backdrop-filter: blur(10px);
            position: relative;
            overflow: hidden;
        }
        
        .category-btn:hover {
            background: rgba(255, 0, 200, 0.2);
            color: white;
            border-color: var(--cyber-secondary);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 0, 200, 0.3);
        }
        
        .category-btn.active {
            background: linear-gradient(45deg, var(--cyber-secondary), var(--cyber-primary));
            color: white;
            border-color: white;
            box-shadow: 0 5px 15px rgba(255, 0, 200, 0.4);
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
        }
        
        .stats-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 40px 0;
            padding: 0 20px;
        }
        
        .stat-item {
            background: rgba(26, 26, 46, 0.6);
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 1px solid var(--cyber-primary);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .stat-item::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, var(--cyber-primary), var(--cyber-secondary));
            z-index: -1;
            border-radius: 14px;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .stat-item:hover {
            transform: translateY(-5px);
            background: rgba(26, 26, 46, 0.8);
        }
        
        .stat-item:hover::before {
            opacity: 1;
        }
        
        .stat-number {
            display: block;
            font-size: 2.5rem;
            font-weight: bold;
            color: var(--cyber-primary);
            margin-bottom: 8px;
            text-shadow: 0 0 10px var(--cyber-primary);
        }
        
        .stat-label {
            font-size: 1rem;
            color: rgba(255, 255, 255, 0.8);
        }
        
        /* 赛博朋克风格的工具网格 */
        .tools-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 30px;
            margin: 40px 0 60px;
        }
        
        .tool-card {
            background: rgba(26, 26, 46, 0.6);
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(14, 255, 196, 0.3);
            backdrop-filter: blur(10px);
        }
        
        .tool-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--cyber-primary), var(--cyber-secondary));
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .tool-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4), 0 0 20px rgba(14, 255, 196, 0.3);
            border-color: var(--cyber-primary);
        }
        
        .tool-card:hover::before {
            opacity: 1;
        }
        
        .tool-badge {
            position: absolute;
            top: 15px;
            right: 15px;
            background: linear-gradient(45deg, var(--cyber-secondary), var(--cyber-primary));
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
            z-index: 2;
            text-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
        }
        
        .tool-category {
            display: inline-block;
            background: rgba(14, 255, 196, 0.1);
            color: var(--cyber-primary);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.9rem;
            margin-bottom: 15px;
            border: 1px solid var(--cyber-primary);
        }
        
        .tool-title {
            font-size: 1.4rem;
            color: var(--cyber-primary);
            margin-bottom: 12px;
            font-weight: 600;
            text-shadow: 0 0 5px rgba(14, 255, 196, 0.5);
        }
        
        .tool-description {
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 20px;
            line-height: 1.7;
            font-size: 1rem;
        }
        
        .rating {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .rating-stars {
            color: var(--cyber-accent);
            font-size: 1.2rem;
            text-shadow: 0 0 5px var(--cyber-accent);
        }
        
        .tool-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 20px;
        }
        
        .tool-link {
            display: inline-block;
            background: linear-gradient(45deg, var(--cyber-primary), var(--cyber-secondary));
            color: white;
            padding: 10px 20px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            font-family: inherit;
        }
        
        .tool-link:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(14, 255, 196, 0.4), 0 0 15px rgba(255, 0, 200, 0.4);
        }
        
        .tag {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: bold;
            margin-top: 10px;
            border: 1px solid;
        }
        
        .tag-free {
            background: rgba(46, 204, 113, 0.1);
            color: #2ecc71;
            border-color: #2ecc71;
        }
        
        .tag-paid {
            background: rgba(231, 76, 60, 0.1);
            color: #e74c3c;
            border-color: #e74c3c;
        }
        
        .tag-chinese {
            background: rgba(241, 196, 15, 0.1);
            color: #f1c40f;
            border-color: #f1c40f;
        }
        
        .hidden {
            display: none;
        }
        
        /* 赛博朋克风格的底部 */
        footer {
            background: rgba(10, 10, 18, 0.95);
            background-image: linear-gradient(to right, var(--cyber-secondary), var(--cyber-primary));
            color: white;
            padding: 60px 0 30px;
            margin-top: 80px;
            text-align: center;
            position: relative;
            border-top: 2px solid var(--cyber-secondary);
            box-shadow: 0 -5px 20px rgba(255, 0, 200, 0.3);
        }
        
        footer::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, var(--cyber-primary), var(--cyber-secondary), var(--cyber-accent));
            z-index: -1;
            animation: gradientShift 3s ease infinite;
            background-size: 300% 300%;
            border-radius: 0;
        }
        
        .footer-content {
            max-width: 1000px;
            margin: 0 auto;
            padding: 0 20px;
            position: relative;
            z-index: 2;
        }
        
        .footer-brand {
            margin-bottom: 30px;
        }
        
        .footer-title {
            font-size: 2rem;
            margin-bottom: 15px;
            color: white;
            text-shadow: 0 0 10px var(--cyber-primary);
        }
        
        .footer-description {
            max-width: 600px;
            margin: 0 auto 25px;
            opacity: 0.9;
            line-height: 1.7;
        }
        
        .trust-indicators {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        
        .trust-item {
            display: flex;
            align-items: center;
            gap: 8px;
            opacity: 0.9;
        }
        
        .footer-links {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        
        .footer-link {
            color: rgba(255, 255, 255, 0.8);
            text-decoration: none;
            transition: all 0.3s ease;
            padding: 8px 15px;
            border-radius: 5px;
        }
        
        .footer-link:hover {
            color: white;
            background: rgba(255, 255, 255, 0.1);
            text-shadow: 0 0 10px var(--cyber-primary);
        }
        
        .copyright-info {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.2);
            opacity: 0.7;
        }
        
        /* 赛博朋克风格的语言切换器 */
        .language-switcher {
            position: fixed;
            top: 20px;
            right: 20px;
            display: flex;
            background: rgba(10, 10, 18, 0.8);
            border-radius: 30px;
            padding: 5px;
            z-index: 1000;
            backdrop-filter: blur(10px);
            border: 1px solid var(--cyber-primary);
            box-shadow: 0 0 15px rgba(14, 255, 196, 0.3);
        }
        
        .lang-option {
            padding: 10px 18px;
            cursor: pointer;
            border-radius: 25px;
            transition: all 0.3s ease;
            font-size: 0.9rem;
            color: var(--cyber-primary);
            text-shadow: 0 0 5px var(--cyber-primary);
        }
        
        .lang-option:hover {
            background: rgba(255, 0, 200, 0.2);
            color: white;
        }
        
        .lang-option.active {
            background: linear-gradient(45deg, var(--cyber-secondary), var(--cyber-primary));
            color: white;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
        }
        
        /* 返回顶部按钮 */
        .back-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(45deg, var(--cyber-primary), var(--cyber-secondary));
            color: white;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            opacity: 0;
            transition: all 0.3s ease;
            z-index: 1000;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: inherit;
        }
        
        .back-to-top.show {
            opacity: 1;
        }
        
        .back-to-top:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(14, 255, 196, 0.4), 0 0 20px rgba(255, 0, 200, 0.4);
        }
        
        /* 社交分享 */
        .social-share {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 25px 0;
            flex-wrap: wrap;
        }
        
        .share-btn {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(10, 10, 18, 0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            cursor: pointer;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            border: 1px solid var(--cyber-primary);
            color: var(--cyber-primary);
        }
        
        .share-btn:hover {
            background: linear-gradient(45deg, var(--cyber-secondary), var(--cyber-primary));
            color: white;
            transform: scale(1.1);
            box-shadow: 0 0 15px rgba(255, 0, 200, 0.4);
        }
        
        /* 模态框 */
        .modal {
            display: none;
            position: fixed;
            z-index: 2000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(10, 10, 18, 0.9);
            backdrop-filter: blur(8px);
        }
        
        .modal-content {
            background: rgba(26, 26, 46, 0.95);
            margin: 5% auto;
            padding: 35px;
            border-radius: 12px;
            width: 85%;
            max-width: 700px;
            position: relative;
            animation: modalAppear 0.4s ease;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
            border: 1px solid var(--cyber-primary);
            backdrop-filter: blur(10px);
        }
        
        @keyframes modalAppear {
            from { opacity: 0; transform: translateY(-60px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .close-modal {
            color: var(--cyber-primary);
            float: right;
            font-size: 32px;
            font-weight: bold;
            cursor: pointer;
            position: absolute;
            right: 20px;
            top: 15px;
            transition: all 0.3s ease;
        }
        
        .close-modal:hover {
            color: var(--cyber-secondary);
            text-shadow: 0 0 10px var(--cyber-secondary);
        }
        
        .modal-title {
            color: var(--cyber-primary);
            margin-bottom: 20px;
            font-size: 1.8rem;
            border-bottom: 2px solid var(--cyber-primary);
            padding-bottom: 15px;
        }
        
        .modal-description {
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 25px;
            line-height: 1.7;
            font-size: 1.1rem;
        }
        
        .modal-details {
            margin: 25px 0;
            padding: 20px;
            background: rgba(10, 10, 18, 0.5);
            border-radius: 12px;
            border-left: 4px solid var(--cyber-primary);
        }
        
        .modal-actions {
            text-align: center;
            margin-top: 25px;
        }
        
        /* Toast消息 */
        .toast-message {
            position: fixed;
            bottom: 25px;
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background: rgba(10, 10, 18, 0.9);
            color: var(--cyber-primary);
            padding: 15px 30px;
            border-radius: 12px;
            z-index: 3000;
            font-size: 16px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
            border: 1px solid var(--cyber-primary);
            opacity: 0;
            transition: all 0.3s ease;
        }
        
        .toast-message.show {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
        
        /* 动画定义 */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* 响应式设计 */
        @media (max-width: 1200px) {
            .tools-grid {
                grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            }
            
            .site-title {
                font-size: 3rem;
            }
        }
        
        @media (max-width: 992px) {
            .site-title {
                font-size: 2.5rem;
            }
            
            .site-slogan {
                font-size: 1.3rem;
            }
            
            .site-subtitle {
                font-size: 1.1rem;
            }
            
            .tools-grid {
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            }
            
            .main-nav {
                padding: 15px;
            }
            
            .search-section {
                flex-direction: column;
            }
            
            .filter-section {
                flex-direction: column;
            }
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 0 15px;
            }
            
            .site-title {
                font-size: 2rem;
            }
            
            .site-slogan {
                font-size: 1.1rem;
            }
            
            .site-subtitle {
                font-size: 1rem;
            }
            
            .logo {
                width: 100px;
                height: 100px;
                font-size: 2.5rem;
            }
            
            .tools-grid {
                grid-template-columns: 1fr;
                gap: 25px;
            }
            
            .tool-card {
                padding: 25px;
            }
            
            .category-nav {
                gap: 8px;
            }
            
            .category-btn {
                padding: 10px 15px;
                font-size: 0.9rem;
            }
            
            .stats-container {
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 15px;
            }
            
            .stat-item {
                padding: 20px;
            }
            
            .stat-number {
                font-size: 2rem;
            }
            
            .main-header {
                padding: 30px 0;
            }
            
            .language-switcher {
                position: static;
                justify-content: center;
                margin: 20px auto;
                width: fit-content;
            }
            
            .social-share {
                gap: 12px;
            }
            
            .share-btn {
                width: 45px;
                height: 45px;
                font-size: 1rem;
            }
        }
        
        @media (max-width: 576px) {
            .site-title {
                font-size: 1.8rem;
            }
            
            .site-slogan {
                font-size: 1rem;
            }
            
            .tool-title {
                font-size: 1.3rem;
            }
            
            .tool-description {
                font-size: 0.95rem;
            }
            
            .tool-card {
                padding: 20px;
            }
            
            .tool-badge {
                top: 10px;
                right: 10px;
                font-size: 0.7rem;
                padding: 4px 8px;
            }
            
            .tool-category {
                font-size: 0.85rem;
                padding: 5px 10px;
            }
            
            .tool-actions {
                flex-direction: column;
            }
            
            .tool-link {
                width: 100%;
                text-align: center;
            }
            
            .stats-container {
                grid-template-columns: 1fr;
            }
            
            .modal-content {
                width: 95%;
                padding: 25px;
            }
            
            .modal-title {
                font-size: 1.5rem;
            }
            
            .footer-links {
                flex-direction: column;
                gap: 15px;
            }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Press+Start+2P&display=swap" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🤖</text></svg>">
    <link rel="alternate" type="application/rss+xml" title="AI工具大全 - 最新AI工具" href="/rss/latest.xml">
</head>
<body>
    <!-- 语言切换器 -->
    <div class="language-switcher">
        <div class="lang-option active" data-lang="zh-CN">中文</div>
        <div class="lang-option" data-lang="en">English</div>
        <div class="lang-option" data-lang="ja">日本語</div>
        <div class="lang-option" data-lang="ko">한국어</div>
    </div>
    
    <div class="container">
        <!-- 主要头部区域 -->
        <header class="main-header">
            <div class="brand-section">
                <div class="logo">🤖</div>
                <h1 class="site-title" data-i18n="siteTitle">AI工具大全</h1>
                <p class="site-slogan" data-i18n="siteSlogan">赛博朋克风AI工具聚合平台</p>
                <p class="site-subtitle" data-i18n="siteSubtitle">全球领先的AI工具聚合平台，汇集全球最热门的AI工具，为您提供一站式AI解决方案</p>
                <p class="contact-info" style="margin-top: 15px; font-size: 1.1rem; color: #0effc4; text-shadow: 0 0 10px #0effc4; animation: blink 2s infinite;">
                    如有问题请联系: Joey Qiao - <a href="mailto:mouseqiao@163.com" style="color: #ff00c8; text-decoration: none;">mouseqiao@163.com</a>
                </p>
            </div>
            
            <!-- 社交分享 -->
            <div class="social-share">
                <div class="share-btn" title="分享到Twitter" onclick="shareToSocial('twitter')">🐦</div>
                <div class="share-btn" title="分享到Facebook" onclick="shareToSocial('facebook')">📘</div>
                <div class="share-btn" title="分享到LinkedIn" onclick="shareToSocial('linkedin')">👔</div>
                <div class="share-btn" title="分享到Reddit" onclick="shareToSocial('reddit')">🔺</div>
            </div>
        </header>
        
        <!-- 主导航区域 -->
        <nav class="main-nav">
            <div class="nav-container">
                <div class="search-section">
                    <input type="text" id="searchInput" class="search-input" placeholder="搜索AI工具..." autocomplete="off" data-i18n-placeholder="searchPlaceholder">
                    <button class="search-button" onclick="performSearch()">搜索</button>
                </div>
                
                <div class="filter-section">
                    <span class="filter-label" data-i18n="sortBy">排序:</span>
                    <select id="sortSelect" class="filter-select" onchange="sortTools()">
                        <option value="name" data-i18n="sortByName">按名称</option>
                        <option value="rating" data-i18n="sortByRating" selected>按评分</option>
                        <option value="category" data-i18n="sortByCategory">按类别</option>
                    </select>
                </div>
            </div>
        </nav>
        
        <!-- 统计数据区域 -->
        <div class="stats-container">
            <div class="stat-item">
                <span class="stat-number" id="totalTools">加载中...</span>
                <span class="stat-label" data-i18n="totalTools">总数</span>
            </div>
            <div class="stat-item">
                <span class="stat-number" id="aiTools">加载中...</span>
                <span class="stat-label">AI工具</span>
            </div>
            <div class="stat-item">
                <span class="stat-number" id="githubProjects">加载中...</span>
                <span class="stat-label">GitHub项目</span>
            </div>
            <div class="stat-item">
                <span class="stat-number" id="clawdSkills">加载中...</span>
                <span class="stat-label">ClawdHub技能</span>
            </div>
        </div>
        
        <!-- 分类导航 -->
        <div class="category-nav">
            <button class="category-btn active" data-category="all" data-i18n="allCategories"><i>🌐</i> 全部</button>
            <button class="category-btn" data-category="text" data-i18n="textGeneration"><i>📝</i> 文本生成</button>
            <button class="category-btn" data-category="image" data-i18n="imageGeneration"><i>🖼️</i> 图像生成</button>
            <button class="category-btn" data-category="audio" data-i18n="audioTools"><i>🎵</i> 音频工具</button>
            <button class="category-btn" data-category="video" data-i18n="videoTools"><i>🎬</i> 视频工具</button>
            <button class="category-btn" data-category="code" data-i18n="codingAssistants"><i>💻</i> 编程助手</button>
            <button class="category-btn" data-category="content" data-i18n="contentCreation"><i>✍️</i> 内容创作</button>
            <button class="category-btn" data-category="business" data-i18n="businessTools"><i>💼</i> 商业工具</button>
            <button class="category-btn" data-category="creative" data-i18n="creativeTools"><i>🎨</i> 创意工具</button>
            <button class="category-btn" data-category="personal-ai" data-i18n="personalAi"><i>🤖</i> 个人AI助理</button>
            <button class="category-btn" data-category="github" data-i18n="githubProjects"><i>🐙</i> GitHub热门</button>
            <button class="category-btn" data-category="clawdhub" data-i18n="clawdhubSkills"><i>⚙️</i> ClawdHub技能</button>
            <button class="category-btn" data-category="search" data-i18n="searchTools"><i>🔍</i> 搜索工具</button>
            <button class="category-btn" data-category="chinese-ai" data-i18n="chineseAi"><i>🇨🇳</i> 国产AI</button>
        </div>
        
        <!-- 工具网格 -->
        <main>
            <div class="tools-grid" id="toolsGrid">
                <!-- 工具卡将通过JavaScript动态加载 -->
                <div class="loading-placeholder">
                    <p>正在加载AI工具...</p>
                </div>
            </div>
        </main>
        
        <!-- 返回顶部按钮 -->
        <button class="back-to-top" onclick="scrollToTop()">↑</button>
    </div>
    
    <!-- 模态框 -->
    <div id="toolModal" class="modal">
        <div class="modal-content">
            <span class="close-modal" onclick="closeModal()">&times;</span>
            <h2 class="modal-title">工具详情</h2>
            <p class="modal-description">这里是工具的详细信息...</p>
            <div class="modal-details">
                <h3>功能特点</h3>
                <ul>
                    <li>强大的AI能力</li>
                    <li>用户友好的界面</li>
                    <li>丰富的定制选项</li>
                </ul>
            </div>
            <div class="modal-actions">
                <a href="#" class="tool-link" id="modalVisitLink" target="_blank">访问官网</a>
            </div>
        </div>
    </div>
    
    <!-- Toast消息 -->
    <div id="toastMessage" class="toast-message"></div>
    
    <script>
        // JavaScript功能实现 - 与PocketBase集成
        document.addEventListener('DOMContentLoaded', function() {
            // 加载工具数据
            loadTools();
            
            // 为分类按钮添加事件监听器
            const categoryBtns = document.querySelectorAll('.category-btn');
            categoryBtns.forEach(btn => {
                btn.addEventListener('click', function() {
                    // 移除所有活动状态
                    categoryBtns.forEach(b => b.classList.remove('active'));
                    // 添加当前活动状态
                    this.classList.add('active');
                    // 过滤工具
                    filterTools(this.dataset.category);
                });
            });
            
            // 为搜索输入框添加事件监听器
            const searchInput = document.getElementById('searchInput');
            searchInput.addEventListener('input', function() {
                performSearch();
            });
            
            // 为排序选择框添加事件监听器
            const sortSelect = document.getElementById('sortSelect');
            sortSelect.addEventListener('change', function() {
                sortTools();
            });
            
            // 监听滚动事件，显示/隐藏返回顶部按钮
            window.addEventListener('scroll', function() {
                const backToTopBtn = document.querySelector('.back-to-top');
                if (window.pageYOffset > 300) {
                    backToTopBtn.classList.add('show');
                } else {
                    backToTopBtn.classList.remove('show');
                }
            });
            
            // 语言切换功能
            const langOptions = document.querySelectorAll('.lang-option');
            langOptions.forEach(option => {
                option.addEventListener('click', function() {
                    langOptions.forEach(opt => opt.classList.remove('active'));
                    this.classList.add('active');
                    changeLanguage(this.dataset.lang);
                });
            });
        });
        
        async function loadTools() {
            try {
                const response = await fetch('/api/tools');
                if (response.ok) {
                    let tools = await response.json();
                    // 默认按评分排序（从高到低）
                    tools.sort((a, b) => b.rating - a.rating);
                    renderTools(tools);
                    updateStats(tools);
                } else {
                    console.error('Failed to load tools:', response.statusText);
                    // 如果API失败，使用静态数据
                    loadStaticTools();
                }
            } catch (error) {
                console.error('Error loading tools:', error);
                // 如果API失败，使用静态数据
                loadStaticTools();
            }
        }
        
        function loadStaticTools() {
            // 静态工具数据作为后备
            const staticTools = [
                {
                    id: "1",
                    name: "ChatGPT",
                    description: "OpenAI开发的高级对话AI，能够回答问题、创作文字、编程等。强大的自然语言理解和生成能力，适用于各种文本创作场景。拥有GPT-4 Turbo等先进模型。",
                    url: "https://chat.openai.com",
                    category: "text",
                    rating: 4.9,
                    is_free: true,
                    is_featured: true,
                    language_support: "zh,en,ja,ko",
                    tags: ["chat", "gpt", "llm", "text-generation"]
                },
                {
                    id: "2",
                    name: "Midjourney",
                    description: "业界领先的AI图像生成工具，通过简单的文本描述就能创造出令人惊叹的艺术作品。拥有独特的艺术风格和强大的图像编辑功能。",
                    url: "https://www.midjourney.com",
                    category: "image",
                    rating: 4.9,
                    is_free: false,
                    is_featured: true,
                    language_support: "en",
                    tags: ["image", "art", "generation", "midjourney"]
                },
                {
                    id: "3",
                    name: "Claude 3.5 Sonnet",
                    description: "Anthropic公司开发的新一代AI助手，具有卓越的推理、视觉、代码生成能力。在复杂任务处理方面表现优异，是目前市场上最先进的AI模型之一。",
                    url: "https://claude.ai",
                    category: "text",
                    rating: 4.9,
                    is_free: false,
                    is_featured: true,
                    language_support: "en",
                    tags: ["anthropic", "claude", "ai", "assistant"]
                },
                {
                    id: "4",
                    name: "通义千问",
                    description: "阿里巴巴集团旗下的通义实验室自主研发的超大规模语言模型，能够回答问题、创作文字、表达观点、玩游戏等。具有强大的中文理解和生成能力。",
                    url: "https://tongyi.aliyun.com",
                    category: "chinese-ai",
                    rating: 4.8,
                    is_free: true,
                    is_featured: true,
                    language_support: "zh,en",
                    tags: ["chinese", "alibaba", "qwen", "llm"]
                },
                {
                    id: "5",
                    name: "GitHub Copilot",
                    description: "基于AI的编码助手，能够在多种编程语言中提供建议和自动完成。由OpenAI的Codex技术支持，集成在主流IDE中。",
                    url: "https://github.com/features/copilot",
                    category: "code",
                    rating: 4.8,
                    is_free: false,
                    is_featured: true,
                    language_support: "en",
                    tags: ["code", "programming", "assistant", "github"]
                }
            ];
            
            // 按评分排序（从高到低）
            staticTools.sort((a, b) => b.rating - a.rating);
            
            renderTools(staticTools);
            updateStats(staticTools);
        }
        
        function renderTools(tools) {
            // 保存当前工具数据，以便语言切换时可以重新渲染
            window.currentToolsData = tools;
            
            const toolsGrid = document.getElementById('toolsGrid');
            toolsGrid.innerHTML = '';
            
            // 获取当前语言
            const currentLang = getCurrentLanguage();
            
            // 获取翻译文本
            const langTexts = {
                'zh-CN': { featured: '推荐', free: '免费版', paid: '付费', visitWebsite: '访问官网', copyLink: '复制链接' },
                'en': { featured: 'Featured', free: 'Free', paid: 'Paid', visitWebsite: 'Visit Website', copyLink: 'Copy Link' },
                'ja': { featured: 'おすすめ', free: '無料', paid: '有料', visitWebsite: '公式サイトへ', copyLink: 'リンクをコピー' },
                'ko': { featured: '추천', free: '무료', paid: '유료', visitWebsite: '웹사이트 방문', copyLink: '링크 복사' }
            };
            
            const texts = langTexts[currentLang] || langTexts['zh-CN'];
            
            tools.forEach(tool => {
                const toolCard = document.createElement('div');
                toolCard.className = 'tool-card';
                toolCard.dataset.category = tool.category;
                toolCard.dataset.rating = tool.rating;
                toolCard.dataset.free = tool.is_free;
                
                // 根据评分生成星级
                const stars = generateStars(tool.rating);
                
                // 确定标签类型
                let tagHtml = '';
                if(tool.is_free) {
                    tagHtml += `<span class="tag tag-free">${texts.free}</span>`;
                } else {
                    tagHtml += `<span class="tag tag-paid">${texts.paid}</span>`;
                }
                
                if(tool.category === 'chinese-ai') {
                    // 根据语言显示不同的国产AI标签
                    const chineseTagText = currentLang === 'zh-CN' ? '国产' : 
                                          currentLang === 'ja' ? '中国製' : 
                                          currentLang === 'ko' ? '중국산' : 'Chinese';
                    tagHtml += `<span class="tag tag-chinese">${chineseTagText}</span>`;
                }
                
                // 获取本地化的分类名称
                const categoryName = getCategoryNameLocalized(tool.category, currentLang);
                
                toolCard.innerHTML = `
                    ${tool.is_featured ? `<span class="tool-badge">${texts.featured}</span>` : ''}
                    <span class="tool-category">${categoryName}</span>
                    <h3 class="tool-title">${tool.name}</h3>
                    <p class="tool-description">${tool.description}</p>
                    <div class="rating">
                        <div class="rating-stars">${stars}</div>
                        <span>${tool.rating}/5</span>
                    </div>
                    <div class="tool-actions">
                        <a href="${tool.url}" target="_blank" class="tool-link">${texts.visitWebsite}</a>
                        <a href="#" class="tool-link" onclick="event.preventDefault(); event.stopPropagation(); copyToClipboard('${tool.url}');">${texts.copyLink}</a>
                    </div>
                    <div>${tagHtml}</div>
                `;
                
                toolsGrid.appendChild(toolCard);
            });
        }
        
        function updateStats(tools) {
            const totalTools = tools.length;
            const aiTools = tools.filter(t => !['github', 'clawdhub'].includes(t.category)).length;
            const githubProjects = tools.filter(t => t.category === 'github').length;
            const clawdSkills = tools.filter(t => t.category === 'clawdhub').length;
            
            document.getElementById('totalTools').textContent = totalTools;
            document.getElementById('aiTools').textContent = aiTools;
            document.getElementById('githubProjects').textContent = githubProjects;
            document.getElementById('clawdSkills').textContent = clawdSkills;
        }
        
        // 旧的getCategoryName函数，为了兼容性保留，但建议使用getCategoryNameLocalized
        function getCategoryName(category) {
            const currentLang = getCurrentLanguage();
            return getCategoryNameLocalized(category, currentLang);
        }
        
        function generateStars(rating) {
            const fullStars = Math.floor(rating);
            const hasHalfStar = rating % 1 >= 0.5;
            let stars = '';
            
            for(let i = 0; i < fullStars; i++) {
                stars += '<span class="star">★</span>';
            }
            
            if(hasHalfStar) {
                stars += '<span class="star">☆</span>';
            }
            
            // 填充剩余星星
            const remaining = 5 - Math.ceil(rating);
            for(let i = 0; i < remaining; i++) {
                stars += '<span class="star">☆</span>';
            }
            
            return stars;
        }
        
        function filterTools(category) {
            const tools = document.querySelectorAll('.tool-card');
            tools.forEach(tool => {
                if (category === 'all' || tool.dataset.category === category) {
                    tool.style.display = 'block';
                } else {
                    tool.style.display = 'none';
                }
            });
        }
        
        function performSearch() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const tools = document.querySelectorAll('.tool-card');
            
            tools.forEach(tool => {
                const title = tool.querySelector('.tool-title').textContent.toLowerCase();
                const description = tool.querySelector('.tool-description').textContent.toLowerCase();
                const category = tool.querySelector('.tool-category').textContent.toLowerCase();
                
                if (title.includes(searchTerm) || description.includes(searchTerm) || category.includes(searchTerm)) {
                    tool.style.display = 'block';
                } else {
                    tool.style.display = 'none';
                }
            });
        }
        
        function sortTools() {
            const sortValue = document.getElementById('sortSelect').value;
            const toolsGrid = document.getElementById('toolsGrid');
            const tools = Array.from(document.querySelectorAll('.tool-card'));
            
            switch(sortValue) {
                case 'name':
                    tools.sort((a, b) => {
                        const titleA = a.querySelector('.tool-title').textContent.toLowerCase();
                        const titleB = b.querySelector('.tool-title').textContent.toLowerCase();
                        return titleA.localeCompare(titleB);
                    });
                    break;
                case 'rating':
                    tools.sort((a, b) => {
                        const ratingA = parseFloat(a.dataset.rating);
                        const ratingB = parseFloat(b.dataset.rating);
                        return ratingB - ratingA; // 降序排列
                    });
                    break;
                case 'category':
                    tools.sort((a, b) => {
                        const catA = a.dataset.category.toLowerCase();
                        const catB = b.dataset.category.toLowerCase();
                        return catA.localeCompare(catB);
                    });
                    break;
            }
            
            // 重新排列DOM元素
            tools.forEach(tool => toolsGrid.appendChild(tool));
        }
        
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
        
        function showModal(toolName, description, link) {
            const modal = document.getElementById('toolModal');
            document.querySelector('.modal-title').textContent = toolName;
            document.querySelector('.modal-description').textContent = description;
            document.getElementById('modalVisitLink').href = link;
            modal.style.display = 'block';
        }
        
        function closeModal() {
            const modal = document.getElementById('toolModal');
            modal.style.display = 'none';
        }
        
        // 关闭模态框当点击外部区域时
        window.onclick = function(event) {
            const modal = document.getElementById('toolModal');
            if (event.target === modal) {
                closeModal();
            }
        }
        
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(function() {
                showToast('链接已复制到剪贴板！');
            }).catch(function(err) {
                console.error('复制失败: ', err);
                showToast('复制失败，请手动复制');
            });
        }
        
        function showToast(message) {
            const toast = document.getElementById('toastMessage');
            toast.textContent = message;
            toast.classList.add('show');
            
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        }
        
        function shareToSocial(platform) {
            const url = window.location.href;
            const title = document.title;
            let shareUrl = '';
            
            switch(platform) {
                case 'twitter':
                    shareUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(title)}`;
                    break;
                case 'facebook':
                    shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
                    break;
                case 'linkedin':
                    shareUrl = `https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}`;
                    break;
                case 'reddit':
                    shareUrl = `https://www.reddit.com/submit?url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}`;
                    break;
            }
            
            window.open(shareUrl, '_blank', 'width=600,height=400');
        }
        
        // 翻译数据
        const translations = {
            'zh-CN': {
                'pageTitle': 'AI工具大全 - 全球领先的AI工具聚合平台 | chuansha.tech',
                'siteTitle': 'AI工具大全',
                'siteSlogan': '赛博朋克风AI工具聚合平台',
                'siteSubtitle': '全球领先的AI工具聚合平台，汇集全球最热门的AI工具，为您提供一站式AI解决方案',
                'searchPlaceholder': '搜索AI工具...',
                'searchButton': '搜索AI工具',
                'sortBy': '排序:',
                'sortByName': '按名称',
                'sortByRating': '按评分',
                'sortByCategory': '按类别',
                'allCategories': '全部',
                'textGeneration': '文本生成',
                'imageGeneration': '图像生成',
                'audioTools': '音频工具',
                'videoTools': '视频工具',
                'codingAssistants': '编程助手',
                'contentCreation': '内容创作',
                'businessTools': '商业工具',
                'creativeTools': '创意工具',
                'chineseAi': '国产AI',
                'searchTools': '搜索工具',
                'personalAi': '个人AI助理',
                'githubProjects': 'GitHub热门',
                'clawdhubSkills': 'ClawdHub技能',
                'totalTools': '总数',
                'featured': '推荐',
                'free': '免费版',
                'paid': '付费',
                'visitWebsite': '访问官网',
                'copyLink': '复制链接',
                'total': '总数',
                'textTools': '文本生成',
                'imageTools': '图像生成',
                'githubPopular': 'GitHub热门',
                'clawdHubSkills': 'ClawdHub技能'
            },
            'en': {
                'pageTitle': 'AI Tools Hub - Leading Global AI Tools Aggregation Platform | chuansha.tech',
                'siteTitle': 'AI Tools Hub',
                'siteSlogan': 'Cyberpunk Style AI Tools Aggregation Platform',
                'siteSubtitle': 'Leading global AI tools aggregation platform, collecting the hottest AI tools worldwide, providing you with a one-stop AI solution',
                'searchPlaceholder': 'Search AI Tools...',
                'searchButton': 'Search AI Tools',
                'sortBy': 'Sort By:',
                'sortByName': 'By Name',
                'sortByRating': 'By Rating',
                'sortByCategory': 'By Category',
                'allCategories': 'All',
                'textGeneration': 'Text Generation',
                'imageGeneration': 'Image Generation',
                'audioTools': 'Audio Tools',
                'videoTools': 'Video Tools',
                'codingAssistants': 'Coding Assistants',
                'contentCreation': 'Content Creation',
                'businessTools': 'Business Tools',
                'creativeTools': 'Creative Tools',
                'chineseAi': 'Chinese AI',
                'searchTools': 'Search Tools',
                'personalAi': 'Personal AI Assistant',
                'githubProjects': 'GitHub Popular',
                'clawdhubSkills': 'ClawdHub Skills',
                'totalTools': 'Total',
                'featured': 'Featured',
                'free': 'Free',
                'paid': 'Paid',
                'visitWebsite': 'Visit Website',
                'copyLink': 'Copy Link',
                'total': 'Total',
                'textTools': 'Text Tools',
                'imageTools': 'Image Tools',
                'githubPopular': 'GitHub Popular',
                'clawdHubSkills': 'ClawdHub Skills'
            },
            'ja': {
                'pageTitle': 'AIツールハブ - 世界最先端のAIツール統合プラットフォーム | chuansha.tech',
                'siteTitle': 'AIツールハブ',
                'siteSlogan': 'サイバーパンク風AIツール統合プラットフォーム',
                'siteSubtitle': '世界最先端のAIツール統合プラットフォーム。世界中の人気AIツールを収集し、ワンストップAIソリューションを提供します',
                'searchPlaceholder': 'AIツールを検索...',
                'searchButton': 'AIツールを検索',
                'sortBy': '並び替え:',
                'sortByName': '名前順',
                'sortByRating': '評価順',
                'sortByCategory': 'カテゴリ別',
                'allCategories': 'すべて',
                'textGeneration': '文章生成',
                'imageGeneration': '画像生成',
                'audioTools': '音声ツール',
                'videoTools': '動画ツール',
                'codingAssistants': 'プログラミング支援',
                'contentCreation': 'コンテンツ作成',
                'businessTools': 'ビジネスツール',
                'creativeTools': 'クリエイティブツール',
                'chineseAi': '中国製AI',
                'searchTools': '検索ツール',
                'personalAi': 'パーソナルAIアシスタント',
                'githubProjects': 'GitHub人気',
                'clawdhubSkills': 'ClawdHubスキル',
                'totalTools': '総数',
                'featured': 'おすすめ',
                'free': '無料版',
                'paid': '有料',
                'visitWebsite': '公式サイトへ',
                'copyLink': 'リンクをコピー',
                'total': '総数',
                'textTools': '文章生成',
                'imageTools': '画像生成',
                'githubPopular': 'GitHub人気',
                'clawdHubSkills': 'ClawdHubスキル'
            },
            'ko': {
                'pageTitle': 'AI 툴 허브 - 세계 최고의 AI 툴 통합 플랫폼 | chuansha.tech',
                'siteTitle': 'AI 툴 허브',
                'siteSlogan': '사이버펑크 스타일 AI 툴 통합 플랫폼',
                'siteSubtitle': '세계 최고의 AI 툴 통합 플랫폼. 전 세계 인기 AI 툴을 모아, 원스톱 AI 솔루션을 제공합니다',
                'searchPlaceholder': 'AI 툴 검색...',
                'searchButton': 'AI 툴 검색',
                'sortBy': '정렬:',
                'sortByName': '이름순',
                'sortByRating': '평점순',
                'sortByCategory': '카테고리별',
                'allCategories': '전체',
                'textGeneration': '텍스트 생성',
                'imageGeneration': '이미지 생성',
                'audioTools': '오디오 도구',
                'videoTools': '비디오 도구',
                'codingAssistants': '코딩 보조',
                'contentCreation': '콘텐츠 제작',
                'businessTools': '비즈니스 도구',
                'creativeTools': '창의적 도구',
                'chineseAi': '중국산 AI',
                'searchTools': '검색 도구',
                'personalAi': '개인 AI 어시스턴트',
                'githubProjects': 'GitHub 인기',
                'clawdhubSkills': 'ClawdHub 스킬',
                'totalTools': '총계',
                'featured': '추천',
                'free': '무료',
                'paid': '유료',
                'visitWebsite': '웹사이트 방문',
                'copyLink': '링크 복사',
                'total': '총계',
                'textTools': '텍스트 도구',
                'imageTools': '이미지 도구',
                'githubPopular': 'GitHub 인기',
                'clawdHubSkills': 'ClawdHub 스킬'
            }
        };
        
        // 获取当前语言
        function getCurrentLanguage() {
            // 优先使用URL参数中的语言设置
            const urlParams = new URLSearchParams(window.location.search);
            const urlLang = urlParams.get('lang');
            if (urlLang && translations[urlLang]) {
                return urlLang;
            }
            
            // 其次使用本地存储的语言偏好
            const storedLang = localStorage.getItem('preferredLanguage');
            if (storedLang && translations[storedLang]) {
                return storedLang;
            }
            
            // 最后根据浏览器语言自动选择
            const browserLang = navigator.language || navigator.languages[0];
            if (browserLang.startsWith('zh')) {
                return 'zh-CN';
            } else if (browserLang.startsWith('ja')) {
                return 'ja';
            } else if (browserLang.startsWith('ko')) {
                return 'ko';
            } else {
                return 'en'; // 默认英语
            }
        }
        
        // 翻译页面元素
        function translatePage(lang) {
            // 更新页面标题
            document.title = translations[lang].pageTitle;
            
            // 更新所有带data-i18n属性的元素
            const elements = document.querySelectorAll('[data-i18n]');
            elements.forEach(element => {
                const key = element.getAttribute('data-i18n');
                if (translations[lang][key]) {
                    // 检查是否需要更新placeholder
                    if ((element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') && element.hasAttribute('placeholder')) {
                        element.placeholder = translations[lang][key];
                    } else if (element.hasAttribute('data-i18n-placeholder')) {
                        // 处理data-i18n-placeholder属性
                        const placeholderKey = element.getAttribute('data-i18n-placeholder');
                        if (translations[lang][placeholderKey]) {
                            element.placeholder = translations[lang][placeholderKey];
                        }
                    } else {
                        element.textContent = translations[lang][key];
                    }
                }
            });
            
            // 更新统计标签
            const statLabels = document.querySelectorAll('.stat-label');
            if (statLabels.length >= 4) {
                statLabels[0].textContent = translations[lang].total;
                statLabels[1].textContent = translations[lang].textTools;
                statLabels[2].textContent = translations[lang].githubPopular;
                statLabels[3].textContent = translations[lang].clawdHubSkills;
            }
            
            // 更新分类按钮
            const categoryButtons = document.querySelectorAll('.category-btn');
            categoryButtons.forEach(button => {
                const category = button.getAttribute('data-category');
                const keyMap = {
                    'all': 'allCategories',
                    'text': 'textGeneration',
                    'image': 'imageGeneration',
                    'audio': 'audioTools',
                    'video': 'videoTools',
                    'code': 'codingAssistants',
                    'content': 'contentCreation',
                    'business': 'businessTools',
                    'creative': 'creativeTools',
                    'chinese-ai': 'chineseAi',
                    'search': 'searchTools',
                    'personal-ai': 'personalAi',
                    'github': 'githubProjects',
                    'clawdhub': 'clawdhubSkills'
                };
                
                const translationKey = keyMap[category];
                if (translationKey && translations[lang][translationKey]) {
                    // 保存按钮的当前激活状态
                    const isActive = button.classList.contains('active');
                    
                    // 保留任何现有的HTML子元素（如图标）
                    const existingChildren = [];
                    for (let i = 0; i < button.children.length; i++) {
                        existingChildren.push(button.children[i].cloneNode(true));
                    }
                    
                    // 更新文本内容
                    button.textContent = translations[lang][translationKey];
                    
                    // 重新添加子元素
                    existingChildren.forEach(child => {
                        button.appendChild(child);
                    });
                    
                    // 恢复按钮的激活状态
                    if (isActive) {
                        button.classList.add('active');
                    }
                }
            });
            
            // 更新语言切换器激活状态
            document.querySelectorAll('.lang-option').forEach(option => {
                if (option.getAttribute('data-lang') === lang) {
                    option.classList.add('active');
                } else {
                    option.classList.remove('active');
                }
            });
            
            console.log(`🌍 页面已切换到 ${lang} 语言`);
        }
        
        // 语言切换功能
        function switchLanguage(newLang) {
            if (!translations[newLang]) {
                console.error(`❌ 不支持的语言: ${newLang}`);
                return;
            }
            
            // 保存语言选择到localStorage
            localStorage.setItem('preferredLanguage', newLang);
            
            // 更新URL参数
            const currentUrl = new URL(window.location.href);
            currentUrl.searchParams.set('lang', newLang);
            window.history.pushState({}, '', currentUrl.toString());
            
            // 执行翻译
            translatePage(newLang);
            
            // 如果已有工具数据，重新渲染以应用语言设置
            if (window.currentToolsData) {
                renderTools(window.currentToolsData);
            }
        }
        
        // 获取分类名称（支持多语言）
        function getCategoryNameLocalized(category, lang = null) {
            const currentLang = lang || getCurrentLanguage();
            
            const categoryNames = {
                "text": {
                    "zh-CN": "文本生成",
                    "en": "Text Generation", 
                    "ja": "テキスト生成",
                    "ko": "텍스트 생성"
                },
                "image": {
                    "zh-CN": "图像生成",
                    "en": "Image Generation",
                    "ja": "画像生成", 
                    "ko": "이미지 생성"
                },
                "audio": {
                    "zh-CN": "音频工具",
                    "en": "Audio Tools",
                    "ja": "オーディオツール",
                    "ko": "오디오 도구"
                },
                "video": {
                    "zh-CN": "视频工具",
                    "en": "Video Tools",
                    "ja": "ビデオツール",
                    "ko": "비디오 도구"
                },
                "code": {
                    "zh-CN": "编程助手",
                    "en": "Coding Assistant",
                    "ja": "コーディングアシスタント",
                    "ko": "코딩 어시스턴트"
                },
                "content": {
                    "zh-CN": "内容创作",
                    "en": "Content Creation",
                    "ja": "コンテンツ制作",
                    "ko": "콘텐츠 제작"
                },
                "business": {
                    "zh-CN": "商业工具",
                    "en": "Business Tools",
                    "ja": "ビジネスツール",
                    "ko": "비즈니스 도구"
                },
                "creative": {
                    "zh-CN": "创意工具",
                    "en": "Creative Tools",
                    "ja": "クリエイティブツール",
                    "ko": "크리에이티브 도구"
                },
                "chinese-ai": {
                    "zh-CN": "国产AI",
                    "en": "Chinese AI",
                    "ja": "中国製AI",
                    "ko": "중국산 AI"
                },
                "search": {
                    "zh-CN": "搜索工具",
                    "en": "Search Tools",
                    "ja": "検索ツール",
                    "ko": "검색 도구"
                },
                "personal-ai": {
                    "zh-CN": "个人AI助理",
                    "en": "Personal AI Assistant",
                    "ja": "パーソナルAIアシスタント",
                    "ko": "개인 AI 어시스턴트"
                },
                "github": {
                    "zh-CN": "GitHub热门",
                    "en": "GitHub Popular",
                    "ja": "GitHub人気",
                    "ko": "GitHub 인기"
                },
                "clawdhub": {
                    "zh-CN": "ClawdHub技能",
                    "en": "ClawdHub Skills",
                    "ja": "ClawdHubスキル",
                    "ko": "ClawdHub 스킬"
                },
                "other": {
                    "zh-CN": "全部",
                    "en": "All",
                    "ja": "すべて",
                    "ko": "전체"
                }
            };
            
            return categoryNames[category] && categoryNames[category][currentLang] 
                ? categoryNames[category][currentLang] 
                : category;
        };
        
        // 搜索功能
        function performSearch() {
            const searchTerm = document.getElementById('searchInput') ? document.getElementById('searchInput').value.toLowerCase() : '';
            const allTools = document.querySelectorAll('.tool-card');
            const currentLang = getCurrentLanguage();

            allTools.forEach(tool => {
                const toolName = tool.querySelector('.tool-title') ? tool.querySelector('.tool-title').textContent.toLowerCase() : '';
                const toolDescription = tool.querySelector('.tool-description') ? tool.querySelector('.tool-description').textContent.toLowerCase() : '';
                const toolCategory = tool.getAttribute('data-category') ? tool.getAttribute('data-category').toLowerCase() : '';
                
                // 检查本地化分类名称
                const localizedCategoryName = getCategoryNameLocalized(toolCategory, currentLang).toLowerCase();

                if (
                    toolName.includes(searchTerm) ||
                    toolDescription.includes(searchTerm) ||
                    localizedCategoryName.includes(searchTerm)
                ) {
                    tool.style.display = 'block';
                } else {
                    tool.style.display = 'none';
                }
            });
        };
        
        // 过滤工具
        function filterTools(category) {
            // 更新分类按钮状态
            document.querySelectorAll('.category-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            
            // 找到对应的按钮并激活
            const targetButton = document.querySelector(`.category-btn[data-category="${category}"]`);
            if (targetButton) {
                targetButton.classList.add('active');
            }

            // 过滤工具
            const allTools = document.querySelectorAll('.tool-card');
            allTools.forEach(tool => {
                if (category === 'all' || tool.getAttribute('data-category') === category) {
                    tool.style.display = 'block';
                } else {
                    tool.style.display = 'none';
                }
            });
            
            console.log(`📋 已过滤到分类: ${category}, 显示 ${document.querySelectorAll('.tool-card:not([style*="display: none"])').length} 个工具`);
        };
        
        // 复制链接功能
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(function() {
                const currentLang = getCurrentLanguage();
                const messages = {
                    'zh-CN': '链接已复制到剪贴板！',
                    'en': 'Link copied to clipboard!',
                    'ja': 'リンクをクリップボードにコピーしました！',
                    'ko': '링크가 클립보드에 복사되었습니다!'
                };
                showToast(messages[currentLang] || messages['zh-CN']);
            }).catch(function(err) {
                console.error('复制失败: ', err);
                showToast('复制失败，请手动复制');
            });
        };
        
        // 语言切换功能
        function changeLanguage(lang) {
            switchLanguage(lang);
        }
        
        function getLanguageName(langCode) {
            const languages = {
                'zh-CN': '中文',
                'en': 'English', 
                'ja': '日本語',
                'ko': '한국어'
            };
            return languages[langCode] || langCode;
        }
    </script>
</body>
</html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
    
    def serve_static_file(self, path):
        """提供静态文件服务"""
        # 对于CSS、JS、图片等文件，返回404，因为我们使用内联样式
        self.send_error(404, "Static files not served by this server")
    
    def serve_sitemap(self, path):
        """提供站点地图"""
        sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://chuansha.tech/</loc>
        <lastmod>2026-02-04</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://chuansha.tech/en</loc>
        <lastmod>2026-02-04</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://chuansha.tech/zh-cn</loc>
        <lastmod>2026-02-04</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://chuansha.tech/ja</loc>
        <lastmod>2026-02-04</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://chuansha.tech/ko</loc>
        <lastmod>2026-02-04</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.9</priority>
    </url>
</urlset>"""
        
        self.send_response(200)
        self.send_header('Content-type', 'application/xml')
        self.end_headers()
        self.wfile.write(sitemap_content.encode('utf-8'))
    
    def serve_robots_txt(self):
        """提供robots.txt"""
        robots_content = """User-agent: *
Allow: /
Sitemap: https://chuansha.tech/sitemap.xml"""
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(robots_content.encode('utf-8'))
    
    def send_json_response(self, data):
        """发送JSON响应"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
    
    def send_error(self, code, message):
        """发送错误响应"""
        self.send_response(code)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))


def run_server(port=8094):
    """运行服务器"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, AIToolsHandler)
    print(f"AI工具聚合网站服务器启动在端口 {port}")
    print(f"访问地址: http://localhost:{port}")
    print("按 Ctrl+C 停止服务器")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        httpd.shutdown()


if __name__ == "__main__":
    run_server(8094)