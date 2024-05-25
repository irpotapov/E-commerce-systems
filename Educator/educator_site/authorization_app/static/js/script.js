document.addEventListener('DOMContentLoaded', function() {
    // Получаем все ссылки меню
    const menuLinks = document.querySelectorAll('.menu a');

    // Функция для переключения видимости разделов
    function switchContent(id) {
        // Скрываем все разделы
        document.querySelectorAll('.content-section').forEach(section => section.classList.add('hidden'));

        // Показываем выбранный раздел
        document.getElementById(id).classList.remove('hidden');
    }

    // Обработчик клика по ссылкам меню
    menuLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Предотвращаем стандартное поведение ссылки
            const targetId = this.getAttribute('href').slice(1); // Получаем ID раздела из href
            switchContent(targetId); // Переключаем видимость раздела
        });
    });

    // Отображаем начальный раздел по умолчанию
    switchContent('card'); // Замените 'card' на ID начального раздела
});

function toggleContent(button) {
    var targetId = button.getAttribute('data-target');
    var targetElement = document.getElementById(targetId);
    if (targetElement) {
        targetElement.classList.toggle('umkd__content--open');
    }
}


document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll('.collapsible');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            toggleContent(button);
        });
    });
});

