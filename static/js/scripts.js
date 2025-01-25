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