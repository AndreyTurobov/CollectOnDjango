// Получаем кнопку
let scrollToTopBtn;

// Отслеживаем прокрутку страницы
document.addEventListener('DOMContentLoaded', function() {
    scrollToTopBtn = document.getElementById("scrollToTopBtn");

    if (scrollToTopBtn) {
        window.onscroll = function() {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                scrollToTopBtn.style.display = "block";
            } else {
                scrollToTopBtn.style.display = "none";
            }
        };

        scrollToTopBtn.addEventListener("click", function() {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }
});

// Функции для открытия и закрытия модального окна в navbar
function openModal(action) {
    const modal = document.getElementById('modal');
    const modalTitle = document.getElementById('modal-title');
    const modalContent = document.getElementById('modal-content');
    const urls = document.getElementById('urls').dataset;

    // Очищаем предыдущий контент
    modalContent.innerHTML = '';

    if (action === 'add-value') {
        modalTitle.textContent = 'Добавить (страну, материал, состояние, тему, тип издания)';
        modalContent.innerHTML = `
            <a href="${urls.createCountry}" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Страна</a>
            <a href="${urls.createMaterial}" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Материал</a>
            <a href="${urls.createState}" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Состояние</a>
            <a href="${urls.createTheme}" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Тема</a>
            <a href="${urls.createEdition}" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Тип выпуска</a>
        `;
    } else if (action === 'create') {
        modalTitle.textContent = 'Добавить в каталог';
        modalContent.innerHTML = `
            <a href="${urls.createCoin}" 
            class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            Монета
            </a>
            <a href="${urls.createBanknote}" 
            class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            Банкнота
            </a>
        `;

    } else if (action === 'edit') {
        modalTitle.textContent = 'Редактировать каталог';
        modalContent.innerHTML = `
            <a href="${urls.coinList}" 
            class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            Монеты
            </a>
            <a href="${urls.banknoteList}" 
            class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            Банкноты
            </a>
        `;
    } else if (action === 'new') {
        modalTitle.textContent = 'Новинки';
        modalContent.innerHTML = `
            <a href="${urls.coinNew}" 
               class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
                Монеты
            </a>
            <a href="${urls.banknoteNew}" 
               class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
                Банкноты
            </a>
        `;
    } else if (action === 'plan') {
        modalTitle.textContent = 'Планы';
        modalContent.innerHTML = `
            <a href="${urls.coinPlan}" 
               class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
                Монеты
            </a>
            <a href="${urls.banknotePlan}" 
               class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
                Банкноты
            </a>
        `;
    }

    modal.classList.remove('hidden');
}

function closeModal() {
    document.getElementById('modal').classList.add('hidden');
}

// Функция для открытия модального окна с выбором каталога по странам
function openCatalogModal(country) {
    const modal = document.getElementById('catalogModal');
    const content = document.getElementById('catalogModalContent');
    const title = document.getElementById('catalogModalTitle');

    title.textContent = `Каталоги: ${country}`;
    content.innerHTML = `
        <a href="/coins/?country=${encodeURIComponent(country)}" 
           class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            Монеты
        </a>
        <a href="/banknotes/?country=${encodeURIComponent(country)}" 
           class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            Банкноты
        </a>
    `;

    modal.classList.add('active');
}

// Функция для закрытия модального окна с выбором каталога по странам
function closeCatalogModal() {
    document.getElementById('catalogModal').classList.remove('active');
}

