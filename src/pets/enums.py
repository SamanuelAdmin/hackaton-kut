from enum import Enum


class AnimalType(Enum):
    CAT = "Кот/Кошка"
    DOG = "Собака"

class AnimalGender(Enum):
    MALE = "Самец"
    FEMALE = "Самка"

class AnimalStatus(Enum):
    WAITING = "Ожидает"
    ADOPTED = "Усыновлен"
    UNAVAILABLE = "Недоступен"

class AnimalTag(str, Enum):
    # Характер и обучение
    LOVES_LEARNING = "люблю вчитися"
    WUNDERKIND = "вундеркінд"
    SERIOUS = "серйозний хвостик"
    ATTENTIVE = "уважний хвостик"

    # Социализация и общение
    NEEDS_SOCIALIZATION = "потребую соціалізації"
    LOVES_CHILDREN = "люблю дітей"
    LOVES_ALL_PETS = "люблю всіх чотирилапих"
    QUICK_TO_HANDS = "швидко йду на ручки"

    # Активность
    ACTIVE_LEISURE = "обожнюю активне дозвілля"
    ROCKET = "ракета"
    COUCH_POTATO = "лежебока"

    # Статус и здоровье
    NEEDS_CARE = "мені потрібен догляд"
    ADULT = "дорослий хвостик"
    PUREBRED = "породистий хвостик"
    MIXED_BREED = "метис"

    def __str__(self):
        return self.value