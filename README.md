********Телефонный справочник _______Творец Агаев Теймур И.

________Задание 
в одного человека надо сделать консольное приложение Телефонный справочник с внешним хранилищем информации,
и чтоб был реализован основной функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.



________Описание
Простейшее консольное приложение, работающее с внешней БД, при помощи модуля json.
Помимо ввода с консоли, можно редактировать файл *phonebook* самостоятельно заполняя БД,
однако стоит помить, что **vsego_id** это счетчик который должен ровнятся последнему введеному ID,
например, если вы привязываете телефонную книгу к табельным номерам, то значение **vsego_id** должно
быть равно самому крайнему табельному. При вводе с консоле, *phonebook* создасться автоматически,
и заполнение id начнется с 1, если вам необходимо чтобы id начиналось с другого значения, редактируте 
значение **vsego_id**
Программа сохраняет всё в автоматическом режиме.



________Запуск
Для запуска необходимо открыть файл Spravochnik.py




