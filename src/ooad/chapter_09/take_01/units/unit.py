from typing import Any

from ooad.chapter_09.take_01.units.weapon import Weapon


class Unit:
    __type: str
    __id: int
    __name: str
    __weapons: list[Weapon] | None = None
    __properties: dict[str, Any] | None = None

    def __init__(self, id: int) -> None:
        self.__id = id

    def get_id(self) -> int:
        return self.__id

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_name(self) -> str:
        return self.__name

    def set_type(self, new_type: str) -> None:
        self.__type = new_type

    def get_type(self) -> str:
        return self.__type

    def add_weapon(self, weapon: Weapon) -> None:
        if not self.__weapons:
            self.__weapons = []
        self.__weapons.append(weapon)

    def get_weapons(self) -> list[Weapon] | None:
        return self.__weapons

    def set_property(self, property: str, value: Any) -> None:
        if not self.__properties:
            self.__properties = {}
        self.__properties[property] = value

    def get_property(self, property: str) -> Any | None:
        if self.__properties:
            return self.__properties.get(property, None)
        else:
            return None
