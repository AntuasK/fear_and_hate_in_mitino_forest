import random, text

# Персонаж/Игрок
class Player:
    def __init__(self, health, strength, dextery, armor, damage, point):
        self.health = health  # Здоровье
        self.strength = strength  # Сила
        self.dextery = dextery  # Ловкость
        self.armor = armor  # Защита
        self.damage = damage  # Урон
        self.point = point  # Очки опыта

    # Методы класса для работы с каждым атрибутом

    # Принтовка статов
    def print_stat(self):
        print(f'Твое здоровье: {self.health}')
        print(f'Твоя сила: {self.strength}')
        print(f'Твоя ловкость: {self.dextery}')
        print(f'Твоя защита: {self.armor}')
        print(f'Твой урон: {self.damage}')
        print(f'Твои качки опыта: {self.point}')

    # Метод повышения и понижения здоровья
    def health_change(self):
        print('Здесь отнимается и прибавляется здоровье! Здоровье не может быть больше 100')

    # Метод повышения и понижения Силы
    def strength_change(self):
        print('Здесь отнимается и прибавляется сила! Сила не может быть меньше одного')

    # Метод повышения и понижения ловкости
    def dextery_change(self):
        print('Здесь отнимается и прибавляется ловкость! Ловкость не может быть меньше одного')

    # Метод повышения и понижения брони
    def armor_change(self):
        print('Здесь отнимается и прибавляется броня! Броня не может быть меньше одного')

    # Метод повышения и понижения урона
    def damage_change(self):
        print('Здесь отнимается и прибавляется урон! Урон не может быть меньше одного')

    # Метод повышения опыта
    def point_change(self):
        print('Здесь прибавляются ОЧКИ ОПЫТА! ОПЫТ не может уменьшаться')


# Мобы
class Mob:
    def __init__(self, mob_name, mob_health, mob_strength, mob_dextery, mob_armor, mob_damage):
        self.mob_name = mob_name
        self.mob_health = mob_health
        self.mob_strenght = mob_strength
        self.mob_dextery = mob_dextery
        self.mob_armor = mob_armor
        self.mob_damage = mob_damagea


# Инвентарь
class Inventory:
    # Возможно стоит разделить все эти вещи на разные классы???????
    def __init__(self, head_name, head_stat, head_value,
                 arms_name, arms_stat, arms_value,
                 body_name, body_stat, body_value,
                 legs_name, legs_stat, legs_value,
                 weapon_name, weapon_stat, weapon_value):
        # Инвентарная вещь которая надевается на голову
        self.head_name = head_name
        self.head_stat = head_stat
        self.head_value = head_value

        # Инвентарная вещь которая надевается на тело
        self.arms_name = arms_name
        self.arms_stat = arms_stat
        self.arms_value = arms_value

        # Инвентарная вещь которая надевается на руки
        self.body_name = body_name
        self.body_stat = body_stat
        self.body_value = body_value

        # Инвентарная вещь которая надевается на ноги
        self.legs_name = legs_name
        self.legs_stat = legs_stat
        self.legs_value = legs_value

        # Инвентарная вещь оружие
        self.weapon_name = weapon_name
        self.weapon_stat = weapon_stat
        self.weapon_value = weapon_value


# Локации
class Location:
    def __init__(self, location_name, location_deck):
        # Атрибуты класса
        self.location_name = location_name  # Имя локации
        self.location_deck = location_deck  # Массив событий карты

        # Методы класса

    # Принтует текст при первом попадании на локацию
    def location_start_name_print(self):
        """Принтует название локации когда игрок появляется на ней впервые"""
        long_name = f'{text.texts_lor_all[random.randint(0, len(text.texts_lor_all) - 1)]} {self.location_name.title()}'
        return long_name
        pass



