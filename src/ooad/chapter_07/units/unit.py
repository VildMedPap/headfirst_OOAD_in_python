from typing import Any


class Unit:
    def __init__(self, type: str, properties: dict[str, Any]) -> None:
        self.__type = type
        if properties:
            self.__properties = properties
        else:
            self.__properties = {}

    def set_type(self, new_type: str) -> None:
        self.__type = new_type

    def get_type(self) -> str:
        return self.__type

    def set_property(self, property: str, value: Any) -> None:
        self.__properties[property] = value

    def get_property(self, property: str) -> Any:
        return self.__properties.get(property)
