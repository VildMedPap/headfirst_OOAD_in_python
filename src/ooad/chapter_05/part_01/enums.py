from enum import Enum


class Type(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"


class Builder(Enum):
    ANY = "Any"
    COLLINGS = "Collings"
    FENDER = "Fender"
    GIBSON = "Gibson"
    MARTIN = "Martin"
    OLSON = "Olson"
    PRS = "Prs"
    RYAN = "Ryan"


class Wood(Enum):
    ADIRONDACK = "Adirondack"
    ALDER = "Alder"
    BRAZILIAN_ROSEWOOD = "Brazilian Rosewood"
    CEDAR = "Cedar"
    COCOBOLO = "Cocobolo"
    INDIAN_ROSEWOOD = "Indian Rosewood"
    MAHOGANY = "Mahogany"
    MAPLE = "Maple"
    SITKA = "Sitka"


class Style(Enum):
    A = "A"
    F = "F"
