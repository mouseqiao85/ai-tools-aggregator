// 国际化功能JavaScript

// 国际化数据
const translations = {
    'zh-CN': {
        pageTitle: 'AI工具聚合站 - 发现最强大的AI工具',
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
        codingAssistants: '编程助手',
        contentCreation: '内容创作',
        creativeTools: '创意工具',
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
        chatgptDescription: 'OpenAI开发的高级对话AI，能够回答问题、创作文字、编程等。强大的自然语言理解和生成能力，适用于各种文本创作场景。拥有GPT-4 Turbo等先进模型。',
        claudeDescription: 'Anthropic公司开发的AI助手，专注于安全和有用性。具有出色的长文本生成和对话能力，特别适合需要安全性和可靠性的场景。支持长达100K tokens的上下文。',
        midjourneyDescription: '强大的AI图像生成工具，能够根据文本描述生成精美图像。以其艺术风格和高质量图像著称，是创意工作者的首选工具。支持多种艺术风格和参数调整。',
        dalle3Description: 'OpenAI的最新图像生成AI，能够创建高质量图像。与ChatGPT深度集成，提供精确的图像生成控制。支持文本到图像的直接转换。',
        stablediffusionDescription: '开源的AI图像生成模型，可在本地运行。提供最大的自定义灵活性，支持各种风格和参数调整。社区活跃，插件丰富。',
        copilotDescription: 'AI编程助手，帮助开发者更快地编写代码。支持多种编程语言，提供智能代码补全和建议。基于GPT-4技术，集成在主流IDE中。',
        codet5Description: '专门针对代码理解与生成的AI模型。支持代码补全、代码解释、代码修复等多种编程任务。开源模型，可本地部署。',
        jasperDescription: 'AI内容创作工具，帮助撰写营销文案、博客等。提供多种内容模板，适合营销和内容创作者。具备品牌声音功能，保持内容一致性。',
        notionaiDescription: '集成在Notion中的AI功能，帮助写作、总结、翻译等。与工作空间无缝集成，提升工作效率。支持多种语言，功能丰富。',
        runwaymlDescription: '创意AI工具平台，提供视频编辑、图像生成等功能。专注于创意专业人士，提供先进的AI创意工具。支持绿幕移除、视频稳定等功能。',
        leonardodescription: 'AI图像和视频生成平台，适合创意项目。提供高质量的艺术风格生成和视频制作能力。支持游戏开发资产生成。',
        perplexityDescription: 'AI驱动的搜索引擎，提供准确的信息查询。结合搜索和AI的优势，提供引用来源的准确答案。支持专业模式和研究模式。'
    },
    'en': {
        pageTitle: 'AI Tools Hub - Discover the Most Powerful AI Tools',
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
        codingAssistants: 'Coding Assistants',
        contentCreation: 'Content Creation',
        creativeTools: 'Creative Tools',
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
        chatgptDescription: 'Advanced conversational AI developed by OpenAI that can answer questions, create text, code, and more. Powerful natural language understanding and generation capabilities suitable for various text creation scenarios. Features advanced models like GPT-4 Turbo.',
        claudeDescription: 'AI assistant developed by Anthropic focused on safety and helpfulness. Has excellent long-form text generation and conversational abilities, especially suitable for scenarios requiring safety and reliability. Supports up to 100K tokens of context.',
        midjourneyDescription: 'Powerful AI image generation tool that can create beautiful images based on text descriptions. Known for its artistic styles and high-quality images, it is the tool of choice for creative professionals. Supports various art styles and parameter adjustments.',
        dalle3Description: 'OpenAI's latest image generation AI that can create high-quality images. Deeply integrated with ChatGPT, providing precise image generation control. Supports direct text-to-image conversion.',
        stablediffusionDescription: 'Open-source AI image generation model that can run locally. Provides maximum customization flexibility, supporting various styles and parameter adjustments. Active community with rich plugins.',
        copilotDescription: 'AI coding assistant that helps developers write code faster. Supports multiple programming languages, providing intelligent code completion and suggestions. Based on GPT-4 technology, integrated into mainstream IDEs.',
        codet5Description: 'AI model specifically designed for code understanding and generation. Supports code completion, code explanation, code fixing, and more. Open-source model that can be deployed locally.',
        jasperDescription: 'AI content creation tool that helps write marketing copy, blogs, and more. Provides multiple content templates suitable for marketers and content creators. Features brand voice functionality to maintain content consistency.',
        notionaiDescription: 'AI features integrated into Notion that help with writing, summarizing, translating, and more. Seamlessly integrates with workspaces to improve efficiency. Supports multiple languages with rich functionality.',
        runwaymlDescription: 'Creative AI tools platform offering video editing, image generation, and more. Focuses on creative professionals, providing advanced AI creative tools. Supports green screen removal, video stabilization, and more.',
        leonardodescription: 'AI image and video generation platform suitable for creative projects. Provides high-quality artistic style generation and video production capabilities. Supports game development asset generation.',
        perplexityDescription: 'AI-powered search engine providing accurate information queries. Combines the advantages of search and AI, providing accurate answers with citations. Supports professional mode and research mode.'
    },
    'ja': {
        pageTitle: 'AIツールハブ - 最強のAIツールを発見',
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
        codingAssistants: 'コーディング支援',
        contentCreation: 'コンテンツ作成',
        creativeTools: 'クリエイティブツール',
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
        chatgptDescription: 'OpenAIが開発した高度な対話型AIで、質問に答えたり、文章やコードを作成したりできます。強力な自然言語理解・生成機能を備え、さまざまな文章作成シナリオに適しています。GPT-4 Turboなどの先進的なモデルを搭載。',
        claudeDescription: 'Anthropic社が開発した安全性と有用性を重視したAIアシスタント。優れた長文生成および対話機能を持ち、安全性と信頼性が求められるシナリオに最適です。最大100Kトークンのコンテキストをサポート。',
        midjourneyDescription: 'テキスト記述に基づいて美しい画像を生成する強力なAI画像生成ツール。芸術的なスタイルと高品質な画像で知られ、クリエイティブプロフェッショナルの選りすぐりのツールです。さまざまなアートスタイルとパラメータ調整をサポート。',
        dalle3Description: 'OpenAIの最新画像生成AIで、高品質な画像を作成できます。ChatGPTと深く統合され、正確な画像生成コントロールを提供します。テキストから画像への直接変換をサポート。',
        stablediffusionDescription: 'ローカルで実行可能なオープンソースのAI画像生成モデル。最大限のカスタマイズ性を提供し、さまざまなスタイルとパラメータ調整をサポートします。活発なコミュニティと豊富なプラグインがあります。',
        copilotDescription: '開発者がより速くコードを書けるように支援するAIコーディングアシスタント。複数のプログラミング言語をサポートし、インテリジェントなコード補完と提案を提供します。GPT-4技術ベースで、主要IDEに統合されています。',
        codet5Description: 'コード理解と生成に特化したAIモデル。コード補完、コード説明、コード修正などをサポート。オープンソースモデルで、ローカルに展開可能です。',
        jasperDescription: 'マーケティングコピー、ブログなどを執筆するAIコンテンツ作成ツール。複数のコンテンツテンプレートを提供し、マーケターとコンテンツクリエーターに最適です。ブランドボイス機能により、コンテンツの一貫性を維持します。',
        notionaiDescription: '文章作成、要約、翻訳などを支援するNotionに統合されたAI機能。ワークスペースとシームレスに統合され、効率を向上させます。複数言語をサポートし、豊富な機能を備えています。',
        runwaymlDescription: '動画編集、画像生成などを提供するクリエイティブAIツールプラットフォーム。クリエイティブプロフェッショナルに焦点を当て、高度なAIクリエイティブツールを提供します。グリーンスクリーン除去、動画安定化などをサポート。',
        leonardodescription: 'クリエイティブプロジェクトに適したAI画像・動画生成プラットフォーム。高品質なアートスタイル生成と動画制作機能を提供します。ゲーム開発アセット生成をサポート。',
        perplexityDescription: '正確な情報検索を提供するAI駆動の検索エンジン。検索とAIの利点を組み合わせ、引用付きの正確な回答を提供します。プロフェッショナルモードとリサーチモードをサポート。'
    },
    'ko': {
        pageTitle: 'AI 도구 허브 - 가장 강력한 AI 도구를 발견하세요',
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
        codingAssistants: '코딩 지원',
        contentCreation: '콘텐츠 제작',
        creativeTools: '크리에이티브 도구',
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
        chatgptDescription: 'OpenAI에서 개발한 고급 대화형 AI로, 질문에 답하거나 텍스트 및 코드 작성 등을 할 수 있습니다. 강력한 자연어 이해 및 생성 기능을 갖추고 있어 다양한 텍스트 작성 시나리오에 적합합니다. GPT-4 Turbo와 같은 고급 모델을 탑재했습니다.',
        claudeDescription: 'Anthropic사가 개발한 안전성과 유용성을 중시하는 AI 어시스턴트입니다. 우수한 장문 생성 및 대화 기능을 보유하여 안전성과 신뢰성이 요구되는 시나리오에 특히 적합합니다. 최대 100K 토큰의 콘텍스트를 지원합니다.',
        midjourneyDescription: '텍스트 설명을 바탕으로 아름다운 이미지를 생성할 수 있는 강력한 AI 이미지 생성 도구입니다. 예술적인 스타일과 고품질 이미지로 유명하며, 창의적 전문가들의 선택 도구입니다. 다양한 아트 스타일과 파라미터 조정을 지원합니다.',
        dalle3Description: 'OpenAI의 최신 이미지 생성 AI로, 고품질 이미지를 생성할 수 있습니다. ChatGPT와 깊이 통합되어 정밀한 이미지 생성 컨트롤을 제공합니다. 텍스트-이미지 직접 변환을 지원합니다.',
        stablediffusionDescription: '로컬에서 실행 가능한 오픈소스 AI 이미지 생성 모델입니다. 최대한의 맞춤화 유연성을 제공하며, 다양한 스타일과 파라미터 조정을 지원합니다. 활성화된 커뮤니티와 풍부한 플러그인을 보유하고 있습니다.',
        copilotDescription: '개발자가 더 빠르게 코드를 작성할 수 있도록 지원하는 AI 코딩 어시스턴트입니다. 여러 프로그래밍 언어를 지원하며, 지능적인 코드 자동 완성과 제안을 제공합니다. GPT-4 기술 기반으로 주요 IDE에 통합되어 있습니다.',
        codet5Description: '코드 이해 및 생성에 특화된 AI 모델입니다. 코드 자동 완성, 코드 설명, 코드 수정 등을 지원합니다. 오픈소스 모델로 로컬에 배포 가능합니다.',
        jasperDescription: '마케팅 카피, 블로그 등을 작성하는 AI 콘텐츠 제작 도구입니다. 다양한 콘텐츠 템플릿을 제공하여 마케터와 콘텐츠 크리에이터에게 적합합니다. 브랜드 보이스 기능을 통해 콘텐츠 일관성을 유지합니다.',
        notionaiDescription: '글쓰기, 요약, 번역 등을 지원하는 Notion에 통합된 AI 기능입니다. 작업 공간과 시ーム리스하게 통합되어 효율을 향상시킵니다. 다국어를 지원하며 다양한 기능을 갖추고 있습니다.',
        runwaymlDescription: '동영상 편집, 이미지 생성 등을 제공하는 크리에이티브 AI 도구 플랫폼입니다. 크리에이티브 전문가에 초점을 맞추고, 고급 AI 크리에이티브 도구를 제공합니다. 그린스크린 제거, 동영상 안정화 등을 지원합니다.',
        leonardodescription: '창의적 프로젝트에 적합한 AI 이미지 및 동영상 생성 플랫폼입니다. 고품질 아트 스타일 생성 및 동영상 제작 기능을 제공합니다. 게임 개발 자산 생성을 지원합니다.',
        perplexityDescription: '정확한 정보 조회를 제공하는 AI 기반 검색 엔진입니다. 검색과 AI의 장점을 결합하여 인용이 포함된 정확한 답변을 제공합니다. 프로페셔널 모드와 리서치 모드를 지원합니다.'
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
    const freeTools = document.querySelectorAll('.tool-card[data-free="true"]').length;
    const categories = new Set();
    
    document.querySelectorAll('.tool-card').forEach(card => {
        categories.add(card.dataset.category);
    });
    
    document.getElementById('totalTools').textContent = totalTools;
    document.getElementById('freeTools').textContent = freeTools;
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
