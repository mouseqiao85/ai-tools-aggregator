// 增强版JavaScript功能

// 添加更多交互功能
document.addEventListener('DOMContentLoaded', function() {
    // 初始化搜索功能
    initSearch();
    
    // 添加卡片悬停效果
    const cards = document.querySelectorAll('.tool-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            // 可以添加额外的悬停效果
        });
        
        card.addEventListener('mouseleave', function() {
            // 重置悬停效果
        });
    });
    
    // 添加平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // 添加键盘快捷键
    document.addEventListener('keydown', function(e) {
        // ESC键清除搜索
        if (e.key === 'Escape') {
            const searchInput = document.getElementById('searchInput');
            if (searchInput) {
                searchInput.value = '';
                searchInput.focus();
                // 触发搜索更新
                const event = new Event('input');
                searchInput.dispatchEvent(event);
            }
        }
    });
    
    // 添加页面加载动画
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease-in-out';
        document.body.style.opacity = '1';
    }, 100);
});

// 增强版搜索功能
function initSearch() {
    const searchInput = document.getElementById('searchInput');
    if (!searchInput) return;
    
    searchInput.addEventListener('input', function(e) {
        const searchTerm = e.target.value.toLowerCase().trim();
        const cards = document.querySelectorAll('.tool-card');
        
        cards.forEach((card, index) => {
            const title = card.querySelector('.tool-title').textContent.toLowerCase();
            const desc = card.querySelector('.tool-description').textContent.toLowerCase();
            const category = card.querySelector('.tool-category')?.textContent.toLowerCase() || '';
            
            if (searchTerm === '') {
                card.style.display = 'block';
                card.style.opacity = '1';
                card.style.transform = 'scale(1)';
                // 重新应用动画延迟
                card.style.animationDelay = (index * 0.1) + 's';
            } else if (title.includes(searchTerm) || desc.includes(searchTerm) || category.includes(searchTerm)) {
                card.style.display = 'block';
                card.style.opacity = '1';
                card.style.transform = 'scale(1)';
                card.style.animationDelay = '0s'; // 搜索时取消动画延迟
            } else {
                card.style.display = 'none';
                card.style.opacity = '0';
                card.style.transform = 'scale(0.8)';
                card.style.animationDelay = '0s';
            }
        });
    });
    
    // 添加输入框焦点效果
    searchInput.addEventListener('focus', function() {
        this.parentElement.style.transform = 'scale(1.02)';
        this.parentElement.style.boxShadow = '0 15px 40px rgba(0, 0, 0, 0.2)';
    });
    
    searchInput.addEventListener('blur', function() {
        this.parentElement.style.transform = 'scale(1)';
        this.parentElement.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.2)';
    });
    
    // 添加搜索建议功能（简化版）
    const suggestions = [
        'ChatGPT', 'Midjourney', 'Claude', '编程助手', '图像生成', '文本生成'
    ];
    
    searchInput.addEventListener('focus', function() {
        if (this.value === '') {
            this.placeholder = '输入关键词搜索，如: ' + suggestions.slice(0, 3).join(', ');
        }
    });
    
    searchInput.addEventListener('blur', function() {
        this.placeholder = '🔍 搜索AI工具...';
    });
}
