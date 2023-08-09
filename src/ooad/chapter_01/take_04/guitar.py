from ooad.chapter_01.take_04.enums import Builder, Type, Wood
from ooad.chapter_01.take_04.guitar_spec import GuitarSpec


class Guitar:
    def __init__(
        self,
        serial_number: str,
        price: float,
        builder: Builder,
        model: str,
        type: Type,
        back_wood: Wood,
        top_wood: Wood,
    ) -> None:
        self.__serial_number = serial_number
        self.__price = price
        self.__spec = GuitarSpec(builder, model, type, back_wood, top_wood)

    def get_serial_number(self) -> str:
        return self.__serial_number

    def get_price(self) -> float:
        return self.__price

    def set_price(self, new_price: float) -> None:
        self.__price = new_price

    def get_spec(self) -> GuitarSpec:
        return self.__spec
