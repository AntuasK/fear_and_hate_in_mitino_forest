from game_function import print_text, player_examination, location_deck_ivent, mob_name_generation, get_change_location
from random import randint
from game_texts import lang_flag
import game_texts
import game_clases
import game_data



def start():
    """Функция инициализирует старт игры и предлагает игроку выбрать язык и пройти обучение"""

    # Модуль выбора языка\Вызываем функцию print_text
    print_text(game_texts.lang, lang_flag, 0, 1)
    switch_case = ['1', '2']
    player_in_clear = player_examination(switch_case)  # Вызываем функцию player_examination
    if player_in_clear == '1':
        game_texts.lang_flag = 0
    elif player_in_clear == '2':
        print_text(game_texts.lang, lang_flag, 2)  # Вызываем функцию print_text
        game_texts.lang_flag = 0  # Поменять этот параметр на 1 для реализации Английского языка
        # click.pause('Нажмите любую клавишу')
    else:
        print('В функции START что-то аварийно вернулось при выборе языка')

    # Блок создания экземпляра игрока

    # Приветственный текст
    print_text(game_texts.texts, lang_flag, 0, 1, 2)  # Вызываем функцию print_text

    # Модуль запроса обучения
    switch_case = ['1', '2']
    player_in_clear = player_examination(switch_case)  # Вызываем функцию player_examination

    if player_in_clear == '1':
        print('ЗАГЛУШКА: Игрок выбрал вариант ДА. ИДЕМ В БЛОК ОБУЧЕНИЯ. Но его пока нет, так что идем играть!')  # ВЫХОД ИЗ ФУНКЦИИ
        game_start()
    elif player_in_clear == '2':
        game_start()  # Вызываем функцию game_start! ВЫХОД ИЗ ФУНКЦИИ
    else:
        print('ЗАГЛУШКА: В функцию START Вернулось что-то непонятное')


def game_start():
    """Определяет стартовую локацию игрока, определяет кол-во событий карты, определяет события карты,
    принтует приветственный ЛОР карты (случайный из набора), переключает на функцию цикла игры"""

    # Блок работает
    location_name = game_data.location_name_full[lang_flag][randint(0, 5)]  # Определяем имя локации
    location_now.append(location_name)  # Добавляем локацию в список ИГРОК-ЗДЕСЬ
    location_open.append(location_name)  # Добавляем локацию в список открытых
    game_data.location_name_full[lang_flag].remove(location_name)  # Удаляем локацию из общего списка

    """Странный блок получился, он делает скрытые операции, но самую главную и большую 
    - создание последовательности событий мы запрашиваем на другом листе
    Надо с этим будет разобраться"""

    # Принтует вступительное слово и название локации
    print_text(game_texts.texts, lang_flag, 3, 4)
    print(
        f'{game_texts.texts_lor_all[lang_flag][randint(0, len(game_texts.texts_lor_all) - 1)]} {new_location.location_long_name()}')

    game()


def game():
    """Основной цикл игры: Заправшивает у игрока ответ, проверяет его, принтует статы и инвентарь, запрашивает событие
    перемещает игрока между локациями"""

    # Принтуем варианты
    print_text(game_texts.texts, lang_flag, 5, 6)

    # Запрашиваем ответ игрока
    switch_case = ['1', '2', '3', '4']
    player_in_clear = player_examination(switch_case)

    # Проверяем ответ
    if player_in_clear == '1':
        get_event_roll()
    elif player_in_clear == '2':
        print(player.print_sats())
        game()
    elif player_in_clear == '3':
        print('ЗАГЛУШКА: Принтуем ИНВЕНТАРЬ игрока из класса ИНВЕНТАРЬ')
        game()
    elif player_in_clear == '4':
        print(
            '\nЗАГЛУШКА: ПРОВЕРЯЕМ ЕСТЬ ЛИ В ПЕРЕМЕННОЙ ЛОКЕЙШН ОУПЕН БОЛЬШЕ 1 ЛОКАЦИИ, если да, переходим на выбор локации')
        get_change_location(location_now, location_open)

        game()
    else:
        print('В Функцию  GAME вернулось что-то непонятное')


def get_event_roll():
    """Функция вытягивает событие из колоды локации, переводит событие из цифры в текст, принтует его игроку"""
    # События карты:
    # 0 - ничего не происходит, 1 - ты встретил моба, 2 - некий саспенс
    # 3 - ты нашел лут, 4 - Ты наше какое-то послание, 5 - Ты нашел новую локацию

    event = new_location.get_location_event()
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
        get_new_location()
        game()
    else:
        print('\n\n\nАварийный выход из функции event!!!!!!!')


def get_new_location():
    """Определяет имя новой лолкации/удаялет имя из общего списка/добавляет локацию в список открытых/обновляет экземпляр"""
    global location_now
    global location_deck
    global new_location

    if len(game_data.location_name_full[lang_flag]) > 0:
        location_now.clear()
        location_now = [game_data.location_name_full[lang_flag][randint(0, len(game_data.location_name_full) - 1)]]
        location_open.append(location_now[0])
        game_data.location_name_full[lang_flag].remove(location_now[0])
        print_text(game_texts.texts_new_location_lor, lang_flag,
                   randint(0, len(game_texts.texts_new_location_lor[lang_flag]) - 1))
    else:
        location_now.clear()
        location_now = [location_open[randint(0, len(location_open) - 1)]]

    location_deck = location_deck_ivent(map_size, map_nothing_happens, map_mob, map_lut, map_saspiens, map_txt)
    new_location = game_clases.Location(location_now, location_deck)
    print(
        f'{game_texts.texts_lor_all[lang_flag][randint(0, len(game_texts.texts_lor_all) - 1)]} {new_location.location_long_name()}')
    pass


# Здесь будут располагаться все глобальные переменные
# Параметры карты, считается в процентах
map_size = 10  # Размер карты
map_nothing_happens = 0.45  # Ничего не происходит
map_mob = 0.25  # Мобы
map_lut = 0.05  # Лут
map_saspiens = 0.10  # Саспенс
map_txt = 0.05  # Тексты на карте

location_now = []  # Очищать перед добавлением нового списка
location_open = []
location_deck = location_deck_ivent(map_size, map_nothing_happens, map_mob, map_lut, map_saspiens,
                                    map_txt)

# Мобы
# Сюда сгружаются все имена мобов
mob_name_all = mob_name_generation(game_data.mob_name_1, game_data.mob_name_2, game_data.mob_name_3,
                                   lang_flag)  # Сюда сгружаются все имена мобов
# Параметры по которым будут создаваться мобы

# Создание экземпляров
new_location = game_clases.Location(location_now, location_deck)
player = game_clases.Player(health=100, str=1, dex=1)

# Старт программы
start()


print('Конец программы')
