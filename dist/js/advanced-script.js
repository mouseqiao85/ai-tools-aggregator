// 高级功能JavaScript

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

document.addEventListener('DOMContentLoaded', function() {
    // 初始化所有功能
    initSearch();
    initCategoryFilter();
    initSort();
    initBackToTop();
    initModal();
    initAnalytics();
    initKeyboardShortcuts();
    
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
            trackEvent('tool_card_click', {
                tool_name: this.querySelector('.tool-title').textContent
            });
        });
    });
    
    // 添加工具链接点击跟踪
    const toolLinks = document.querySelectorAll('.tool-link');
    toolLinks.forEach(link => {
        link.addEventListener('click', function() {
            trackEvent('external_link_click', {
                tool_name: this.closest('.tool-card').querySelector('.tool-title').textContent,
                url: this.href
            });
        });
    });
});

// 搜索功能
function initSearch() {
    const searchInput = document.getElementById('searchInput');
    if (!searchInput) return;
    
    searchInput.addEventListener('input', debounce(function(e) {
        const searchTerm = e.target.value.toLowerCase().trim();
        const cards = document.querySelectorAll('.tool-card');
        
        cards.forEach(card => {
            const title = card.querySelector('.tool-title').textContent.toLowerCase();
            const desc = card.querySelector('.tool-description').textContent.toLowerCase();
            const category = card.querySelector('.tool-category')?.textContent.toLowerCase() || '';
            
            if (searchTerm === '') {
                card.classList.remove('hidden');
            } else if (title.includes(searchTerm) || desc.includes(searchTerm) || category.includes(searchTerm)) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        });
        
        // 重新排序显示的卡片
        sortCards();
        
        trackEvent('search_performed', {
            search_term: searchTerm,
            results_count: document.querySelectorAll('.tool-card:not(.hidden)').length
        });
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
            
            cards.forEach(card => {
                if (category === 'all') {
                    card.classList.remove('hidden');
                } else {
                    if (card.dataset.category === category) {
                        card.classList.remove('hidden');
                    } else {
                        card.classList.add('hidden');
                    }
                }
            });
            
            // 重新排序显示的卡片
            sortCards();
            
            trackEvent('category_filter', {
                category: category,
                filtered_count: document.querySelectorAll('.tool-card:not(.hidden)').length
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
    
    document.querySelector('.modal-title').textContent = title;
    document.querySelector('.modal-description').innerHTML = desc + '<br><br><strong>类别:</strong> ' + category + '<br><strong>评分:</strong> ' + rating + '/5';
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
    // 这里可以集成实际的分析工具
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
