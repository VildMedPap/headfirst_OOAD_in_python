from ooad.chapter_05.part_02.instrument_spec import InstrumentSpec


class Instrument:
    def __init__(self, serial_number: str, price: float, spec: InstrumentSpec) -> None:
        self.__serial_number = serial_number
        self.__price = price
        self.__spec = spec

    def get_serial_number(self) -> str:
        return self.__serial_number

    def get_price(self) -> float:
        return self.__price

    def set_price(self, new_price: float) -> None:
        self.__price = new_price

    def get_spec(self) -> InstrumentSpec:
        return self.__spec
