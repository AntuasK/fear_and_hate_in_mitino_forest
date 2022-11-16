import clases, function

"""Специальный файл где хранятся глобальные данные об игроке, его местоположении....."""

location_now = [] # Очищать перед добавлением нового списка
location_open = []
location_deck = function.location_deck_ivent() # На всякий случай очищать перед вызовом фуункции

start_location = clases.Location(location_now, location_deck)

new_location = clases.Location(location_name=location_now, location_deck=location_deck)



