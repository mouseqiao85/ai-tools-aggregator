
    // 简单的搜索功能
    function initSearch() {
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            searchInput.addEventListener('input', function(e) {
                const searchTerm = e.target.value.toLowerCase();
                const cards = document.querySelectorAll('.tool-card');
                
                cards.forEach(card => {
                    const title = card.querySelector('.tool-title').textContent.toLowerCase();
                    const desc = card.querySelector('.tool-description').textContent.toLowerCase();
                    
                    if (title.includes(searchTerm) || desc.includes(searchTerm)) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        }
    }
    
    // 页面加载完成后初始化
    document.addEventListener('DOMContentLoaded', function() {
        initSearch();
    });
    