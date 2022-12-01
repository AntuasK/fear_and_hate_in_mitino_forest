import game_texts
from game_texts import lang_flag
from random import randint




# Локации
class Location:

    def __init__(self, location_name, location_deck):
        print('Инициализируем новый экземпляр ЛОКАЦИИ')
        # Атрибуты класса
        self.location_name = location_name  # Имя локации\приходит список
        self.location_deck = location_deck  # Массив событий карты

    def location_long_name(self):
        """Форматирует имя локации"""
        long_name = self.location_name[0].title()
        return long_name

    # Выводит имя локации где сейчас находится игрок
    def location_name_now_print(self):
        a = f'\nМесто вокруг тебя называется {self.location_name[0].title()}'
        return a

    # Возвращает верхнее событие из экземпляра класса
    def get_location_event(self):
        """Возвращает верхнее событие из событий карты"""
        event = self.location_deck[0]
        self.location_deck.remove(event)
        return event

    def location_back_print(self):
        long_name = f'{game_texts.texts_location_back[randint(0, len(game_texts.texts_location_back) - 1)]} {self.location_name[0].title()}'
        print(long_name)
        pass


    def __del__(self):
        """Удаляет созданный экземпляр"""
        return


class Player:

    def __init__(self, health, str, dex):
        # пока будем опереировать только 3 параметрами
        self.health = health
        self.str = str
        self.dex = dex

    # Вывод всех статов
    def print_sats(self):
        """Принтует ужасный внутренний монолог и статы игрока"""
        stat = f'\n{game_texts.texts_stats_all[lang_flag][randint(0, len(game_texts.texts_stats_all[lang_flag]) - 1)]}'\
               f'{game_texts.texts_player_stats[lang_flag][0]} {self.health}\n' \
               f'{game_texts.texts_player_stats[lang_flag][1]} {self.str}\n' \
               f'{game_texts.texts_player_stats[lang_flag][2]} {self.dex}\n'
        return stat

    # Метод уменьшения/увеличения здоровья. Здоровье не больше 100
    # Метод увеличения/уменьшения статов
