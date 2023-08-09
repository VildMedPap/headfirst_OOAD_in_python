from ooad.chapter_01.take_05.guitar_spec import GuitarSpec


class Guitar:
    def __init__(
        self,
        serial_number: str,
        price: float,
        spec: GuitarSpec,
    ) -> None:
        self.__serial_number = serial_number
        self.__price = price
        self.__spec = spec

    def get_serial_number(self) -> str:
        return self.__serial_number

    def get_price(self) -> float:
        return self.__price

    def set_price(self, new_price: float) -> None:
        self.__price = new_price

    def get_spec(self) -> GuitarSpec:
        return self.__spec
