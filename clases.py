import random, text

# Локации
class Location:

    def __init__(self, location_name, location_deck):
        # Атрибуты класса
        self.location_name = location_name  # Имя локации\приходит список
        self.location_deck = location_deck  # Массив событий карты

        # Методы класса

    # Принтует текст при первом попадании на локацию
    def location_start_name_print(self):
        """Принтует название локации когда игрок появляется на ней впервые"""
        long_name = f'{text.texts_lor_all[random.randint(0, len(text.texts_lor_all) - 1)]} {self.location_name[0].title()}'
        print(long_name)
        pass

    # Возвращает верхнее событие из экземпляра класса
    def get_location_event(self):
        """Возвращает верхнее событие из событий карты"""
        event = self.location_deck[0]
        self.location_deck.remove(event)
        return event



