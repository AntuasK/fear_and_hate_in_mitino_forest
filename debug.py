
class Location():

    def __init__(self, location_name, location_deck):
        self.location_name = location_name  # Имя локации
        self.location_deck = location_deck  # Массив событий карты

    def location_event(self):
        event = self.location_deck[0]
        self.location_deck.remove(event)
        name = self.location_name
        print(name)
        print(event)


a = 'Невиданная хрень'
b = ['44', '33', '55']
name_randon = a
deck_random = b

location = Location(name_randon, deck_random)
location.location_event()

a = 'Безумная темная дичь'
b = ['77', '88', '99']

name_randon = a
deck_random = b


new_location = Location(name_randon, deck_random)
new_location.location_event()


