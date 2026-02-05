// PocketBase Integration Script
// 用于从PocketBase数据库获取AI工具数据

// PocketBase API基础URL
const POCKETBASE_URL = 'http://8.215.63.182:8090';

// 从PocketBase获取工具数据
async function fetchToolsFromPocketBase() {
    try {
        const response = await fetch(`${POCKETBASE_URL}/api/collections/ai_tools/records`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data.items || [];
    } catch (error) {
        console.error('从PocketBase获取数据时出错:', error);
        return [];
    }
}

// 将PocketBase数据转换为网站所需的格式
function convertPocketBaseData(pocketBaseItems) {
    return pocketBaseItems.map(item => ({
        id: item.id,
        name: item.name || '未知工具',
        description: item.description || '暂无描述',
        url: item.url || '#',
        category: item.category || 'other',
        rating: item.rating || 0,
        is_free: item.is_free || false,
        is_featured: item.is_featured || false,
        language_support: item.language_support || '',
        tags: item.tags ? item.tags.split(',').map(tag => tag.trim()) : []
    }));
}

// 加载工具数据并渲染到页面
async function loadAndRenderTools() {
    try {
        console.log('正在从PocketBase获取数据...');
        const pocketBaseData = await fetchToolsFromPocketBase();
        const convertedData = convertPocketBaseData(pocketBaseData);
        
        console.log(`从PocketBase获取到 ${convertedData.length} 个工具`);
        
        // 如果成功获取数据，更新页面内容
        if (convertedData.length > 0) {
            renderTools(convertedData);
            updateStats(convertedData);
        } else {
            // 如果没有获取到数据，使用备用数据
            console.warn('未从PocketBase获取到数据，使用备用数据');
            loadFallbackTools();
        }
    } catch (error) {
        console.error('加载数据时出错:', error);
        loadFallbackTools();
    }
}

// 更新统计信息
function updateStats(tools) {
    const totalTools = tools.length;
    const aiTools = tools.filter(t => !['github', 'clawdhub'].includes(t.category)).length;
    const githubProjects = tools.filter(t => t.category === 'github').length;
    const clawdSkills = tools.filter(t => t.category === 'clawdhub').length;

    // 更新统计数字
    document.getElementById('totalTools').textContent = totalTools;
    document.getElementById('aiTools').textContent = aiTools;
    document.getElementById('githubProjects').textContent = githubProjects;
    document.getElementById('clawdSkills').textContent = clawdSkills;
}

// 渲染工具到页面
function renderTools(tools) {
    const grid = document.getElementById('toolsGrid');
    grid.innerHTML = '';

    if (tools.length === 0) {
        grid.innerHTML = '<p>暂无工具数据</p>';
        return;
    }

    tools.forEach(tool => {
        const toolElement = createToolElement(tool);
        grid.appendChild(toolElement);
    });
}

// 创建单个工具元素
function createToolElement(tool) {
    const div = document.createElement('div');
    div.className = 'tool-card';
    div.setAttribute('data-category', tool.category);
    div.setAttribute('data-rating', tool.rating);
    div.setAttribute('data-free', tool.is_free);

    // 生成星级评价
    let stars = '';
    const fullStars = Math.floor(tool.rating);
    const hasHalfStar = tool.rating % 1 >= 0.5;
    
    for (let i = 0; i < fullStars; i++) {
        stars += '★';
    }
    if (hasHalfStar) {
        stars += '★'; // 简化处理，半星也显示为整星
    }
    for (let i = fullStars + (hasHalfStar ? 1 : 0); i < 5; i++) {
        stars += '☆';
    }

    // 根据当前语言获取翻译
    const currentLang = getCurrentLanguage();
    const translations = window.translations || {};
    const langTranslations = translations[currentLang] || translations['zh-CN'] || {};

    div.innerHTML = `
        ${tool.is_featured ? `<span class="tool-badge">${langTranslations.featured || '推荐'}</span>` : ''}
        <span class="tool-category">${getCategoryName(tool.category)}</span>
        <h3 class="tool-title">${tool.name}</h3>
        <p class="tool-description">${tool.description}</p>
        <div class="rating">
            <div class="rating-stars">${stars}</div>
            <span>${tool.rating}/5</span>
        </div>
        <div class="tool-actions">
            <a href="${tool.url}" target="_blank" class="tool-link">${langTranslations.visitWebsite || '访问官网'}</a>
        </div>
        <div>
            ${tool.is_free ? 
                `<span class="tag tag-free">${langTranslations.free || '免费版'}</span>` : 
                `<span class="tag tag-paid">${langTranslations.paid || '付费'}</span>`
            }
            ${tool.tags && tool.tags.length > 0 ? 
                tool.tags.map(tag => `<span class="tag" style="margin-right: 5px; background: rgba(14, 255, 196, 0.1); color: var(--cyber-primary); border: 1px solid var(--cyber-primary);">${tag}</span>`).join('') 
                : ''}
        </div>
    `;

    return div;
}

// 获取分类名称
function getCategoryName(category) {
    const currentLang = getCurrentLanguage();
    const translations = window.translations || {};
    const langTranslations = translations[currentLang] || translations['zh-CN'] || {};
    
    const categories = {
        'text': langTranslations.textGeneration || '文本生成',
        'image': langTranslations.imageGeneration || '图像生成',
        'audio': langTranslations.audioTools || '音频工具',
        'video': langTranslations.videoTools || '视频工具',
        'code': langTranslations.codingAssistants || '编程助手',
        'content': langTranslations.contentCreation || '内容创作',
        'business': langTranslations.businessTools || '商业工具',
        'creative': langTranslations.creativeTools || '创意工具',
        'chinese-ai': langTranslations.chineseAi || '国产AI',
        'search': langTranslations.searchTools || '搜索工具',
        'personal-ai': langTranslations.personalAi || '个人AI助理',
        'github': langTranslations.githubProjects || 'GitHub热门',
        'clawdhub': langTranslations.clawdhubSkills || 'ClawdHub技能',
        'other': langTranslations.allCategories || '全部'
    };
    
    return categories[category] || category;
}

// 获取当前语言
function getCurrentLanguage() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('lang') || 'zh-CN';
}

// 加载备用工具数据
function loadFallbackTools() {
    console.log('🔄 使用备用工具数据');
    const fallbackTools = [
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
    renderTools(fallbackTools);
    updateStats(fallbackTools);
}

// 在DOM加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    // 如果页面已经有API加载函数，则替换它；否则添加新的
    if (typeof loadToolsFromAPI !== 'undefined') {
        // 替换原有的loadToolsFromAPI函数
        window.loadToolsFromAPI = loadAndRenderTools;
    } else {
        // 直接定义全局函数
        window.loadToolsFromAPI = loadAndRenderTools;
    }
    
    // 开始加载数据
    loadAndRenderTools();
});