from enum import Enum


class AnimalType(Enum):
    CAT = "Кіт/Кішка"
    DOG = "Собака"


class AnimalGender(Enum):
    MALE = "Самець"
    FEMALE = "Самка"


class AnimalStatus(Enum):
    WAITING = "Очікує"
    ADOPTED = "Усиновлений"
    UNAVAILABLE = "Недоступний"


class AnimalTag(str, Enum):
    # --- НОВЕ: РОЗМІР ---
    SIZE_SMALL = "маленький (до 30 см)"
    SIZE_MEDIUM = "середній (30–50 см)"
    SIZE_MEDIUM_PLUS = "середній+ (50–60 см)"
    SIZE_LARGE = "великий 60 см+"

    # --- НОВЕ: СТАТЬ ---
    GENDER_MALE = "хлопчик"
    GENDER_FEMALE = "дівчинка"

    # --- НОВЕ: ВІК ---
    AGE_UNDER_1 = "до 1 року"
    AGE_1_5 = "1–5 років"
    AGE_OVER_5 = "5 і більше років"

    # --- ТЕГИ (Інше) ---
    LOVES_LEARNING = "люблю вчитися"
    NEEDS_SOCIALIZATION = "потребую соціалізації"
    QUICK_TO_HANDS = "швидко йду на ручки"
    LOVES_CHILDREN = "люблю дітей"
    LOVES_ALL_PETS = "люблю чотирилапих"
    TURBO = "турбо"
    ACTIVE_LEISURE = "обожнюю активне дозвілля"
    PUREBRED = "породистий"

    # З попереднього списку (якщо потрібно залишити)
    WUNDERKIND = "вундеркінд"
    SERIOUS = "серйозний хвостик"
    ATTENTIVE = "уважний хвостик"
    COUCH_POTATO = "лежебока"
    ROCKET = "ракета"
    NEEDS_CARE = "мені потрібен догляд"
    ADULT = "дорослий хвостик"
    MIXED_BREED = "метис"

    def __str__(self):
        return self.value
