from typing import Any


class Unit:
    def __init__(self, type: str, properties: dict[str, Any]) -> None:
        self.__type = type
        if properties:
            self.__properties = properties
        else:
            self.__properties = {}

    def get_type(self) -> str:
        return self.__type

    def set_type(self, new_type: str) -> None:
        self.__type = new_type

    def get_property(self, property: str) -> Any:
        return self.__properties.get(property)

    def get_properties(self) -> dict[str, Any]:
        return self.__properties
