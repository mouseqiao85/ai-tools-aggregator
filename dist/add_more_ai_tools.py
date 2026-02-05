#!/usr/bin/env python3
"""
为AI工具聚合网站添加更多主流AI工具
"""

def add_more_mainstream_ai_tools():
    # 更新HTML页面，添加更多主流AI工具
    enhanced_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title data-i18n="pageTitle">AI工具聚合站 - 发现最强大的AI工具 | chuansha.tech</title>
    <meta name="description" content="全球领先的AI工具聚合平台，汇集ChatGPT、Midjourney、Claude等最热门AI工具，以及GitHub热门项目和ClawdHub技能。提供一站式AI解决方案。">
    <meta name="keywords" content="AI工具,ChatGPT,ClawDBot,个人AI助理,GitHub热门项目,ClawdHub技能,Midjourney,Claude,Stable Diffusion,AI绘画,编程助手,人工智能工具,免费AI工具,AI导航,全球AI,海外AI工具,国际AI平台">
    <meta name="author" content="AI工具聚合站">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="CN">
    <meta name="geo.placename" content="China">
    <meta name="geo.position" content="39.9042;116.4074">
    <meta name="ICBM" content="39.9042, 116.4074">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://chuansha.tech/">
    <meta property="og:title" content="AI工具聚合站 - 发现最强大的AI工具">
    <meta property="og:description" content="全球领先的AI工具聚合平台，汇集ChatGPT、Midjourney、Claude等最热门AI工具，以及GitHub热门项目和ClawdHub技能。">
    <meta property="og:image" content="https://chuansha.tech/images/ai-tools-og.jpg">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:locale:alternate" content="en_US">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="https://chuansha.tech/">
    <meta name="twitter:title" content="AI工具聚合站 - 发现最强大的AI工具">
    <meta name="twitter:description" content="全球领先的AI工具聚合平台，汇集ChatGPT、Midjourney、Claude等最热门AI工具，以及GitHub热门项目和ClawdHub技能">
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
        "name": "AI工具聚合站",
        "alternateName": ["AI Tools Hub", "AI工具中心", "AIツールハブ", "ClawDBot推荐"],
        "url": "https://chuansha.tech/",
        "description": "全球领先的AI工具聚合平台，汇集最热门的AI工具，GitHub热门项目和ClawdHub技能",
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://chuansha.tech/search?q={search_term}",
            "query-input": "required name=search_term"
        },
        "publisher": {
            "@type": "Organization",
            "name": "AI工具聚合站团队",
            "logo": {
                "@type": "ImageObject",
                "url": "https://chuansha.tech/images/logo.png"
            }
        }
    }
    </script>
    
    <link rel="stylesheet" href="css/international-style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+SC:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🤖</text></svg>">
    <link rel="alternate" type="application/rss+xml" title="AI工具聚合站 - 最新AI工具" href="https://chuansha.tech/rss/latest.xml">
</head>
<body>
    <div class="language-switcher">
        <div class="lang-option active" data-lang="zh-CN">中文</div>
        <div class="lang-option" data-lang="en">English</div>
        <div class="lang-option" data-lang="ja">日本語</div>
        <div class="lang-option" data-lang="ko">한국어</div>
    </div>
    
    <div class="container">
        <header>
            <div class="header-content">
                <h1 data-i18n="siteTitle">AI工具聚合站</h1>
                <p class="subtitle" data-i18n="siteSubtitle">发现并使用最强大的人工智能工具，助力您的工作和生活</p>
                
                <div class="clawdbot-promo">
                    <div class="promo-banner">
                        <h3>🤖 推荐：ClawDBot个人AI助理系统</h3>
                        <p>想要一个专属的个人AI助理？ClawDBot是一个功能强大的AI助理系统，可以帮您处理日常任务、管理信息、自动化工作流程。</p>
                        <a href="https://clawdbot.com" target="_blank" class="promo-link">了解更多ClawDBot</a>
                    </div>
                </div>
                
                <div class="social-share">
                    <div class="share-btn" title="分享到Twitter" onclick="shareToSocial('twitter')">🐦</div>
                    <div class="share-btn" title="分享到Facebook" onclick="shareToSocial('facebook')">📘</div>
                    <div class="share-btn" title="分享到LinkedIn" onclick="shareToSocial('linkedin')">👔</div>
                    <div class="share-btn" title="分享到Reddit" onclick="shareToSocial('reddit')">🔺</div>
                </div>
                
                <div class="search-container">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="searchInput" class="search-input" placeholder="搜索AI工具..." autocomplete="off" data-i18n-placeholder="searchPlaceholder">
                </div>
                
                <div class="sort-container">
                    <span class="sort-label" data-i18n="sortBy">排序:</span>
                    <select id="sortSelect" class="sort-select">
                        <option value="name" data-i18n="sortByName">按名称</option>
                        <option value="rating" data-i18n="sortByRating">按评分</option>
                        <option value="category" data-i18n="sortByCategory">按类别</option>
                    </select>
                </div>
                
                <div class="stats-container">
                    <div class="stat-item">
                        <span class="stat-number" id="totalTools">43</span>
                        <span class="stat-label" data-i18n="totalTools">总数</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-number" id="aiTools">23</span>
                        <span class="stat-label">AI工具</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-number" id="githubProjects">10</span>
                        <span class="stat-label">GitHub项目</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-number" id="clawdSkills">10</span>
                        <span class="stat-label">ClawdHub技能</span>
                    </div>
                </div>
                
                <div class="category-nav">
                    <button class="category-btn active" data-category="all" data-i18n="allCategories">全部</button>
                    <button class="category-btn" data-category="text" data-i18n="textGeneration">文本生成</button>
                    <button class="category-btn" data-category="image" data-i18n="imageGeneration">图像生成</button>
                    <button class="category-btn" data-category="audio" data-i18n="audioTools">音频工具</button>
                    <button class="category-btn" data-category="video" data-i18n="videoTools">视频工具</button>
                    <button class="category-btn" data-category="code" data-i18n="codingAssistants">编程助手</button>
                    <button class="category-btn" data-category="content" data-i18n="contentCreation">内容创作</button>
                    <button class="category-btn" data-category="business" data-i18n="businessTools">商业工具</button>
                    <button class="category-btn" data-category="creative" data-i18n="creativeTools">创意工具</button>
                    <button class="category-btn" data-category="personal-ai" data-i18n="personalAi">个人AI助理</button>
                    <button class="category-btn" data-category="github" data-i18n="githubProjects">GitHub热门</button>
                    <button class="category-btn" data-category="clawdhub" data-i18n="clawdhubSkills">ClawdHub技能</button>
                    <button class="category-btn" data-category="search" data-i18n="searchTools">搜索工具</button>
                </div>
            </div>
        </header>
        
        <main>
            <div class="tools-grid" id="toolsGrid">
                <!-- Personal AI Assistant Category -->
                <div class="tool-card" data-category="personal-ai" data-rating="5" data-free="false">
                    <span class="featured-badge" data-i18n="featured">推荐</span>
                    <span class="tool-category" data-i18n="personalAi">个人AI助理</span>
                    <h3 class="tool-title">ClawDBot</h3>
                    <p class="tool-description" data-i18n="clawdbotDescription">ClawDBot是一个功能强大的个人AI助理系统，能够帮您处理日常任务、管理信息、自动化工作流程。支持多种通信渠道，包括Telegram、WhatsApp、Signal等，可以成为您的专属AI助手，提升工作效率和生活品质。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.9/5</span>
                    </div>
                    <div>
                        <a href="https://clawdbot.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <!-- Text Generation Tools -->
                <div class="tool-card" data-category="text" data-rating="5" data-free="true">
                    <span class="featured-badge" data-i18n="featured">推荐</span>
                    <span class="tool-category" data-i18n="textGeneration">文本生成</span>
                    <h3 class="tool-title">ChatGPT</h3>
                    <p class="tool-description" data-i18n="chatgptDescription">OpenAI开发的高级对话AI，能够回答问题、创作文字、编程等。强大的自然语言理解和生成能力，适用于各种文本创作场景。拥有GPT-4 Turbo等先进模型。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.9/5</span>
                    </div>
                    <div>
                        <a href="https://chat.openai.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="free-tag" data-i18n="free">免费版</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="text" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="textGeneration">文本生成</span>
                    <h3 class="tool-title">Claude</h3>
                    <p class="tool-description" data-i18n="claudeDescription">Anthropic公司开发的AI助手，专注于安全和有用性。具有出色的长文本生成和对话能力，特别适合需要安全性和可靠性的场景。支持长达100K tokens的上下文。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.7/5</span>
                    </div>
                    <div>
                        <a href="https://claude.ai" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="free-tag" data-i18n="free">免费版</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="text" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="textGeneration">文本生成</span>
                    <h3 class="tool-title">Gemini</h3>
                    <p class="tool-description" data-i18n="geminiDescription">Google开发的多模态AI模型，能够处理文本、图像、音频、视频和代码。强大的多模态理解和生成能力，结合Google搜索能力，提供准确的信息。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.6/5</span>
                    </div>
                    <div>
                        <a href="https://gemini.google.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="text" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="textGeneration">文本生成</span>
                    <h3 class="tool-title">ChatGPT Edu</h3>
                    <p class="tool-description" data-i18n="chatgpteudDescription">OpenAI为教育机构推出的ChatGPT版本，专为学生和教师设计。提供安全的学习环境，帮助提高教学效率和学习成果。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.5/5</span>
                    </div>
                    <div>
                        <a href="https://edu.openai.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="text" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="textGeneration">文本生成</span>
                    <h3 class="tool-title">Microsoft Copilot</h3>
                    <p class="tool-description" data-i18n="copilotDescription">Microsoft开发的AI助手，集成在Office 365、Windows和其他Microsoft产品中。提供生产力增强功能，帮助用户更高效地完成工作任务。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.4/5</span>
                    </div>
                    <div>
                        <a href="https://www.microsoft.com/copilot" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="text" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="textGeneration">文本生成</span>
                    <h3 class="tool-title">HuggingChat</h3>
                    <p class="tool-description" data-i18n="huggingchatDescription">Hugging Face推出的开源聊天界面，提供对多种开源模型的访问。用户可以选择不同的模型进行对话，支持隐私保护的聊天体验。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.3/5</span>
                    </div>
                    <div>
                        <a href="https://huggingface.co/chat" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="free-tag" data-i18n="free">免费版</span>
                    </div>
                </div>
                
                <!-- Image Generation Tools -->
                <div class="tool-card" data-category="image" data-rating="5" data-free="false">
                    <span class="tool-category" data-i18n="imageGeneration">图像生成</span>
                    <h3 class="tool-title">Midjourney</h3>
                    <p class="tool-description" data-i18n="midjourneyDescription">强大的AI图像生成工具，能够根据文本描述生成精美图像。以其艺术风格和高质量图像著称，是创意工作者的首选工具。支持多种艺术风格和参数调整。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.8/5</span>
                    </div>
                    <div>
                        <a href="https://www.midjourney.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="image" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="imageGeneration">图像生成</span>
                    <h3 class="tool-title">DALL-E 3</h3>
                    <p class="tool-description" data-i18n="dalle3Description">OpenAI的最新图像生成AI，能够创建高质量图像。与ChatGPT深度集成，提供精确的图像生成控制。支持文本到图像的直接转换。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.6/5</span>
                    </div>
                    <div>
                        <a href="https://openai.com/dall-e-3" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="image" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="imageGeneration">图像生成</span>
                    <h3 class="tool-title">Stable Diffusion</h3>
                    <p class="tool-description" data-i18n="stablediffusionDescription">开源的AI图像生成模型，可在本地运行。提供最大的自定义灵活性，支持各种风格和参数调整。社区活跃，插件丰富。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.5/5</span>
                    </div>
                    <div>
                        <a href="https://stability.ai/stable-diffusion" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="free-tag" data-i18n="free">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="image" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="imageGeneration">图像生成</span>
                    <h3 class="tool-title">Adobe Firefly</h3>
                    <p class="tool-description" data-i18n="fireflyDescription">Adobe开发的AI创意工具，集成在Photoshop和其他Creative Cloud应用中。提供专业的图像生成和编辑功能，适合设计师使用。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.4/5</span>
                    </div>
                    <div>
                        <a href="https://www.adobe.com/firefly" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="image" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="imageGeneration">图像生成</span>
                    <h3 class="tool-title">Leonardo AI</h3>
                    <p class="tool-description" data-i18n="leonardodescription">AI图像和视频生成平台，适合创意项目。提供高质量的艺术风格生成和视频制作能力。支持游戏开发资产生成。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">☆</div>
                        </div>
                        <span>4.4/5</span>
                    </div>
                    <div>
                        <a href="https://leonardo.ai" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <!-- Audio Tools -->
                <div class="tool-card" data-category="audio" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="audioTools">音频工具</span>
                    <h3 class="tool-title">ElevenLabs</h3>
                    <p class="tool-description" data-i18n="elevenlabsDescription">AI语音合成工具，能够创建逼真的语音。提供多种声音选择，支持文本转语音，广泛应用于播客、视频解说等领域。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.6/5</span>
                    </div>
                    <div>
                        <a href="https://elevenlabs.io" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="audio" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="audioTools">音频工具</span>
                    <h3 class="tool-title">Descript</h3>
                    <p class="tool-description" data-i18n="descriptDescription">音频和视频编辑工具，提供AI驱动的转录、编辑和合成功能。可以像编辑文本一样编辑音频和视频，简化创作流程。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.3/5</span>
                    </div>
                    <div>
                        <a href="https://www.descript.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="free-tag" data-i18n="free">免费版</span>
                    </div>
                </div>
                
                <!-- Video Tools -->
                <div class="tool-card" data-category="video" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="videoTools">视频工具</span>
                    <h3 class="tool-title">Runway ML</h3>
                    <p class="tool-description" data-i18n="runwaymlDescription">创意AI工具平台，提供视频编辑、图像生成等功能。专注于创意专业人士，提供先进的AI创意工具。支持绿幕移除、视频稳定等功能。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">★</div>
                        </div>
                        <span>4.6/5</span>
                    </div>
                    <div>
                        <a href="https://runwayml.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="video" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="videoTools">视频工具</span>
                    <h3 class="tool-title">Synthesia</h3>
                    <p class="tool-description" data-i18n="synthesiaDescription">AI虚拟主播平台，可以创建专业的企业培训和营销视频。无需摄像设备和演播室，快速生成个性化视频内容。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">☆</div>
                        </div>
                        <span>4.5/5</span>
                    </div>
                    <div>
                        <a href="https://www.synthesia.io" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <!-- Coding Tools -->
                <div class="tool-card" data-category="code" data-rating="5" data-free="false">
                    <span class="tool-category" data-i18n="codingAssistants">编程助手</span>
                    <h3 class="tool-title">GitHub Copilot</h3>
                    <p class="tool-description" data-i18n="copilotDescription">AI编程助手，帮助开发者更快地编写代码。支持多种编程语言，提供智能代码补全和建议。基于GPT-4技术，集成在主流IDE中。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.7/5</span>
                    </div>
                    <div>
                        <a href="https://copilot.github.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="code" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="codingAssistants">编程助手</span>
                    <h3 class="tool-title">Amazon CodeWhisperer</h3>
                    <p class="tool-description" data-i18n="codewhispererDescription">Amazon开发的AI编程助手，提供代码建议和自动补全功能。支持多种编程语言，集成在主流IDE中，提高开发效率。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.4/5</span>
                    </div>
                    <div>
                        <a href="https://aws.amazon.com/codewhisperer" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="free-tag" data-i18n="free">免费版</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="code" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="codingAssistants">编程助手</span>
                    <h3 class="tool-title">Tabnine</h3>
                    <p class="tool-description" data-i18n="tabnineDescription">AI驱动的代码自动补全工具，支持多种编程语言和IDE。提供智能代码建议，提高编码效率和准确性。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.3/5</span>
                    </div>
                    <div>
                        <a href="https://www.tabnine.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="free-tag" data-i18n="free">免费版</span>
                    </div>
                </div>
                
                <!-- Business Tools -->
                <div class="tool-card" data-category="business" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="businessTools">商业工具</span>
                    <h3 class="tool-title">Salesforce Einstein</h3>
                    <p class="tool-description" data-i18n="salesforceDescription">Salesforce集成的AI功能，提供预测分析、自动化和个性化功能。帮助企业更好地了解客户，提高销售和营销效率。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.5/5</span>
                    </div>
                    <div>
                        <a href="https://www.salesforce.com/einstein" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="business" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="businessTools">商业工具</span>
                    <h3 class="tool-title">IBM Watson</h3>
                    <p class="tool-description" data-i18n="watsonDescription">IBM的AI平台，提供认知计算、机器学习和自然语言处理功能。广泛应用于企业级AI解决方案，支持多种行业应用场景。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.4/5</span>
                    </div>
                    <div>
                        <a href="https://www.ibm.com/watson" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <!-- Content Creation Tools -->
                <div class="tool-card" data-category="content" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="contentCreation">内容创作</span>
                    <h3 class="tool-title">Jasper</h3>
                    <p class="tool-description" data-i18n="jasperDescription">AI内容创作工具，帮助撰写营销文案、博客等。提供多种内容模板，适合营销和内容创作者。具备品牌声音功能，保持内容一致性。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.4/5</span>
                    </div>
                    <div>
                        <a href="https://www.jasper.ai" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="content" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="contentCreation">内容创作</span>
                    <h3 class="tool-title">Notion AI</h3>
                    <p class="tool-description" data-i18n="notionaiDescription">集成在Notion中的AI功能，帮助写作、总结、翻译等。与工作空间无缝集成，提升工作效率。支持多种语言，功能丰富。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">☆</div>
                        </div>
                        <span>4.2/5</span>
                    </div>
                    <div>
                        <a href="https://www.notion.so/product/ai" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="content" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="contentCreation">内容创作</span>
                    <h3 class="tool-title">Writesonic</h3>
                    <p class="tool-description" data-i18n="writesonicDescription">AI内容创作工具，帮助撰写广告文案、博客文章、社交媒体内容等。提供多种内容模板和创作工具，适合营销人员和内容创作者。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.3/5</span>
                    </div>
                    <div>
                        <a href="https://writesonic.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <!-- Creative Tools -->
                <div class="tool-card" data-category="creative" data-rating="5" data-free="false">
                    <span class="tool-category" data-i18n="creativeTools">创意工具</span>
                    <h3 class="tool-title">Adobe Sensei</h3>
                    <p class="tool-description" data-i18n="senseiDescription">Adobe Creative Cloud中的AI功能集合，提供智能图像编辑、内容识别、自动修复等功能。集成在Photoshop、Premiere Pro等应用中，提升创意工作效率。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">★</div>
                        </div>
                        <span>4.7/5</span>
                    </div>
                    <div>
                        <a href="https://www.adobe.com/sensei" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="creative" data-rating="4" data-free="false">
                    <span class="tool-category" data-i18n="creativeTools">创意工具</span>
                    <h3 class="tool-title">Canva AI</h3>
                    <p class="tool-description" data-i18n="canvaDescription">Canva中的AI功能，提供智能设计建议、背景移除、文本生成等功能。帮助用户快速创建专业设计，无需设计经验。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">☆</div>
                        </div>
                        <span>4.5/5</span>
                    </div>
                    <div>
                        <a href="https://www.canva.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="paid-tag" data-i18n="paid">付费</span>
                    </div>
                </div>
                
                <!-- Search Tools -->
                <div class="tool-card" data-category="search" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="searchTools">搜索工具</span>
                    <h3 class="tool-title">Perplexity AI</h3>
                    <p class="tool-description" data-i18n="perplexityDescription">AI驱动的搜索引擎，提供准确的信息查询。结合搜索和AI的优势，提供引用来源的准确答案。支持专业模式和研究模式。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">☆</div>
                        </div>
                        <span>4.3/5</span>
                    </div>
                    <div>
                        <a href="https://www.perplexity.ai" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="free-tag" data-i18n="free">免费版</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="search" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="searchTools">搜索工具</span>
                    <h3 class="tool-title">You.com</h3>
                    <p class="tool-description" data-i18n="youDescription">AI驱动的搜索平台，提供个性化搜索结果。整合多种信息源，提供更相关和有用的搜索结果，保护用户隐私。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">★</div><div class="star">☆</div>
                        </div>
                        <span>4.2/5</span>
                    </div>
                    <div>
                        <a href="https://you.com" target="_blank" class="tool-link" data-i18n="visitWebsite">访问官网</a>
                        <span class="free-tag" data-i18n="free">免费版</span>
                    </div>
                </div>
                
                <!-- GitHub Top Projects -->
                <div class="tool-card" data-category="github" data-rating="5" data-free="true">
                    <span class="featured-badge">⭐</span>
                    <span class="tool-category" data-i18n="githubProjects">GitHub热门</span>
                    <h3 class="tool-title">moltbot/moltbot</h3>
                    <p class="tool-description" data-i18n="githubProjectDescription">Moltbot是一个先进的AI代理框架，支持多通道通信、智能决策和自动化工作流。具有强大的扩展能力和灵活的配置选项。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.8/5</span>
                    </div>
                    <div>
                        <a href="https://github.com/moltbot/moltbot" target="_blank" class="tool-link">GitHub访问</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="github" data-rating="5" data-free="true">
                    <span class="tool-category" data-i18n="githubProjects">GitHub热门</span>
                    <h3 class="tool-title">microsoft/autogen</h3>
                    <p class="tool-description">AutoGen是一个用于下一代大语言模型应用的框架，支持多代理对话、工具集成和复杂工作流编排。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.7/5</span>
                    </div>
                    <div>
                        <a href="https://github.com/microsoft/autogen" target="_blank" class="tool-link">GitHub访问</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="github" data-rating="5" data-free="true">
                    <span class="tool-category" data-i18n="githubProjects">GitHub热门</span>
                    <h3 class="tool-title">langchain-ai/langchain</h3>
                    <p class="tool-description">LangChain是一个用于开发由LLM驱动的应用程序的框架，提供数据连接、代理和工具等功能。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.6/5</span>
                    </div>
                    <div>
                        <a href="https://github.com/langchain-ai/langchain" target="_blank" class="tool-link">GitHub访问</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="github" data-rating="5" data-free="true">
                    <span class="tool-category" data-i18n="githubProjects">GitHub热门</span>
                    <h3 class="tool-title">openai/openai-python</h3>
                    <p class="tool-description">OpenAI官方Python库，提供简单易用的API接口，支持ChatGPT、DALL-E等模型调用。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.5/5</span>
                    </div>
                    <div>
                        <a href="https://github.com/openai/openai-python" target="_blank" class="tool-link">GitHub访问</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="github" data-rating="5" data-free="true">
                    <span class="tool-category" data-i18n="githubProjects">GitHub热门</span>
                    <h3 class="tool-title">huggingface/transformers</h3>
                    <p class="tool-description">Transformers是Hugging Face提供的最先进的预训练模型库，支持NLP、计算机视觉等多个领域。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.9/5</span>
                    </div>
                    <div>
                        <a href="https://github.com/huggingface/transformers" target="_blank" class="tool-link">GitHub访问</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="github" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="githubProjects">GitHub热门</span>
                    <h3 class="tool-title">mem0ai/mem0</h3>
                    <p class="tool-description">Mem0是下一代内存层，允许应用程序为用户提供个性化的AI体验，记住用户偏好和历史。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.4/5</span>
                    </div>
                    <div>
                        <a href="https://github.com/mem0ai/mem0" target="_blank" class="tool-link">GitHub访问</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="github" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="githubProjects">GitHub热门</span>
                    <h3 class="tool-title">continuedev/continue</h3>
                    <p class="tool-description">Continue是一个VS Code和JetBrains插件，使您能够在IDE中使用ChatGPT、Claude等模型进行编程。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.3/5</span>
                    </div>
                    <div>
                        <a href="https://github.com/continuedev/continue" target="_blank" class="tool-link">GitHub访问</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="github" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="githubProjects">GitHub热门</span>
                    <h3 class="tool-title">lobehub/lobe-chat</h3>
                    <p class="tool-description">Lobe Chat是一个开源的、可扩展的、高性能的聊天机器人框架，支持多种AI模型和插件。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.2/5</span>
                    </div>
                    <div>
                        <a href="https://github.com/lobehub/lobe-chat" target="_blank" class="tool-link">GitHub访问</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="github" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="githubProjects">GitHub热门</span>
                    <h3 class="tool-title">AgentOps-AI/agentops</h3>
                    <p class="tool-description">AgentOps是一个用于LLM应用的全栈式可观测性和分析平台，帮助调试和优化AI代理。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.1/5</span>
                    </div>
                    <div>
                        <a href="https://github.com/AgentOps-AI/agentops" target="_blank" class="tool-link">GitHub访问</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="github" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="githubProjects">GitHub热门</span>
                    <h3 class="tool-title">janhq/jan</h3>
                    <p class="tool-description">Jan是一个桌面AI套件，使AI模型可以在本地运行，提供离线AI功能和数据隐私保护。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.0/5</span>
                    </div>
                    <div>
                        <a href="https://github.com/janhq/jan" target="_blank" class="tool-link">GitHub访问</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <!-- ClawdHub Skills -->
                <div class="tool-card" data-category="clawdhub" data-rating="5" data-free="true">
                    <span class="featured-badge">🛠️</span>
                    <span class="tool-category" data-i18n="clawdhubSkills">ClawdHub技能</span>
                    <h3 class="tool-title">clawdhub-weather</h3>
                    <p class="tool-description" data-i18n="clawdhubSkillDescription">天气查询技能，提供实时天气信息、预报和气象数据，支持全球多个城市和地区。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.8/5</span>
                    </div>
                    <div>
                        <a href="https://clawdhub.com/skills/weather" target="_blank" class="tool-link">查看详情</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="clawdhub" data-rating="5" data-free="true">
                    <span class="tool-category" data-i18n="clawdhubSkills">ClawdHub技能</span>
                    <h3 class="tool-title">clawdhub-github</h3>
                    <p class="tool-description">GitHub集成技能，支持仓库管理、PR操作、Issue跟踪等功能，方便开发者管理GitHub项目。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.7/5</span>
                    </div>
                    <div>
                        <a href="https://clawdhub.com/skills/github" target="_blank" class="tool-link">查看详情</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="clawdhub" data-rating="5" data-free="true">
                    <span class="tool-category" data-i18n="clawdhubSkills">ClawdHub技能</span>
                    <h3 class="tool-title">clawdhub-google-search</h3>
                    <p class="tool-description">Google搜索技能，提供实时网络搜索功能，获取最新信息和网页内容，支持多语言搜索。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.6/5</span>
                    </div>
                    <div>
                        <a href="https://clawdhub.com/skills/google-search" target="_blank" class="tool-link">查看详情</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="clawdhub" data-rating="5" data-free="true">
                    <span class="tool-category" data-i18n="clawdhubSkills">ClawdHub技能</span>
                    <h3 class="tool-title">clawdhub-file-manager</h3>
                    <p class="tool-description">文件管理技能，支持文件上传、下载、搜索、组织等功能，方便管理各种文档和资源。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.5/5</span>
                    </div>
                    <div>
                        <a href="https://clawdhub.com/skills/file-manager" target="_blank" class="tool-link">查看详情</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="clawdhub" data-rating="5" data-free="true">
                    <span class="tool-category" data-i18n="clawdhubSkills">ClawdHub技能</span>
                    <h3 class="tool-title">clawdhub-calendar</h3>
                    <p class="tool-description">日历集成技能，支持事件管理、提醒设置、日程安排等功能，与Google Calendar等服务同步。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span>
                        </div>
                        <span>4.4/5</span>
                    </div>
                    <div>
                        <a href="https://clawdhub.com/skills/calendar" target="_blank" class="tool-link">查看详情</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="clawdhub" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="clawdhubSkills">ClawdHub技能</span>
                    <h3 class="tool-title">clawdhub-email</h3>
                    <p class="tool-description">邮件集成技能，支持收发邮件、邮件模板、自动回复等功能，与Gmail等邮箱服务集成。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.3/5</span>
                    </div>
                    <div>
                        <a href="https://clawdhub.com/skills/email" target="_blank" class="tool-link">查看详情</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="clawdhub" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="clawdhubSkills">ClawdHub技能</span>
                    <h3 class="tool-title">clawdhub-notion</h3>
                    <p class="tool-description">Notion集成技能，支持页面创建、数据库管理、内容同步等功能，方便管理Notion工作区。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.2/5</span>
                    </div>
                    <div>
                        <a href="https://clawdhub.com/skills/notion" target="_blank" class="tool-link">查看详情</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="clawdhub" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="clawdhubSkills">ClawdHub技能</span>
                    <h3 class="tool-title">clawdhub-web-browser</h3>
                    <p class="tool-description">网页浏览技能，支持网页内容提取、信息抓取、网页分析等功能，提供浏览器自动化能力。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.1/5</span>
                    </div>
                    <div>
                        <a href="https://clawdhub.com/skills/web-browser" target="_blank" class="tool-link">查看详情</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="clawdhub" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="clawdhubSkills">ClawdHub技能</span>
                    <h3 class="tool-title">clawdhub-image-analyzer</h3>
                    <p class="tool-description">图像分析技能，支持图像识别、OCR文字提取、图像内容分析等功能，处理各种图像格式。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.0/5</span>
                    </div>
                    <div>
                        <a href="https://clawdhub.com/skills/image-analyzer" target="_blank" class="tool-link">查看详情</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
                
                <div class="tool-card" data-category="clawdhub" data-rating="4" data-free="true">
                    <span class="tool-category" data-i18n="clawdhubSkills">ClawdHub技能</span>
                    <h3 class="tool-title">clawdhub-document-processor</h3>
                    <p class="tool-description">文档处理技能，支持PDF、Word、Excel等格式文档的读取、分析和处理，提取关键信息。</p>
                    <div class="rating">
                        <div class="rating-stars">
                            <span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">☆</span>
                        </div>
                        <span>4.0/5</span>
                    </div>
                    <div>
                        <a href="https://clawdhub.com/skills/document-processor" target="_blank" class="tool-link">查看详情</a>
                        <span class="free-tag">免费</span>
                    </div>
                </div>
            </div>
        </main>
        
        <footer>
            <div class="footer-links">
                <a href="https://chuansha.tech/about" class="footer-link" data-i18n="aboutUs">关于我们</a>
                <a href="https://chuansha.tech/contact" class="footer-link" data-i18n="contactUs">联系我们</a>
                <a href="https://chuansha.tech/privacy" class="footer-link" data-i18n="privacyPolicy">隐私政策</a>
                <a href="https://chuansha.tech/terms" class="footer-link" data-i18n="termsOfService">使用条款</a>
                <a href="https://chuansha.tech/sitemap" class="footer-link" data-i18n="sitemap">网站地图</a>
                <a href="https://chuansha.tech/api" class="footer-link" data-i18n="apiDocs">API文档</a>
            </div>
            <p data-i18n="copyright">© 2026 AI工具聚合站 - 发现并使用最好的AI工具</p>
            <p data-i18n="disclaimer">免责声明：本网站仅为AI工具导航，不提供任何AI服务</p>
            <p data-i18n="currentDomain">当前域名: http://8.215.63.182:8094 | 正式域名: https://chuansha.tech</p>
        </footer>
        
        <button id="backToTop" class="back-to-top">↑</button>
    </div>
    
    <!-- Tool Detail Modal -->
    <div id="toolModal" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <h2 class="modal-title" data-i18n="toolDetails">工具详情</h2>
            <p class="modal-description">工具详细信息将在这里显示。</p>
            <div class="modal-details">
                <p><strong data-i18n="category">类别:</strong> <span id="modalCategory"></span></p>
                <p><strong data-i18n="rating">评分:</strong> <span id="modalRating"></span></p>
                <p><strong data-i18n="pricing">费用:</strong> <span id="modalFreeStatus"></span></p>
            </div>
            <div class="modal-actions">
                <a href="#" id="modalLink" class="tool-link" target="_blank" data-i18n="visitWebsite">访问官网</a>
            </div>
        </div>
    </div>
    
    <script>
        // 国际化功能JavaScript
        const translations = {
            'zh-CN': {
                pageTitle: 'AI工具聚合站 - 发现最强大的AI工具 | ClawDBot推荐',
                siteTitle: 'AI工具聚合站',
                siteSubtitle: '发现并使用最强大的人工智能工具，助力您的工作和生活',
                searchPlaceholder: '搜索AI工具...',
                sortBy: '排序:',
                sortByName: '按名称',
                sortByRating: '按评分',
                sortByCategory: '按类别',
                allCategories: '全部',
                textGeneration: '文本生成',
                imageGeneration: '图像生成',
                audioTools: '音频工具',
                videoTools: '视频工具',
                codingAssistants: '编程助手',
                contentCreation: '内容创作',
                businessTools: '商业工具',
                creativeTools: '创意工具',
                personalAi: '个人AI助理',
                githubProjects: 'GitHub热门',
                clawdhubSkills: 'ClawdHub技能',
                searchTools: '搜索工具',
                featured: '推荐',
                visitWebsite: '访问官网',
                free: '免费版',
                paid: '付费',
                totalTools: '工具总数',
                freeTools: '免费工具',
                categories: '分类',
                aboutUs: '关于我们',
                contactUs: '联系我们',
                privacyPolicy: '隐私政策',
                termsOfService: '使用条款',
                sitemap: '网站地图',
                apiDocs: 'API文档',
                copyright: '© 2026 AI工具聚合站 - 发现并使用最好的AI工具',
                disclaimer: '免责声明：本网站仅为AI工具导航，不提供任何AI服务',
                currentDomain: '当前域名: http://8.215.63.182:8094 | 正式域名: https://chuansha.tech',
                toolDetails: '工具详情',
                category: '类别:',
                rating: '评分:',
                pricing: '费用:',
                clawdbotDescription: 'ClawDBot是一个功能强大的个人AI助理系统，能够帮您处理日常任务、管理信息、自动化工作流程。支持多种通信渠道，包括Telegram、WhatsApp、Signal等，可以成为您的专属AI助手，提升工作效率和生活品质。',
                githubProjectDescription: 'GitHub热门项目描述',
                clawdhubSkillDescription: 'ClawdHub技能描述',
                chatgptDescription: 'OpenAI开发的高级对话AI，能够回答问题、创作文字、编程等。强大的自然语言理解和生成能力，适用于各种文本创作场景。拥有GPT-4 Turbo等先进模型。',
                claudeDescription: 'Anthropic公司开发的AI助手，专注于安全和有用性。具有出色的长文本生成和对话能力，特别适合需要安全性和可靠性的场景。支持长达100K tokens的上下文。',
                geminiDescription: 'Google开发的多模态AI模型，能够处理文本、图像、音频、视频和代码。强大的多模态理解和生成能力，结合Google搜索能力，提供准确的信息。',
                chatgpteudDescription: 'OpenAI为教育机构推出的ChatGPT版本，专为学生和教师设计。提供安全的学习环境，帮助提高教学效率和学习成果。',
                copilotDescription: 'Microsoft开发的AI助手，集成在Office 365、Windows和其他Microsoft产品中。提供生产力增强功能，帮助用户更高效地完成工作任务。',
                huggingchatDescription: 'Hugging Face推出的开源聊天界面，提供对多种开源模型的访问。用户可以选择不同的模型进行对话，支持隐私保护的聊天体验。',
                midjourneyDescription: '强大的AI图像生成工具，能够根据文本描述生成精美图像。以其艺术风格和高质量图像著称，是创意工作者的首选工具。支持多种艺术风格和参数调整。',
                dalle3Description: 'OpenAI的最新图像生成AI，能够创建高质量图像。与ChatGPT深度集成，提供精确的图像生成控制。支持文本到图像的直接转换。',
                stablediffusionDescription: '开源的AI图像生成模型，可在本地运行。提供最大的自定义灵活性，支持各种风格和参数调整。社区活跃，插件丰富。',
                fireflyDescription: 'Adobe开发的AI创意工具，集成在Photoshop和其他Creative Cloud应用中。提供专业的图像生成和编辑功能，适合设计师使用。',
                leonardodescription: 'AI图像和视频生成平台，适合创意项目。提供高质量的艺术风格生成和视频制作能力。支持游戏开发资产生成。',
                elevenlabsDescription: 'AI语音合成工具，能够创建逼真的语音。提供多种声音选择，支持文本转语音，广泛应用于播客、视频解说等领域。',
                descriptDescription: '音频和视频编辑工具，提供AI驱动的转录、编辑和合成功能。可以像编辑文本一样编辑音频和视频，简化创作流程。',
                runwaymlDescription: '创意AI工具平台，提供视频编辑、图像生成等功能。专注于创意专业人士，提供先进的AI创意工具。支持绿幕移除、视频稳定等功能。',
                synthesiaDescription: 'AI虚拟主播平台，可以创建专业的企业培训和营销视频。无需摄像设备和演播室，快速生成个性化视频内容。',
                codewhispererDescription: 'Amazon开发的AI编程助手，提供代码建议和自动补全功能。支持多种编程语言，集成在主流IDE中，提高开发效率。',
                tabnineDescription: 'AI驱动的代码自动补全工具，支持多种编程语言和IDE。提供智能代码建议，提高编码效率和准确性。',
                salesforceDescription: 'Salesforce集成的AI功能，提供预测分析、自动化和个性化功能。帮助企业更好地了解客户，提高销售和营销效率。',
                watsonDescription: 'IBM的AI平台，提供认知计算、机器学习和自然语言处理功能。广泛应用于企业级AI解决方案，支持多种行业应用场景。',
                jasperDescription: 'AI内容创作工具，帮助撰写营销文案、博客等。提供多种内容模板，适合营销和内容创作者。具备品牌声音功能，保持内容一致性。',
                notionaiDescription: '集成在Notion中的AI功能，帮助写作、总结、翻译等。与工作空间无缝集成，提升工作效率。支持多种语言，功能丰富。',
                writesonicDescription: 'AI内容创作工具，帮助撰写广告文案、博客文章、社交媒体内容等。提供多种内容模板和创作工具，适合营销人员和内容创作者。',
                senseiDescription: 'Adobe Creative Cloud中的AI功能集合，提供智能图像编辑、内容识别、自动修复等功能。集成在Photoshop、Premiere Pro等应用中，提升创意工作效率。',
                canvaDescription: 'Canva中的AI功能，提供智能设计建议、背景移除、文本生成等功能。帮助用户快速创建专业设计，无需设计经验。',
                perplexityDescription: 'AI驱动的搜索引擎，提供准确的信息查询。结合搜索和AI的优势，提供引用来源的准确答案。支持专业模式和研究模式。',
                youDescription: 'AI驱动的搜索平台，提供个性化搜索结果。整合多种信息源，提供更相关和有用的搜索结果，保护用户隐私。'
            },
            'en': {
                pageTitle: 'AI Tools Hub - Discover the Most Powerful AI Tools | Recommended by ClawDBot',
                siteTitle: 'AI Tools Hub',
                siteSubtitle: 'Discover and use the most powerful AI tools to enhance your work and life',
                searchPlaceholder: 'Search AI tools...',
                sortBy: 'Sort by:',
                sortByName: 'Name',
                sortByRating: 'Rating',
                sortByCategory: 'Category',
                allCategories: 'All',
                textGeneration: 'Text Generation',
                imageGeneration: 'Image Generation',
                audioTools: 'Audio Tools',
                videoTools: 'Video Tools',
                codingAssistants: 'Coding Assistants',
                contentCreation: 'Content Creation',
                businessTools: 'Business Tools',
                creativeTools: 'Creative Tools',
                personalAi: 'Personal AI Assistant',
                githubProjects: 'GitHub Popular',
                clawdhubSkills: 'ClawdHub Skills',
                searchTools: 'Search Tools',
                featured: 'Featured',
                visitWebsite: 'Visit Website',
                free: 'Free Tier',
                paid: 'Paid',
                totalTools: 'Total Tools',
                freeTools: 'Free Tools',
                categories: 'Categories',
                aboutUs: 'About Us',
                contactUs: 'Contact Us',
                privacyPolicy: 'Privacy Policy',
                termsOfService: 'Terms of Service',
                sitemap: 'Sitemap',
                apiDocs: 'API Documentation',
                copyright: '© 2026 AI Tools Hub - Discover and use the best AI tools',
                disclaimer: 'Disclaimer: This website is only an AI tools directory and does not provide any AI services',
                currentDomain: 'Current Domain: http://8.215.63.182:8094 | Official Domain: https://chuansha.tech',
                toolDetails: 'Tool Details',
                category: 'Category:',
                rating: 'Rating:',
                pricing: 'Pricing:',
                clawdbotDescription: 'ClawDBot is a powerful personal AI assistant system that can help you handle daily tasks, manage information, and automate workflows. It supports multiple communication channels including Telegram, WhatsApp, Signal, etc., and can become your exclusive AI assistant to improve work efficiency and quality of life.',
                githubProjectDescription: 'Description of popular GitHub project',
                clawdhubSkillDescription: 'Description of ClawdHub skill',
                chatgptDescription: 'Advanced conversational AI developed by OpenAI that can answer questions, create text, code, and more. Powerful natural language understanding and generation capabilities suitable for various text creation scenarios. Features advanced models like GPT-4 Turbo.',
                claudeDescription: 'AI assistant developed by Anthropic focused on safety and helpfulness. Has excellent long-form text generation and conversational abilities, especially suitable for scenarios requiring safety and reliability. Supports up to 100K tokens of context.',
                geminiDescription: 'Google-developed multimodal AI model that can handle text, images, audio, video, and code. Powerful multimodal understanding and generation capabilities combined with Google search capabilities to provide accurate information.',
                chatgpteudDescription: 'ChatGPT version for educational institutions launched by OpenAI, designed specifically for students and teachers. Provides a secure learning environment to help improve teaching efficiency and learning outcomes.',
                copilotDescription: 'AI assistant developed by Microsoft, integrated into Office 365, Windows, and other Microsoft products. Provides productivity enhancement features to help users complete work tasks more efficiently.',
                huggingchatDescription: 'Open-source chat interface launched by Hugging Face that provides access to multiple open-source models. Users can select different models for conversations, supporting privacy-protected chat experiences.',
                midjourneyDescription: 'Powerful AI image generation tool that can create beautiful images based on text descriptions. Known for its artistic styles and high-quality images, it is the tool of choice for creative professionals. Supports various art styles and parameter adjustments.',
                dalle3Description: 'OpenAI\'s latest image generation AI that can create high-quality images. Deeply integrated with ChatGPT, providing precise image generation control. Supports direct text-to-image conversion.',
                stablediffusionDescription: 'Open-source AI image generation model that can run locally. Provides maximum customization flexibility, supporting various styles and parameter adjustments. Active community with rich plugins.',
                fireflyDescription: 'Adobe-developed AI creative tool, integrated in Photoshop and other Creative Cloud applications. Provides professional image generation and editing functions, suitable for designers.',
                leonardodescription: 'AI image and video generation platform suitable for creative projects. Provides high-quality artistic style generation and video production capabilities. Supports game development asset generation.',
                elevenlabsDescription: 'AI voice synthesis tool that can create realistic voices. Offers multiple voice options, supports text-to-speech, widely used in podcasts, video narrations, etc.',
                descriptDescription: 'Audio and video editing tool that provides AI-driven transcription, editing, and synthesis functions. Allows editing audio and video like editing text, simplifying the creation process.',
                runwaymlDescription: 'Creative AI tools platform offering video editing, image generation, and more. Focuses on creative professionals, providing advanced AI creative tools. Supports green screen removal, video stabilization, and more.',
                synthesiaDescription: 'AI virtual presenter platform that can create professional enterprise training and marketing videos. No camera equipment or studio needed, quickly generate personalized video content.',
                codewhispererDescription: 'AI coding assistant developed by Amazon that provides code suggestions and auto-completion. Supports multiple programming languages, integrated into mainstream IDEs, improving development efficiency.',
                tabnineDescription: 'AI-driven code auto-completion tool that supports multiple programming languages and IDEs. Provides intelligent code suggestions to improve coding efficiency and accuracy.',
                salesforceDescription: 'AI functions integrated in Salesforce that provide predictive analytics, automation, and personalization. Helps businesses better understand customers and improve sales and marketing efficiency.',
                watsonDescription: 'IBM\'s AI platform that provides cognitive computing, machine learning, and natural language processing functions. Widely used in enterprise-level AI solutions, supporting multiple industry application scenarios.',
                jasperDescription: 'AI content creation tool that helps write marketing copy, blogs, and more. Provides multiple content templates suitable for marketers and content creators. Features brand voice functionality to maintain content consistency.',
                notionaiDescription: 'AI features integrated into Notion that help with writing, summarizing, translating, and more. Seamlessly integrates with workspaces to improve efficiency. Supports multiple languages with rich functionality.',
                writesonicDescription: 'AI content creation tool that helps write ad copy, blog articles, social media content, etc. Provides multiple content templates and creation tools suitable for marketers and content creators.',
                senseiDescription: 'Collection of AI functions in Adobe Creative Cloud that provide intelligent image editing, content recognition, automatic repair, and more. Integrated in Photoshop, Premiere Pro, etc., to enhance creative work efficiency.',
                canvaDescription: 'AI functions in Canva that provide intelligent design suggestions, background removal, text generation, and more. Helps users quickly create professional designs without design experience.',
                perplexityDescription: 'AI-powered search engine providing accurate information queries. Combines the advantages of search and AI, providing accurate answers with citations. Supports professional mode and research mode.',
                youDescription: 'AI-powered search platform providing personalized search results. Integrates multiple information sources to provide more relevant and useful search results while protecting user privacy.'
            },
            'ja': {
                pageTitle: 'AIツールハブ - 最強のAIツールを発見 | ClawDBot推奨',
                siteTitle: 'AIツールハブ',
                siteSubtitle: '最も強力なAIツールを発見し、仕事と生活を向上させましょう',
                searchPlaceholder: 'AIツールを検索...',
                sortBy: '並び替え:',
                sortByName: '名前',
                sortByRating: '評価',
                sortByCategory: 'カテゴリ',
                allCategories: 'すべて',
                textGeneration: 'テキスト生成',
                imageGeneration: '画像生成',
                audioTools: '音声ツール',
                videoTools: '動画ツール',
                codingAssistants: 'コーディング支援',
                contentCreation: 'コンテンツ作成',
                businessTools: 'ビジネスツール',
                creativeTools: 'クリエイティブツール',
                personalAi: '個人用AIアシスタント',
                githubProjects: 'GitHub人気',
                clawdhubSkills: 'ClawdHubスキル',
                searchTools: '検索ツール',
                featured: '注目',
                visitWebsite: 'ウェブサイトへ',
                free: '無料版',
                paid: '有料',
                totalTools: 'ツール総数',
                freeTools: '無料ツール',
                categories: 'カテゴリ',
                aboutUs: '私たちについて',
                contactUs: 'お問い合わせ',
                privacyPolicy: 'プライバシーポリシー',
                termsOfService: '利用規約',
                sitemap: 'サイトマップ',
                apiDocs: 'APIドキュメント',
                copyright: '© 2026 AIツールハブ - 最高のAIツールを発見して活用',
                disclaimer: '免責事項: 当サイトはAIツールのディレクトリであり、AIサービスを提供するものではありません',
                currentDomain: '現在のドメイン: http://8.215.63.182:8094 | 公式ドメイン: https://chuansha.tech',
                toolDetails: 'ツール詳細',
                category: 'カテゴリ:',
                rating: '評価:',
                pricing: '価格:',
                clawdbotDescription: 'ClawDBotは、日常タスクの処理、情報管理、ワークフロー自動化を支援する強力な個人用AIアシスタントシステムです。Telegram、WhatsApp、Signalなど複数の通信チャネルをサポートし、あなたの専属AIアシスタントとして働き、仕事効率と生活の質を向上させます。',
                githubProjectDescription: '人気のあるGitHubプロジェクトの説明',
                clawdhubSkillDescription: 'ClawdHubスキルの説明',
                chatgptDescription: 'OpenAIが開発した高度な対話型AIで、質問に答えたり、文章やコードを作成したりできます。強力な自然言語理解・生成機能を備え、さまざまな文章作成シナリオに適しています。GPT-4 Turboなどの先進的なモデルを搭載。',
                claudeDescription: 'Anthropic社が開発した安全性と有用性を重視したAIアシスタント。優れた長文生成および対話機能を持ち、安全性と信頼性が求められるシナリオに最適です。最大100Kトークンのコンテキストをサポート。',
                geminiDescription: 'Googleが開発したマルチモーダルAIモデルで、テキスト、画像、音声、動画、コードを処理できます。強力なマルチモーダル理解・生成機能に加え、Google検索機能を組み合わせ、正確な情報を提供します。',
                chatgpteudDescription: 'OpenAIが教育機関向けに提供するChatGPTバージョンで、学生と教師のために設計されています。安全な学習環境を提供し、教育効率と学習成果を向上させます。',
                copilotDescription: 'Microsoftが開発したAIアシスタントで、Office 365、Windows、その他のMicrosoft製品に統合されています。生産性向上機能を提供し、ユーザーが作業を効率的に完了できるように支援します。',
                huggingchatDescription: 'Hugging Faceが提供するオープンソースのチャットインターフェースで、複数のオープンソースモデルにアクセスできます。ユーザーは異なるモデルを選択して会話でき、プライバシー保護されたチャット体験をサポートします。',
                midjourneyDescription: 'テキスト記述に基づいて美しい画像を生成する強力なAI画像生成ツール。芸術的なスタイルと高品質な画像で知られ、クリエイティブプロフェッショナルの選りすぐりのツールです。さまざまなアートスタイルとパラメータ調整をサポート。',
                dalle3Description: 'OpenAIの最新画像生成AIで、高品質な画像を作成できます。ChatGPTと深く統合され、正確な画像生成コントロールを提供します。テキストから画像への直接変換をサポート。',
                stablediffusionDescription: 'ローカルで実行可能なオープンソースのAI画像生成モデル。最大限のカスタマイズ性を提供し、さまざまなスタイルとパラメータ調整をサポートします。活発なコミュニティと豊富なプラグインがあります。',
                fireflyDescription: 'Adobeが開発したAIクリエイティブツールで、Photoshopやその他のCreative Cloudアプリケーションに統合されています。プロフェッショナルな画像生成・編集機能を提供し、デザイナーに最適です。',
                leonardodescription: 'クリエイティブプロジェクトに適したAI画像・動画生成プラットフォーム。高品質なアートスタイル生成と動画制作機能を提供します。ゲーム開発アセット生成をサポート。',
                elevenlabsDescription: 'リアルな音声を生成できるAI音声合成ツール。複数の音声オプションを提供し、テキスト読み上げをサポート。ポッドキャスト、動画ナレーションなどで広く使用されています。',
                descriptDescription: '音声・動画編集ツールで、AI駆動のトランスクリプション、編集、合成機能を提供します。テキスト編集のように音声・動画を編集でき、制作プロセスを簡略化します。',
                runwaymlDescription: '動画編集、画像生成などを提供するクリエイティブAIツールプラットフォーム。クリエイティブプロフェッショナルに焦点を当て、高度なAIクリエイティブツールを提供します。グリーンスクリーン除去、動画安定化などをサポート。',
                synthesiaDescription: 'AIバーチャルプレゼンタープラットフォームで、プロフェッショナルな企業研修・マーケティング動画を作成できます。カメラ機器やスタジオが不要で、迅速にパーソナライズされた動画コンテンツを生成します。',
                codewhispererDescription: 'Amazonが開発したAIコーディングアシスタントで、コード提案・自動補完機能を提供します。複数のプログラミング言語をサポートし、主要IDEに統合され、開発効率を向上させます。',
                tabnineDescription: 'AI駆動のコード自動補完ツールで、複数のプログラミング言語とIDEをサポートします。インテリジェントなコード提案により、コーディング効率と正確性を向上させます。',
                salesforceDescription: 'Salesforceに統合されたAI機能で、予測分析、自動化、パーソナライゼーションを提供します。企業が顧客をよりよく理解し、販売・マーケティング効率を向上させるのに役立ちます。',
                watsonDescription: 'IBMのAIプラットフォームで、認知計算、機械学習、自然言語処理機能を提供します。エンタープライズレベルのAIソリューションで広く使用され、複数の業界アプリケーションシナリオをサポートします。',
                jasperDescription: 'マーケティングコピー、ブログなどを執筆するAIコンテンツ作成ツール。複数のコンテンツテンプレートを提供し、マーケターとコンテンツクリエーターに最適です。ブランドボイス機能により、コンテンツの一貫性を維持します。',
                notionaiDescription: '文章作成、要約、翻訳などを支援するNotionに統合されたAI機能。ワークスペースとシームレスに統合され、効率を向上させます。複数言語をサポートし、豊富な機能を備えています。',
                writesonicDescription: '広告コピー、ブログ記事、SNSコンテンツなどを作成するAIコンテンツ作成ツール。複数のコンテンツテンプレートと作成ツールを提供し、マーケターとコンテンツクリエーターに適しています。',
                senseiDescription: 'Adobe Creative CloudのAI機能群で、インテリジェントな画像編集、コンテンツ認識、自動修復などを提供します。Photoshop、Premiere Proなどに統合され、クリエイティブ作業効率を向上させます。',
                canvaDescription: 'CanvaのAI機能で、インテリジェントなデザイン提案、背景削除、テキスト生成などを提供します。デザイン経験がなくても、プロフェッショナルなデザインを素早く作成できます。',
                perplexityDescription: '正確な情報検索を提供するAI駆動の検索エンジン。検索とAIの利点を組み合わせ、引用付きの正確な回答を提供します。プロフェッショナルモードとリサーチモードをサポート。',
                youDescription: 'AI駆動の検索プラットフォームで、パーソナライズされた検索結果を提供します。複数の情報源を統合し、より関連性の高い有用な検索結果を提供しながら、ユーザーのプライバシーを保護します。'
            },
            'ko': {
                pageTitle: 'AI 도구 허브 - 가장 강력한 AI 도구를 발견하세요 | ClawDBot 추천',
                siteTitle: 'AI 도구 허브',
                siteSubtitle: '가장 강력한 AI 도구를 발견하고 업무와 삶을 향상시키세요',
                searchPlaceholder: 'AI 도구 검색...',
                sortBy: '정렬:',
                sortByName: '이름순',
                sortByRating: '평점순',
                sortByCategory: '카테고리',
                allCategories: '전체',
                textGeneration: '텍스트 생성',
                imageGeneration: '이미지 생성',
                audioTools: '음성 도구',
                videoTools: '비디오 도구',
                codingAssistants: '코딩 지원',
                contentCreation: '콘텐츠 제작',
                businessTools: '비즈니스 도구',
                creativeTools: '크리에이티브 도구',
                personalAi: '개인 AI 어시스턴트',
                githubProjects: 'GitHub 인기',
                clawdhubSkills: 'ClawdHub 스킬',
                searchTools: '검색 도구',
                featured: '추천',
                visitWebsite: '웹사이트 방문',
                free: '무료 버전',
                paid: '유료',
                totalTools: '총 도구 수',
                freeTools: '무료 도구',
                categories: '카테고리',
                aboutUs: '회사 소개',
                contactUs: '연락처',
                privacyPolicy: '개인정보 처리방침',
                termsOfService: '이용 약관',
                sitemap: '사이트맵',
                apiDocs: 'API 문서',
                copyright: '© 2026 AI 도구 허브 - 최고의 AI 도구를 발견하고 활용하세요',
                disclaimer: '면책사항: 본 사이트는 AI 도구 디렉토리일 뿐, AI 서비스를 제공하지 않습니다',
                currentDomain: '현재 도메인: http://8.215.63.182:8094 | 공식 도메인: https://chuansha.tech',
                toolDetails: '도구 상세 정보',
                category: '카테고리:',
                rating: '평점:',
                pricing: '가격:',
                clawdbotDescription: 'ClawDBot은 일상 업무 처리, 정보 관리, 워크플로우 자동화를 지원하는 강력한 개인 AI 어시스턴트 시스템입니다. Telegram, WhatsApp, Signal 등 다양한 통신 채널을 지원하며, 귀하의 전담 AI 어시스턴트가 되어 업무 효율과 생활의 질을 향상시켜 줍니다.',
                githubProjectDescription: '인기 있는 GitHub 프로젝트 설명',
                clawdhubSkillDescription: 'ClawdHub 스킬 설명',
                chatgptDescription: 'OpenAI에서 개발한 고급 대화형 AI로, 질문에 답하거나 텍스트 및 코드 작성 등을 할 수 있습니다. 강력한 자연어 이해 및 생성 기능을 갖추고 있어 다양한 텍스트 작성 시나리오에 적합합니다. GPT-4 Turbo와 같은 고급 모델을 탑재했습니다.',
                claudeDescription: 'Anthropic사가 개발한 안전성과 유용성을 중시하는 AI 어시스턴트입니다. 우수한 장문 생성 및 대화 기능을 보유하여 안전성과 신뢰성이 요구되는 시나리오에 특히 적합합니다. 최대 100K 토큰의 콘텍스트를 지원합니다.',
                geminiDescription: 'Google에서 개발한 멀티모달 AI 모델로, 텍스트, 이미지, 음성, 비디오, 코드를 처리할 수 있습니다. 강력한 멀티모달 이해 및 생성 기능과 Google 검색 기능을 결합하여 정확한 정보를 제공합니다.',
                chatgpteudDescription: 'OpenAI가 교육 기관을 위해 출시한 ChatGPT 버전으로, 학생과 교사를 위해 특별히 설계되었습니다. 안전한 학습 환경을 제공하여 교육 효율과 학습 성과를 향상시킵니다.',
                copilotDescription: 'Microsoft가 개발한 AI 어시스턴트로, Office 365, Windows 및 기타 Microsoft 제품에 통합되어 있습니다. 생산성 향상 기능을 제공하여 사용자가 작업을 보다 효율적으로 완료할 수 있도록 도와줍니다.',
                huggingchatDescription: 'Hugging Face가 출시한 오픈소스 채팅 인터페이스로, 여러 오픈소스 모델에 접근할 수 있습니다. 사용자는 서로 다른 모델을 선택하여 대화할 수 있으며, 개인정보 보호가 가능한 채팅 경험을 지원합니다.',
                midjourneyDescription: '텍스트 설명을 바탕으로 아름다운 이미지를 생성할 수 있는 강력한 AI 이미지 생성 도구입니다. 예술적인 스타일과 고품질 이미지로 유명하며, 창의적 전문가들의 선택 도구입니다. 다양한 아트 스타일과 파라미터 조정을 지원합니다.',
                dalle3Description: 'OpenAI의 최신 이미지 생성 AI로, 고품질 이미지를 생성할 수 있습니다. ChatGPT와 깊이 통합되어 정밀한 이미지 생성 컨트롤을 제공합니다. 텍스트-이미지 직접 변환을 지원합니다.',
                stablediffusionDescription: '로컬에서 실행 가능한 오픈소스 AI 이미지 생성 모델입니다. 최대한의 맞춤화 유연성을 제공하며, 다양한 스타일과 파라미터 조정을 지원합니다. 활성화된 커뮤니티와 풍부한 플러그인을 보유하고 있습니다.',
                fireflyDescription: 'Adobe에서 개발한 AI 크리에이티브 도구로, Photoshop 및 기타 Creative Cloud 애플리케이션에 통합되어 있습니다. 전문적인 이미지 생성 및 편집 기능을 제공하여 디자이너에게 적합합니다.',
                leonardodescription: '창의적 프로젝트에 적합한 AI 이미지 및 비디오 생성 플랫폼입니다. 고품질 아트 스타일 생성 및 비디오 제작 기능을 제공합니다. 게임 개발 자산 생성을 지원합니다.',
                elevenlabsDescription: '현실적인 음성을 생성할 수 있는 AI 음성 합성 도구입니다. 다양한 음성 옵션을 제공하고 텍스트 음성 변환을 지원하여 팟캐스트, 비디오 내레이션 등에서 널리 사용됩니다.',
                descriptDescription: '오디오 및 비디오 편집 도구로, AI 기반의 전사, 편집, 합성 기능을 제공합니다. 텍스트를 편집하듯 오디오 및 비디오를 편집할 수 있어 제작 프로세스를 간소화합니다.',
                runwaymlDescription: '비디오 편집, 이미지 생성 등을 제공하는 크리에이티브 AI 도구 플랫폼입니다. 크리에이티브 전문가에 초점을 맞추고, 고급 AI 크리에이티브 도구를 제공합니다. 그린스크린 제거, 비디오 안정화 등을 지원합니다.',
                synthesiaDescription: 'AI 가상 발표자 플랫폼으로, 전문적인 기업 교육 및 마케팅 비디오를 만들 수 있습니다. 카메라 장비나 스튜디오가 필요 없이 빠르게 개인화된 비디오 콘텐츠를 생성합니다.',
                codewhispererDescription: 'Amazon이 개발한 AI 코딩 어시스턴트로, 코드 제안 및 자동 완성 기능을 제공합니다. 여러 프로그래밍 언어를 지원하며 주류 IDE에 통합되어 개발 효율을 향상시킵니다.',
                tabnineDescription: 'AI 기반 코드 자동 완성 도구로, 여러 프로그래밍 언어와 IDE를 지원합니다. 지능적인 코드 제안을 통해 코딩 효율과 정확성을 향상시킵니다.',
                salesforceDescription: 'Salesforce에 통합된 AI 기능으로, 예측 분석, 자동화, 개인화 기능을 제공합니다. 기업이 고객을 더 잘 이해하고 판매 및 마케팅 효율을 향상시키는 데 도움을 줍니다.',
                watsonDescription: 'IBM의 AI 플랫폼으로, 인지 컴퓨팅, 머신 러닝, 자연어 처리 기능을 제공합니다. 엔터프라이즈 수준의 AI 솔루션에 널리 사용되며, 여러 산업 응용 시나리오를 지원합니다.',
                jasperDescription: '마케팅 카피, 블로그 등을 작성하는 AI 콘텐츠 제작 도구입니다. 다양한 콘텐츠 템플릿을 제공하여 마케터와 콘텐츠 크리에이터에게 적합합니다. 브랜드 보이스 기능을 통해 콘텐츠 일관성을 유지합니다.',
                notionaiDescription: '글쓰기, 요약, 번역 등을 지원하는 Notion에 통합된 AI 기능입니다. 작업 공간과 시ーム리스하게 통합되어 효율을 향상시킵니다. 다국어를 지원하며 다양한 기능을 갖추고 있습니다.',
                writesonicDescription: '광고 카피, 블로그 기사, SNS 콘텐츠 등을 작성하는 AI 콘텐츠 제작 도구입니다. 다양한 콘텐츠 템플릿과 제작 도구를 제공하여 마케터와 콘텐츠 크리에이터에게 적합합니다.',
                senseiDescription: 'Adobe Creative Cloud의 AI 기능 집합으로, 지능형 이미지 편집, 콘텐츠 인식, 자동 수리 등을 제공합니다. Photoshop, Premiere Pro 등에 통합되어 창의적 작업 효율을 향상시킵니다.',
                canvaDescription: 'Canva의 AI 기능으로, 지능형 디자인 제안, 배경 제거, 텍스트 생성 등을 제공합니다. 디자인 경험이 없어도 전문적인 디자인을 빠르게 만들 수 있습니다.',
                perplexityDescription: '정확한 정보 조회를 제공하는 AI 기반 검색 엔진입니다. 검색과 AI의 장점을 결합하여 인용이 포함된 정확한 답변을 제공합니다. 프로페셔널 모드와 리서치 모드를 지원합니다.',
                youDescription: 'AI 기반 검색 플랫폼으로, 개인화된 검색 결과를 제공합니다. 여러 정보 소스를 통합하여 더 관련성 높고 유용한 검색 결과를 제공하면서 사용자 개인정보를 보호합니다.'
            }
        };

        // 当前语言
        let currentLang = localStorage.getItem('preferredLanguage') || 'zh-CN';

        // 防抖函数
        function debounce(func, wait) {
            let timeout;
            return function executedFunction(...args) {
                const later = () => {
                    clearTimeout(timeout);
                    func(...args);
                };
                clearTimeout(timeout);
                timeout = setTimeout(later, wait);
            };
        }

        // 节流函数
        function throttle(func, limit) {
            let inThrottle;
            return function() {
                const args = arguments;
                const context = this;
                if (!inThrottle) {
                    func.apply(context, args);
                    inThrottle = true;
                    setTimeout(() => inThrottle = false, limit);
                }
            }
        }

        // DOM加载完成后初始化
        document.addEventListener('DOMContentLoaded', function() {
            // 初始化国际化
            initializeI18n();
            
            // 初始化所有功能
            updateStats();
            initSearch();
            initCategoryFilter();
            initSort();
            initBackToTop();
            initModal();
            initAnalytics();
            initKeyboardShortcuts();
            initCopyToClipboard();
            initShareButtons();
            
            // 添加工具点击事件
            const cards = document.querySelectorAll('.tool-card');
            cards.forEach(card => {
                card.addEventListener('click', function(e) {
                    // 如果点击的是链接，则不触发模态框
                    if (e.target.tagName === 'A' || e.target.classList.contains('tool-link')) {
                        trackEvent('tool_link_click', {
                            tool_name: this.querySelector('.tool-title').textContent
                        });
                        return;
                    }
                    showToolModal(this);
                });
            });
            
            // 添加复制链接功能
            addCopyLinkFeature();
        });

        // 初始化国际化
        function initializeI18n() {
            // 设置当前语言
            setLanguage(currentLang);
            
            // 语言切换事件
            const langOptions = document.querySelectorAll('.lang-option');
            langOptions.forEach(option => {
                option.addEventListener('click', function() {
                    const lang = this.dataset.lang;
                    setLanguage(lang);
                    
                    // 更新活动状态
                    langOptions.forEach(opt => opt.classList.remove('active'));
                    this.classList.add('active');
                    
                    // 保存用户偏好
                    localStorage.setItem('preferredLanguage', lang);
                });
            });
        }

        // 设置语言
        function setLanguage(lang) {
            currentLang = lang;
            
            // 更新页面语言属性
            document.documentElement.lang = lang;
            
            // 更新所有带有data-i18n属性的元素
            const elements = document.querySelectorAll('[data-i18n]');
            elements.forEach(element => {
                const key = element.dataset.i18n;
                if (translations[lang] && translations[lang][key]) {
                    element.textContent = translations[lang][key];
                }
            });
            
            // 更新placeholder
            const placeholders = document.querySelectorAll('[data-i18n-placeholder]');
            placeholders.forEach(element => {
                const key = element.dataset.i18nPlaceholder;
                if (translations[lang] && translations[lang][key]) {
                    element.placeholder = translations[lang][key];
                }
            });
            
            // 更新title属性
            const titles = document.querySelectorAll('[data-i18n-title]');
            titles.forEach(element => {
                const key = element.dataset.i18nTitle;
                if (translations[lang] && translations[lang][key]) {
                    element.title = translations[lang][key];
                }
            });
        }

        // 更新统计信息
        function updateStats() {
            const totalTools = document.querySelectorAll('.tool-card').length;
            const aiTools = document.querySelectorAll('.tool-card[data-category="text"], .tool-card[data-category="image"], .tool-card[data-category="audio"], .tool-card[data-category="video"], .tool-card[data-category="code"], .tool-card[data-category="content"], .tool-card[data-category="business"], .tool-card[data-category="creative"], .tool-card[data-category="search"], .tool-card[data-category="personal-ai"]').length;
            const githubProjects = document.querySelectorAll('.tool-card[data-category="github"]').length;
            const clawdSkills = document.querySelectorAll('.tool-card[data-category="clawdhub"]').length;
            const freeTools = document.querySelectorAll('.tool-card[data-free="true"]').length;
            const categories = new Set();
            
            document.querySelectorAll('.tool-card').forEach(card => {
                categories.add(card.dataset.category);
            });
            
            document.getElementById('totalTools').textContent = totalTools;
            document.getElementById('aiTools').textContent = aiTools;
            document.getElementById('githubProjects').textContent = githubProjects;
            document.getElementById('clawdSkills').textContent = clawdSkills;
            document.getElementById('categories').textContent = categories.size;
        }
        
        // 搜索功能
        function initSearch() {
            const searchInput = document.getElementById('searchInput');
            if (!searchInput) return;
            
            searchInput.addEventListener('input', debounce(function(e) {
                const searchTerm = e.target.value.toLowerCase().trim();
                const cards = document.querySelectorAll('.tool-card');
                let visibleCount = 0;
                
                cards.forEach(card => {
                    const title = card.querySelector('.tool-title').textContent.toLowerCase();
                    const desc = card.querySelector('.tool-description').textContent.toLowerCase();
                    const category = card.querySelector('.tool-category').textContent.toLowerCase();
                    
                    if (searchTerm === '') {
                        card.classList.remove('hidden');
                        visibleCount++;
                    } else if (title.includes(searchTerm) || desc.includes(searchTerm) || category.includes(searchTerm)) {
                        card.classList.remove('hidden');
                        visibleCount++;
                    } else {
                        card.classList.add('hidden');
                    }
                });
                
                // 更新统计
                document.getElementById('totalTools').textContent = visibleCount;
                
                // 重新排序显示的卡片
                sortCards();
            }, 300));
        }
        
        // 分类筛选
        function initCategoryFilter() {
            const categoryBtns = document.querySelectorAll('.category-btn');
            if (!categoryBtns.length) return;
            
            categoryBtns.forEach(btn => {
                btn.addEventListener('click', function() {
                    // 移除所有激活状态
                    categoryBtns.forEach(b => b.classList.remove('active'));
                    // 添加当前激活状态
                    this.classList.add('active');
                    
                    const category = this.dataset.category;
                    const cards = document.querySelectorAll('.tool-card');
                    
                    let visibleCount = 0;
                    
                    cards.forEach(card => {
                        if (category === 'all') {
                            card.classList.remove('hidden');
                            visibleCount++;
                        } else {
                            if (card.dataset.category === category) {
                                card.classList.remove('hidden');
                                visibleCount++;
                            } else {
                                card.classList.add('hidden');
                            }
                        }
                    });
                    
                    // 更新统计
                    document.getElementById('totalTools').textContent = visibleCount;
                    
                    // 重新排序显示的卡片
                    sortCards();
                    
                    trackEvent('category_filter', {
                        category: category,
                        filtered_count: visibleCount
                    });
                });
            });
        }
        
        // 排序功能
        function initSort() {
            const sortSelect = document.getElementById('sortSelect');
            if (!sortSelect) return;
            
            sortSelect.addEventListener('change', function() {
                sortCards();
                trackEvent('sort_changed', {
                    sort_type: this.value
                });
            });
        }
        
        // 对卡片进行排序
        function sortCards() {
            const sortType = document.getElementById('sortSelect')?.value || 'name';
            const container = document.getElementById('toolsGrid');
            const cards = Array.from(document.querySelectorAll('.tool-card:not(.hidden)'));
            const hiddenCards = Array.from(document.querySelectorAll('.tool-card.hidden'));
            
            switch(sortType) {
                case 'name':
                    cards.sort((a, b) => {
                        const titleA = a.querySelector('.tool-title').textContent.toLowerCase();
                        const titleB = b.querySelector('.tool-title').textContent.toLowerCase();
                        return titleA.localeCompare(titleB);
                    });
                    break;
                case 'rating':
                    cards.sort((a, b) => {
                        return parseInt(b.dataset.rating) - parseInt(a.dataset.rating);
                    });
                    break;
                case 'category':
                    cards.sort((a, b) => {
                        const catA = a.dataset.category;
                        const catB = b.dataset.category;
                        return catA.localeCompare(catB);
                    });
                    break;
            }
            
            // 重新排列DOM元素
            cards.forEach(card => container.appendChild(card));
            hiddenCards.forEach(card => container.appendChild(card));
        }
        
        // 返回顶部按钮
        function initBackToTop() {
            const backToTopBtn = document.getElementById('backToTop');
            if (!backToTopBtn) return;
            
            window.addEventListener('scroll', throttle(function() {
                if (window.pageYOffset > 300) {
                    backToTopBtn.classList.add('show');
                } else {
                    backToTopBtn.classList.remove('show');
                }
            }, 100));
            
            backToTopBtn.addEventListener('click', function() {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        }
        
        // 工具详情模态框
        function initModal() {
            const modal = document.getElementById('toolModal');
            const closeBtn = document.querySelector('.close-modal');
            
            closeBtn.addEventListener('click', function() {
                modal.style.display = 'none';
                trackEvent('modal_closed');
            });
            
            window.addEventListener('click', function(e) {
                if (e.target === modal) {
                    modal.style.display = 'none';
                    trackEvent('modal_closed_outside_click');
                }
            });
        }
        
        // 显示工具详情模态框
        function showToolModal(card) {
            const modal = document.getElementById('toolModal');
            const title = card.querySelector('.tool-title').textContent;
            const desc = card.querySelector('.tool-description').textContent;
            const link = card.querySelector('.tool-link').href;
            const category = card.querySelector('.tool-category').textContent;
            const rating = card.dataset.rating;
            const freeStatus = card.dataset.free === 'true' ? 
                (currentLang === 'en' ? 'Free Tier' : currentLang === 'ja' ? '無料版' : currentLang === 'ko' ? '무료 버전' : '免费版') : 
                (currentLang === 'en' ? 'Paid' : currentLang === 'ja' ? '有料' : currentLang === 'ko' ? '유료' : '付费');
            
            document.querySelector('.modal-title').textContent = title;
            document.querySelector('.modal-description').textContent = desc;
            document.getElementById('modalCategory').textContent = category;
            document.getElementById('modalRating').textContent = rating + '/5';
            document.getElementById('modalFreeStatus').textContent = freeStatus;
            document.getElementById('modalLink').href = link;
            
            modal.style.display = 'block';
            trackEvent('modal_opened', {
                tool_name: title
            });
        }
        
        // 分析跟踪功能
        function initAnalytics() {
            // 这里可以集成实际的分析工具
            console.log('分析功能已初始化');
        }
        
        // 跟踪事件
        function trackEvent(eventName, properties = {}) {
            // 模拟事件跟踪
            console.log('事件跟踪:', eventName, properties);
            // 这里可以集成实际的分析工具如GA4等
        }
        
        // 键盘快捷键
        function initKeyboardShortcuts() {
            document.addEventListener('keydown', function(e) {
                // ESC键关闭模态框
                if (e.key === 'Escape') {
                    const modal = document.getElementById('toolModal');
                    if (modal.style.display === 'block') {
                        modal.style.display = 'none';
                    }
                }
                
                // Ctrl/Cmd + K 焦点搜索框
                if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                    e.preventDefault();
                    const searchInput = document.getElementById('searchInput');
                    if (searchInput) {
                        searchInput.focus();
                    }
                }
                
                // Ctrl/Cmd + F 聚焦搜索框
                if ((e.ctrlKey || e.metaKey) && e.key === 'f') {
                    e.preventDefault();
                    const searchInput = document.getElementById('searchInput');
                    if (searchInput) {
                        searchInput.focus();
                    }
                }
            });
        }
        
        // 添加复制链接功能
        function addCopyLinkFeature() {
            const cards = document.querySelectorAll('.tool-card');
            cards.forEach(card => {
                // 检查是否已有复制链接按钮
                if (!card.querySelector('.copy-link-btn')) {
                    const linkButton = document.createElement('a');
                    linkButton.href = '#';
                    linkButton.className = 'tool-link copy-link-btn';
                    linkButton.innerHTML = '🔗 ' + (currentLang === 'en' ? 'Copy Link' : currentLang === 'ja' ? 'リンクをコピー' : currentLang === 'ko' ? '링크 복사' : '复制链接');
                    linkButton.onclick = function(e) {
                        e.preventDefault();
                        e.stopPropagation();
                        const toolLink = card.querySelector('.tool-link').href;
                        copyToClipboard(toolLink);
                        showToast(currentLang === 'en' ? 'Link copied to clipboard!' : 
                                  currentLang === 'ja' ? 'リンクをクリップボードにコピーしました！' : 
                                  currentLang === 'ko' ? '링크가 클립보드에 복사되었습니다!' : '链接已复制到剪贴板！');
                    };
                    card.appendChild(linkButton);
                }
            });
        }
        
        // 复制到剪贴板
        function copyToClipboard(text) {
            if (navigator.clipboard) {
                navigator.clipboard.writeText(text).then(() => {
                    console.log('链接已复制到剪贴板');
                }).catch(err => {
                    console.error('复制失败:', err);
                    fallbackCopyTextToClipboard(text);
                });
            } else {
                fallbackCopyTextToClipboard(text);
            }
        }
        
        // 降级复制方案
        function fallbackCopyTextToClipboard(text) {
            const textArea = document.createElement('textarea');
            textArea.value = text;
            
            // 避免滚动到底部
            textArea.style.top = '0';
            textArea.style.left = '0';
            textArea.style.position = 'fixed';
            textArea.style.opacity = '0';
            
            document.body.appendChild(textArea);
            textArea.focus();
            textArea.select();
            
            try {
                const successful = document.execCommand('copy');
                if (successful) {
                    console.log('链接已复制到剪贴板');
                } else {
                    console.error('复制失败');
                }
            } catch (err) {
                console.error('复制异常:', err);
            }
            
            document.body.removeChild(textArea);
        }
        
        // 显示提示消息
        function showToast(message) {
            // 检查是否已有提示元素
            const existingToast = document.querySelector('.toast-message');
            if (existingToast) {
                existingToast.remove();
            }
            
            const toast = document.createElement('div');
            toast.className = 'toast-message';
            toast.textContent = message;
            toast.style.position = 'fixed';
            toast.style.bottom = '20px';
            toast.style.left = '50%';
            toast.style.transform = 'translateX(-50%)';
            toast.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
            toast.style.color = 'white';
            toast.style.padding = '12px 24px';
            toast.style.borderRadius = '8px';
            toast.style.zIndex = '10000';
            toast.style.fontSize = '14px';
            toast.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.3)';
            toast.style.opacity = '0';
            toast.style.transition = 'opacity 0.3s ease';
            
            document.body.appendChild(toast);
            
            // 显示动画
            setTimeout(() => {
                toast.style.opacity = '1';
            }, 10);
            
            // 3秒后移除提示
            setTimeout(() => {
                toast.style.opacity = '0';
                setTimeout(() => {
                    if (toast.parentNode) {
                        toast.parentNode.removeChild(toast);
                    }
                }, 300);
            }, 3000);
        }
        
        // 初始化复制到剪贴板功能
        function initCopyToClipboard() {
            // 功能已在addCopyLinkFeature中实现
        }
        
        // 初始化分享按钮
        function initShareButtons() {
            // 分享功能已经通过onclick事件实现
        }
        
        // 社交分享功能
        function shareToSocial(platform) {
            const url = encodeURIComponent(window.location.href);
            const title = encodeURIComponent(document.title);
            const description = encodeURIComponent(translations[currentLang].siteSubtitle || 'Check out this amazing collection of AI tools!');
            
            let shareUrl = '';
            
            switch(platform) {
                case 'twitter':
                    shareUrl = `https://twitter.com/intent/tweet?url=${url}&text=${title}`;
                    break;
                case 'facebook':
                    shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
                    break;
                case 'linkedin':
                    shareUrl = `https://www.linkedin.com/shareArticle?mini=true&url=${url}&title=${title}&summary=${description}`;
                    break;
                case 'reddit':
                    shareUrl = `https://reddit.com/submit?url=${url}&title=${title}`;
                    break;
                default:
                    shareUrl = url;
            }
            
            window.open(shareUrl, '_blank', 'width=600,height=400');
            
            trackEvent('social_share', {
                platform: platform
            });
        }
        
        // 添加页面加载动画
        document.body.style.opacity = '0';
        setTimeout(() => {
            document.body.style.transition = 'opacity 0.5s ease-in-out';
            document.body.style.opacity = '1';
        }, 100);
        
        // 页面可见性API
        document.addEventListener('visibilitychange', function() {
            if (document.visibilityState === 'visible') {
                // 页面变为可见时执行的操作
                console.log('页面变为可见');
            } else {
                // 页面变为隐藏时执行的操作
                console.log('页面变为隐藏');
            }
        });
        
        // 性能监控
        if ('performance' in window) {
            window.addEventListener('load', function() {
                setTimeout(function() {
                    const perfData = performance.getEntriesByType('navigation')[0];
                    console.log('页面加载时间:', perfData.loadEventEnd - perfData.loadEventStart, 'ms');
                }, 0);
            });
        }
    </script>
</body>
</html>
"""

    # 写入更新后的HTML文件
    with open("/home/admin/clawd/ai_tools_website/index.html", "w", encoding="utf-8") as f:
        f.write(enhanced_html)
    
    print("🎉 已成功为AI工具聚合网站添加更多主流AI工具!")
    print("⭐ 新增功能包括:")
    print("  • 添加了23个主流AI工具，总计43个工具")
    print("  • 新增了音频工具和视频工具分类")
    print("  • 新增了商业工具分类")
    print("  • 扩展了文本生成类别，包含Gemini、ChatGPT Edu等")
    print("  • 扩展了图像生成类别，包含Adobe Firefly等")
    print("  • 扩展了编程助手类别，包含Amazon CodeWhisperer等")
    print("  • 扩展了内容创作类别，包含Writesonic等")
    print("  • 扩展了创意工具类别，包含Adobe Sensei等")
    print("  • 扩展了搜索工具类别，包含You.com等")
    print("  • 更新了统计数据，现在显示43个总工具")
    print("\n网站现在更加全面，包含了主流AI工具，访问地址: http://8.215.63.182:8094")

if __name__ == "__main__":
    add_more_mainstream_ai_tools()