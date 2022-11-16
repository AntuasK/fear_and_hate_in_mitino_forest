import player_data
import function
import game_data
import random
import text


def start():
    """Функция инициализирует старт игры и предлагает игроку выбрать язык и пройти обучение"""

    # Модуль выбора языка\Вызываем функцию print_text
    function.print_text(text.lang, 0, 1)
    switch_case = ['1', '2']
    player_in_clear = function.player_examination(switch_case)  # Вызываем функцию player_examination
    if player_in_clear == '1':
        text.lang_flag = 0
    elif player_in_clear == '2':
        function.print_text(text.lang, 2)  # Вызываем функцию print_text
        text.lang_flag = 0  # Поменять этот параметр на 1 для реализации Английского языка
        # click.pause('Нажмите любую клавишу')
    else:
        print('В функции START что-то аварийно вернулось при выборе языка')

    # Приветственный текст
    function.print_text(text.texts[text.lang_flag], 0, 1, 2)  # Вызываем функцию print_text

    # Модуль запроса обучения
    switch_case = ['1', '2']
    player_in_clear = function.player_examination(switch_case)  # Вызываем функцию player_examination

    if player_in_clear == '1':
        print('ЗАГЛУШКА: Игрок выбрал вариант ДА. ИДЕМ В БЛОК ОБУЧЕНИЯ')  # ВЫХОД ИЗ ФУНКЦИИ
    elif player_in_clear == '2':
        game_start()  # Вызываем функцию game_start! ВЫХОД ИЗ ФУНКЦИИ
    else:
        print('ЗАГЛУШКА: В функцию START Вернулось что-то непонятное')


def game_start():
    """Определяет стартовую локацию игрока, определяет кол-во событий карты, определяет события карты,
    принтует приветственный ЛОР карты (случайный из набора), переключает на функцию цикла игры"""

    # Блок работает
    location_name = game_data.location_name_full[random.randint(0, 5)]  # Определяем имя локации
    player_data.location_now.append(location_name)  # Добавляем локацию в список ИГРОК-ЗДЕСЬ
    player_data.location_open.append(location_name)  # Добавляем локацию в список открытых
    game_data.location_name_full.remove(location_name)  # Удаляем локацию из общего списка

    """Странный блок получился, он делает скрытые операции, но самую главную и большую 
    - создание последовательности событий мы запрашиваем на листе bd
    Надо с этим будет разобраться"""

    # Принтует вступительное слово и название локации
    function.print_text(text.texts[text.lang_flag], 3, 4)
    player_data.start_location.location_start_name_print()

    game()


def game():
    """Основной цикл игры: Заправшивает у игрока ответ, проверяет его, принтует статы и инвентарь, запрашивает событие
    перемещает игрока между локациями"""

    # Принтуем варианты
    function.print_text(text.texts[text.lang_flag], 5, 6)

    # Запрашиваем ответ игрока
    switch_case = ['1', '2', '3', '4']
    player_in_clear = function.player_examination(switch_case)

    # Проверяем ответ
    if player_in_clear == '1':
        get_event_roll()
    elif player_in_clear == '2':
        print('ЗАГЛУШКА: Принтуем СТАТЫ игрока из класса ПЛЕЕР')
    elif player_in_clear == '3':
        print('ЗАГЛУШКА: Принтуем ИНВЕНТАРЬ игрока из класса ИНВЕНТАРЬ')
    elif player_in_clear == '4':
        print(
            'ЗАГЛУШКА: ПРОВЕРЯЕМ ЕСТЬ ЛИ В ПЕРЕМЕННОЙ ЛОКЕЙШН ОУПЕН БОЛЬШЕ 1 ЛОКАЦИИ, если да, переходим на выбор локации')
    else:
        print('В Функцию  GAME вернулось что-то непонятное')

def get_event_roll():
    """Функция вытягивает событие из колоды локации, переводит событие из цифры в текст, принтует его игроку"""
    # События карты:
    # 0 - ничего не происходит, 1 - ты встретил моба, 2 - некий саспенс
    # 3 - ты нашел лут, 4 - Ты наше какое-то послание, 5 - Ты нашел новую локацию

    event = player_data.start_location.get_location_event()
    if event == '0':
        print('\nНичего не происходит\n')
        game()
    elif event == '1':
        print('\nТы встретил моба - уходим определять моба\n')
        game()
    elif event == '2':
        print('\nНекий саспенс - уходим определять саспенс\n')
        game()
    elif event == '3':
        print('\nТы нашел лут - уходим определять лут\n')
        game()
    elif event == '4':
        print('\nТы нашел какое-то послание - уходим определять послание\n')
        game()
    elif event == '5':
        print('\nТы нашел новую локацию - уходим определять локации\n')
    else:
        print('\n\n\nАварийный выход из функции event!!!!!!!')



# Вход в функцию, старт игры
start()
#game_start()

print('Конец программы')
