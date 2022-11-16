import random


def player_examination(switch_case):
    """Функция принимает список доступных ответов, принимает ответ пользователя.
    Запрашивает до тех пор, пока ответ не будет корректным и находиться в списке доступных.
    Возвращает, корректный ответ пользователя str()"""
    while True:
        player_in = input('Введите свой ответ: ')
        if player_in.isdigit() and (player_in in switch_case):
            break
        else:
            print('Нет доступных вариантов. Введите свой ответ корректно.')
    return player_in


def print_text(list_t, *args):
    """Функция принимает имя листа откуда нужно забрать текст,
     принимает последовательность индексов - принтует из массива по полученным индексам"""
    for i in args:
        if len(list_t[i]) > 250:  # Кол-во символов
            print(list_t[i])
            # time.sleep(3.0)
        else:
            print(list_t[i])
            # time.sleep(0.5)


def location_deck_ivent():
    """Функция формирует события карты согласно плану и размеру. Возвращает перемешанный список событий"""

    """Правила формирования карты: Ничего не происходит - 45% Мобы- 25% Ты что-то нашел - 5%
        Саспенс - 10% Текст - 5% Остаток случайные события генерируемые по остатку"""

    """Создал эту функцию отдельно, т.к она будет делать карты далее, в моей голове"""

    # Размер карты
    location_deck_size = 30  # Этот параметр будет случайным

    # События карты:
    # 0 - ничего не происходит, 1 - ты встретил моба, 2 - некий саспенс
    # 3 - ты нашел лут, 4 - Ты наше какое-то послание, 5 - Ты нашел новую локацию
    ivent = ['0', '1', '2', '3', '4']
    # Возвращаемый список
    out = []

    # Определяем кол-во событий
    nothing_happens = round(0.45 * location_deck_size)
    mob = round(0.25 * location_deck_size)
    lut = round(0.05 * location_deck_size)
    saspiens = round(0.10 * location_deck_size)
    txt = round(0.05 * location_deck_size)

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

    random.shuffle(out)
    # Добавляем финал локации
    location_end = '5'
    out.append(location_end)

    return out  # ВЫХОД ИЗ ФУНКЦИИ


