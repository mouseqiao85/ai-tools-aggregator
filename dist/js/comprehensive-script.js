// 综合功能JavaScript

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
    initBookmarking();
    initDarkModeToggle();
    
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
    
    // 添加工具链接点击跟踪
    const toolLinks = document.querySelectorAll('.tool-link');
    toolLinks.forEach(link => {
        if (!link.href.includes('#')) { // 不是锚点链接
            link.addEventListener('click', function() {
                trackEvent('external_link_click', {
                    tool_name: this.closest('.tool-card').querySelector('.tool-title').textContent,
                    url: this.href
                });
            });
        }
    });
    
    // 添加复制链接功能
    addCopyLinkFeature();
});

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
        showLoading(true);
        
        setTimeout(() => {
            const searchTerm = e.target.value.toLowerCase().trim();
            const cards = document.querySelectorAll('.tool-card');
            let visibleCount = 0;
            
            cards.forEach(card => {
                const title = card.querySelector('.tool-title').textContent.toLowerCase();
                const desc = card.querySelector('.tool-description').textContent.toLowerCase();
                const category = card.querySelector('.tool-category')?.textContent.toLowerCase() || '';
                
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
            showLoading(false);
        }, 100);
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
    const freeStatus = card.dataset.free === 'true' ? '免费' : '付费';
    
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

// 显示/隐藏加载指示器
function showLoading(show) {
    const loadingIndicator = document.getElementById('loadingIndicator');
    if (show) {
        loadingIndicator.style.display = 'block';
    } else {
        loadingIndicator.style.display = 'none';
    }
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
            linkButton.innerHTML = '🔗 复制链接';
            linkButton.onclick = function(e) {
                e.preventDefault();
                e.stopPropagation();
                const toolLink = card.querySelector('.tool-link').href;
                copyToClipboard(toolLink);
                showToast('链接已复制到剪贴板！');
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

// 初始化复制到剪贴板功能
function initCopyToClipboard() {
    // 功能已在addCopyLinkFeature中实现
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

// 书签功能
function initBookmarking() {
    // 添加书签功能的实现
    console.log('书签功能已初始化');
}

// 暗色模式切换
function initDarkModeToggle() {
    // 检查用户偏好设置
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    
    // 这里可以添加暗色模式切换逻辑
    console.log('暗色模式功能已初始化');
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
