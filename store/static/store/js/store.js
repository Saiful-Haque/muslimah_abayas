document.addEventListener('DOMContentLoaded', function() {
    // --- Inquiry Modal Handling ---
    const inquiryModal = document.getElementById('inquiry-modal');
    const openInquiryBtns = document.querySelectorAll('.open-inquiry-modal');
    const closeInquiryBtn = document.getElementById('close-modal');
    const modalAbayaId = document.getElementById('modal-abaya-id');
    const modalAbayaName = document.getElementById('inquiry-abaya-name');

    if (inquiryModal) {
        openInquiryBtns.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                const abayaId = this.getAttribute('data-id');
                const abayaName = this.getAttribute('data-name');
                
                modalAbayaId.value = abayaId;
                modalAbayaName.value = abayaName;
                
                inquiryModal.classList.remove('hidden');
                document.body.style.overflow = 'hidden'; // Prevent background scrolling
            });
        });

        const closeInquiry = () => {
            inquiryModal.classList.add('hidden');
            document.body.style.overflow = '';
        };

        if (closeInquiryBtn) {
            closeInquiryBtn.addEventListener('click', closeInquiry);
        }

        inquiryModal.addEventListener('click', function(e) {
            if (e.target === inquiryModal) {
                closeInquiry();
            }
        });
    }

    // --- Size Chart Modal Handling ---
    const sizeChartModal = document.getElementById('size-chart-modal');
    const openSizeChartBtn = document.getElementById('open-size-chart');
    const closeSizeChartBtn = document.getElementById('close-size-modal');

    if (sizeChartModal && openSizeChartBtn) {
        openSizeChartBtn.addEventListener('click', function() {
            sizeChartModal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        });

        const closeSizeChart = () => {
            sizeChartModal.classList.add('hidden');
            document.body.style.overflow = '';
        };

        if (closeSizeChartBtn) {
            closeSizeChartBtn.addEventListener('click', closeSizeChart);
        }

        sizeChartModal.addEventListener('click', function(e) {
            if (e.target === sizeChartModal) {
                closeSizeChart();
            }
        });
    }

    // --- Navbar "Our Story" link Modal Behavior ---
    const navStoryTrigger = document.getElementById('nav-story-trigger');
    const storyModal = document.getElementById('story-modal');

    if (navStoryTrigger && storyModal) {
        navStoryTrigger.addEventListener('click', function(e) {
            const pathname = window.location.pathname;
            if (pathname === '/' || pathname === '/store/') {
                e.preventDefault();
                storyModal.classList.remove('hidden');
                document.body.style.overflow = 'hidden';
            }
        });
    }

    // --- Catalog Filter & Sort Handling ---
    const searchInput = document.getElementById('search-input');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const sortSelect = document.getElementById('sort-select');
    const productsGrid = document.getElementById('products-grid');
    const productCards = document.querySelectorAll('.product-card');
    const noResultsMsg = document.getElementById('no-results-msg');

    let currentCategory = 'all';
    let currentSearchQuery = '';

    if (productsGrid && productCards.length > 0) {
        // Filter Logic
        function filterProducts() {
            let visibleCount = 0;

            productCards.forEach(card => {
                const category = card.getAttribute('data-category');
                const name = card.getAttribute('data-name');

                const matchesCategory = currentCategory === 'all' || category === currentCategory;
                const matchesSearch = name.includes(currentSearchQuery);

                if (matchesCategory && matchesSearch) {
                    card.classList.remove('hidden');
                    visibleCount++;
                } else {
                    card.classList.add('hidden');
                }
            });

            if (visibleCount === 0) {
                noResultsMsg.classList.remove('hidden');
            } else {
                noResultsMsg.classList.add('hidden');
            }
        }

        // Search Input Listener
        if (searchInput) {
            searchInput.addEventListener('input', function() {
                currentSearchQuery = this.value.toLowerCase().trim();
                filterProducts();
            });
        }

        // Category Filter Buttons Listener
        filterBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                filterBtns.forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                currentCategory = this.getAttribute('data-filter');
                filterProducts();
            });
        });

        // Sorting Logic
        if (sortSelect) {
            sortSelect.addEventListener('change', function() {
                const sortBy = this.value;
                const cardsArray = Array.from(productCards);

                cardsArray.sort((a, b) => {
                    if (sortBy === 'newest') {
                        return parseInt(b.getAttribute('data-date')) - parseInt(a.getAttribute('data-date'));
                    }
                    return 0;
                });

                // Clear and re-append in new order
                productsGrid.innerHTML = '';
                cardsArray.forEach(card => {
                    productsGrid.appendChild(card);
                });
            });
        }
    }
});
