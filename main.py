from game_function import print_text, player_examination, location_deck_ivent, mob_name_generation, \
    get_change_location
from random import randint
from game_texts import lang_flag
import game_texts
import game_clases
import game_data
import game_define


def start():
    """Функция инициализирует старт игры и предлагает игроку выбрать язык и пройти обучение"""

    # Модуль выбора языка\Вызываем функцию print_text
    print_text(game_texts.lang, lang_flag, 0, 1)
    switch_case = ['1', '2']
    player_in_clear = player_examination(switch_case)  # Вызываем функцию player_examination
    if player_in_clear == game_define.B:
        game_texts.lang_flag = 0
    elif player_in_clear == game_define.C:
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

    if player_in_clear == game_define.B:
        print(
            'ЗАГЛУШКА: Игрок выбрал вариант ДА. ИДЕМ В БЛОК ОБУЧЕНИЯ. Но его пока нет, так что идем играть!')  # ВЫХОД ИЗ ФУНКЦИИ
        game()
    elif player_in_clear == game_define.C:
        print_text(game_texts.texts, lang_flag, 3, 4)
        print(
            f'{game_texts.texts_lor_all[lang_flag][randint(0, len(game_texts.texts_lor_all) - 1)]} {new_location.location_long_name()}')
        game()
    else:
        print('ЗАГЛУШКА: В функцию START Вернулось что-то непонятное')


def game():
    """Основной цикл игры: Заправшивает у игрока ответ, проверяет его, принтует статы и инвентарь, запрашивает событие
    перемещает игрока между локациями"""

    # Принтуем варианты
    print_text(game_texts.texts, lang_flag, 5, 6)

    # Запрашиваем ответ игрока
    switch_case = ['1', '2', '3', '4']
    player_in_clear = player_examination(switch_case)

    # Проверяем ответ
    if player_in_clear == game_define.B:
        get_event_roll()
    elif player_in_clear == game_define.C:
        print(player.print_sats())
        game()
    elif player_in_clear == game_define.D:
        print('ЗАГЛУШКА: Принтуем ИНВЕНТАРЬ игрока из класса ИНВЕНТАРЬ')
        game()
    elif player_in_clear == game_define.E:
        if len(location_open) == 1:
            print(f'\n{game_texts.texts_location_now[lang_flag][2]} {new_location.location_long_name()}\n')
            game()
        elif len(location_open) > 1:
            print('\n')
            # Ты находишься здесь
            print(
                f'{game_texts.texts_location_now[lang_flag][randint(3, len(game_texts.texts_location_now[lang_flag]) - 1)]} {new_location.location_long_name()}\n')
            a = get_change_location(location_now, location_open)
            if a == game_define.A:
                print('\n')
                game()
            else:
                a = int(a)
                get_new_location(a)
                print(
                    f'{game_texts.texts_location_teleport[lang_flag][randint(3, len(game_texts.texts_location_teleport[lang_flag]) - 1)]} {new_location.location_long_name()}\n')
                game()

    else:
        print('В Функцию  GAME вернулось что-то непонятное')


def get_event_roll():
    """Функция вытягивает событие из колоды локации, переводит событие из цифры в текст, принтует его игроку"""
    # События карты:
    # 0 - ничего не происходит, 1 - ты встретил моба, 2 - некий саспенс
    # 3 - ты нашел лут, 4 - Ты наше какое-то послание, 5 - Ты нашел новую локацию

    event = new_location.get_location_event()
    if event == game_define.A:
        print('\nНичего не происходит\n')
        game()
    elif event == game_define.B:
        print('\nТы встретил моба - уходим определять моба\n')
        game()
    elif event == game_define.C:
        print('\nНекий саспенс - уходим определять саспенс\n')
        game()
    elif event == game_define.D:
        print('\nТы нашел лут - уходим определять лут\n')
        game()
    elif event == game_define.E:
        print('\nТы нашел какое-то послание - уходим определять послание\n')
        game()
    elif event == game_define.F:
        get_new_location(a=game_define.N)
        game()
    else:
        print('\n\n\nАварийный выход из функции event!!!!!!!')


def get_new_location(a):
    """Принимает 1 параметр: Определяет имя новой лолкации/удаялет имя из общего списка/добавляет локацию в список открытых/обновляет экземпляр/
    Забирает индекс из списка ОУПЕН создает новую последовательность и экземпляр локации"""
    global location_open
    global location_now
    global location_deck
    global new_location

    if a == game_define.N:
        # Стартовая локация
        if len(location_open) == game_define.A:
            index_start_location = int(randint(0, 5))
            location_open.append(index_start_location)
            location_now.append(index_start_location)

        # Локации которые еще не открыты
        elif len(game_data.location_name_full[lang_flag]) != len(location_open):
            index_new_location = int(randint(0, len(game_data.location_name_full[lang_flag]) - 1))

            if index_new_location in location_open:
                get_new_location(game_define.N)
                print('ЗАГЛУШКА: Пытаемся найти новый индекс которого нет в ЛОКЕЙШН ОУПЕН!')
                pass
            else:
                location_now.clear()
                location_open.append(index_new_location)
                location_now.append(index_new_location)

        # Случайная локация которую находит игрок после того, как открыл все доступные
        elif len(game_data.location_name_full[lang_flag]) == len(location_open):
            index_back_location = randint(0, len(game_data.location_name_full[lang_flag]) - 1)
            if index_back_location in location_now:
                print('ВЫБРАННАЯ ЛОКАЦИЯ СОВПАДАЕТ С ТЕКУЩЕЙ! ИЩЕМ ЕЩЕ РАЗ')
                get_new_location(game_define.N)
                pass
            else:
                location_now.clear()
                location_now.append(index_back_location)
        else:
            print('ПРИ ФОРМИРОВАНИИ ЛОКАЦИИ ПРОИЗОШЛО ЧТО_ТО НЕВНЯТНОЕ! ФУНКЦИЯ ГЕТ НЬЮ ЛОКЕЙШН')

        location_deck = location_deck_ivent(map_size, map_nothing_happens, map_mob, map_lut, map_saspiens, map_txt)
        new_location = game_clases.Location(game_data.location_name_full[lang_flag][location_now[-1]], location_deck)
        print(
            f'{game_texts.texts_lor_all[lang_flag][randint(0, len(game_texts.texts_lor_all) - 1)]} {new_location.location_long_name()}')
        pass

    # Сюда должен прийти индекс ЛОКЕЙШН ОУПЕН
    elif a >= 0:
        location_now.clear()
        location_now.append(a)
        location_deck = location_deck_ivent(map_size, map_nothing_happens, map_mob, map_lut, map_saspiens, map_txt)
        new_location = game_clases.Location(game_data.location_name_full[lang_flag][location_now[-1]], location_deck)
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


# Создание первого экземпляра локации
location_name = int(randint(0, 4))
location_now.append(location_name)
location_open.append(location_name)
new_location = game_clases.Location(game_data.location_name_full[lang_flag][location_now[-1]], location_deck)

# Создание экземпляра игрок
player = game_clases.Player(health=100, str=1, dex=1)

# Старт программы
start()

print('Конец программы')
