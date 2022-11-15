
class Location():

    def __init__(self, location_name, location_deck):
        self.location_name = location_name  # Имя локации
        self.location_deck = location_deck  # Массив событий карты

    def location_event(self):
        event = self.location_deck[0]
        self.location_deck.remove(event)
        print(event)

loc_deck = ['66', '0', '1']
name = 'мангальная поляна'

new_location = Location(location_name=name, location_deck=loc_deck)


new_location.location_event()
new_location.location_event()
new_location.location_event()

