// Получаем кнопку
const scrollToTopBtn = document.getElementById("scrollToTopBtn");

// Отслеживаем прокрутку страницы
window.onscroll = function() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        scrollToTopBtn.style.display = "block"; // Показываем кнопку
    } else {
        scrollToTopBtn.style.display = "none"; // Скрываем кнопку
    }
};

// Прокрутка вверх при нажатии на кнопку
scrollToTopBtn.addEventListener("click", function() {
    window.scrollTo({
        top: 0,
        behavior: "smooth" // Плавная прокрутка
    });
});

// Функции для открытия и закрытия модального окна
function openModal(action) {
    const modal = document.getElementById('modal');
    const modalTitle = document.getElementById('modal-title');
    const modalContent = document.getElementById('modal-content');
    const urls = document.getElementById('urls').dataset;  // Получаем URL-адреса

    // Очищаем предыдущий контент
    modalContent.innerHTML = '';

    if (action === 'create') {
        modalTitle.textContent = 'Добавить в каталог';
        modalContent.innerHTML = `
            <a href="${urls.createCoin}" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Монета</a>
            <a href="${urls.createBanknote}" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Банкнота</a>
        `;
    } else if (action === 'edit') {
        modalTitle.textContent = 'Редактировать каталог';
        modalContent.innerHTML = `
            <a href="${urls.coinList}" class="bg-yellow-500 text-white px-4 py-2 rounded hover:bg-yellow-600">Монеты</a>
            <a href="${urls.banknoteList}" class="bg-yellow-500 text-white px-4 py-2 rounded hover:bg-yellow-600">Банкноты</a>
        `;
    }

    modal.classList.remove('hidden');
}

function closeModal() {
    document.getElementById('modal').classList.add('hidden');
}