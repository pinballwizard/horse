/**
 * Created by pinballwizard on 06.12.15.
 */

$(document).ready(function(){
    $('.button-collapse').sideNav();
    $('.modal-trigger').leanModal();
    $('select').material_select();

    $('.dropdown-button').dropdown({
        belowOrigin: true
    });

    $('.switch').change(function(){
        $(this).parents("form").submit();
    });
    // Настройка выбора даты
    $('.datepicker').pickadate({
        monthsFull: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        monthsShort: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
        weekdaysFull: ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'],
        weekdaysShort: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
        format: 'dd.mm.yyyy',
        // First day of the week
        firstDay: 'monday',
        // Date limits
        max: 'today',
        // Buttons
        today: 'Сегодня',
        clear: 'Очистить',
        close: 'Закрыть',
        // Accessibility labels
        labelMonthNext: 'Следующий',
        labelMonthPrev: 'Предыдущий',
        labelMonthSelect: 'Выбрать месяц',
        labelYearSelect: 'Выбрать год',
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 200 // Creates a dropdown of number years to control year
    });
});