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
    # --- НОВОЕ: РАЗМЕР (Розмір) ---
    SIZE_SMALL = "маленький (до 30см)"
    SIZE_MEDIUM = "середній (30-50см)"
    SIZE_MEDIUM_PLUS = "середній+ (50-60см)"
    SIZE_LARGE = "великий 60см+"

    # --- НОВОЕ: ПОЛ (Стать) ---
    GENDER_MALE = "хлопчик"
    GENDER_FEMALE = "дівчинка"

    # --- НОВОЕ: ВОЗРАСТ (Вік) ---
    AGE_UNDER_1 = "до 1 року"
    AGE_1_5 = "1-5 років"
    AGE_OVER_5 = "5 і більше років"

    # --- ТЕГИ (Інше) ---
    LOVES_LEARNING = "любить вчитися"
    NEEDS_SOCIALIZATION = "потребую соціалізації"
    QUICK_TO_HANDS = "швидко йду на ручки"
    LOVES_CHILDREN = "люблю дітей"
    LOVES_ALL_PETS = "люблю чотирилапих"
    TURBO = "турбо"  # Добавлено из нового скрина
    ACTIVE_LEISURE = "обожнюю активне дозвілля"
    PUREBRED = "породистий"

    # Из предыдущего списка (если нужно оставить)
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
