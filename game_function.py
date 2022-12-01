from random import shuffle
"""Все функции проекта, внтури каждой есть докстринг"""


def player_examination(switch_case):
    """Функция принимает список доступных ответов, принимает ответ пользователя.
    Запрашивает до тех пор, пока ответ не будет корректным и находиться в списке доступных.
    Возвращает, корректный ответ пользователя str()"""
    # Ответ должен содержать не более 2-х символов, ответ не должен содержать пробелов
    while True:
        player_in = input('Введите свой ответ: ')
        if player_in.isdigit() and (player_in in switch_case):
            break
        else:
            print('Нет доступных вариантов. Введите свой ответ корректно.')
    return player_in


def print_text(list_t, lang_flag, *args):
    """Функция принимает имя листа откуда нужно забрать текст,
     принимает последовательность индексов - принтует из массива по полученным индексам"""
    for i in args:
        if len(list_t[lang_flag][i]) > 250:  # Кол-во символов
            print(list_t[lang_flag][i])
            # time.sleep(3.0)
        else:
            print(list_t[lang_flag][i])
            # time.sleep(0.5)


def location_deck_ivent(map_size, map_nothing_happens, map_mob, map_lut, map_saspiens, map_txt):
    """Функция формирует события карты согласно плану и размеру. Возвращает перемешанный список событий"""
    """Правила формирования карты: Ничего не происходит - 45% Мобы- 25% Ты что-то нашел - 5%
        Саспенс - 10% Текст - 5% Остаток случайные события генерируемые по остатку"""

    # Размер карты
    location_deck_size = map_size  # Этот параметр будет случайным

    # События карты:
    # 0 - ничего не происходит, 1 - ты встретил моба, 2 - некий саспенс
    # 3 - ты нашел лут, 4 - Ты наше какое-то послание, 5 - Ты нашел новую локацию
    ivent = ['0', '1', '2', '3', '4']
    # Возвращаемый список
    out = []

    # Определяем кол-во событий
    nothing_happens = round(map_nothing_happens * location_deck_size)
    mob = round(map_mob * location_deck_size)
    lut = round(map_lut * location_deck_size)
    saspiens = round(map_saspiens * location_deck_size)
    txt = round(map_txt * location_deck_size) #+ 1  # Эта фигня будет работать только если на локации есть хотя бы 1 текст

    # Добавляет события в список out
    while txt > 0:
        if nothing_happens > 0:
            out.append(ivent[0])
            nothing_happens = nothing_happens - 1
            continue
        elif mob > 0:
            out.append(ivent[1])
            mob = mob - 1
            continue
        elif lut > 0:
            out.append(ivent[2])
            lut = lut - 1
            continue
        elif saspiens > 0:
            out.append(ivent[3])
            saspiens = saspiens - 1
        elif txt > 0:
            out.append(ivent[4])
            txt = txt - 1
            continue
        else:
            print('Аварийный выход из цикла')
            break

    shuffle(out)
    # Добавляем финал локации
    location_end = '5'
    out.append(location_end)

    return out  # ВЫХОД ИЗ ФУНКЦИИ


def mob_name_generation(mob_name_1, mob_name_2, mob_name_3, lang_flag):
    """Принимает три списка имен мобов - возвращает перемешанный список имен мобов, где каждый индекс - это конкретный моб"""
    """Всего в списке 27к имен, весит все это 220кб, предполагается, что при создании персонажа, 
        этот спсиок будет создаваться на стороне сервера и загружаться в базу конкретного игрока, при встрече с мобом 
        из него будет доставаться случайный индекс и удаляться из общего котла"""
    m_n_1 = mob_name_1
    m_n_2 = mob_name_2
    m_n_3 = mob_name_3
    l_f = lang_flag

    mob_name_list = []

    for i in m_n_1[l_f]:
        for o in m_n_2[l_f]:
            for p in m_n_3[l_f]:
                m_n = [i.title(), o, p]
                mob_name_list.append(' '.join(m_n))
    shuffle(mob_name_list)

    return mob_name_list


def get_change_location(now_loc, open_loc):
    """Функция создает список открытых локаций и предлагает игроку переместится в одну из них"""
    # Добавитьт: Ты сейчас находишься здесь!
    # Куда хочешь пойти - далее список
    # Создать мэп лист, или добавить в словарь индекс из списка локейшн оупен
    # Сделать что-то с разделением блоков НАЗАД и ЧТО БУДЕШЬ ДЕЛАТЬ

    list_now = now_loc
    list_open = open_loc

    if len(open_loc) > 1:
        for i in list_open:
            if i == list_now[0]:
                list_open.remove(i)

        location_open_dict = {}
        location_open_index_dict = {}

        # Создаем словарь для принтовки доступных локаций
        n = 0
        for z in range(1, len(list_open) + 1):
            location_open_dict[z] = list_open[n]
            n += 1

        print(list_open)

        # Создаем словарь для хранения индексов
        for i in list_open:
            location_open_index_dict[i] = list_open.index(i)

        print(location_open_index_dict)


        location_open_dict[0] = 'назад'  # Заменить на переменную с языком

        # формируем свитчкейс из ключей словаря
        switch_case = []
        for x in range(1, len(location_open_dict) + 1):
            switch_case.append(str(x))

        switch_case.append(str(0))

        # циклом фор принтуем каждое значение словаря
        for i in location_open_dict:
            a = f'{i} - {location_open_dict[i].title()}'
            print(a)

        player_in_clear = player_examination(switch_case)

        if player_in_clear == '0':
            return
        else:

            print('Идем создавать новую локацию по номеру')
    else:
        print('Нет доступных локаций для перемещения')






