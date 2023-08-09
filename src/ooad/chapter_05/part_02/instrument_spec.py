from typing import Any


class InstrumentSpec:
    def __init__(self, properties: dict[str, Any]) -> None:
        if properties:
            self.__properties = properties
        else:
            self.__properties = {}

    def get_property(self, property: str) -> Any:
        return self.__properties.get(property)

    def get_properties(self) -> dict[str, Any]:
        return self.__properties

    def matches(self, other_spec: "InstrumentSpec") -> bool:
        for property_name, property_value in other_spec.get_properties().items():
            if self.__properties.get(property_name) != property_value:
                return False

        return True
