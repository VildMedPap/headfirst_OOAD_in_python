from ooad.chapter_01.take_05.enums import Builder, Type, Wood
from ooad.chapter_01.take_05.guitar import Guitar
from ooad.chapter_01.take_05.guitar_spec import GuitarSpec


class Inventory:
    def __init__(self) -> None:
        self.__guitars: list[Guitar] = []

    def add_guitar(
        self,
        serial_number: str,
        price: float,
        builder: Builder,
        model: str,
        type: Type,
        num_strings: int,
        back_wood: Wood,
        top_wood: Wood,
    ) -> None:
        guitar_spec = GuitarSpec(builder, model, type, num_strings, back_wood, top_wood)
        guitar = Guitar(serial_number, price, guitar_spec)
        self.__guitars.append(guitar)

    def get_guitar(self, serial_number: str) -> Guitar | None:
        for guitar in self.__guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar

        return None

    def search_guitar(self, search_spec: GuitarSpec) -> list[Guitar] | None:
        matching_guitars: list[Guitar] = []

        for guitar in self.__guitars:
            if guitar.get_spec().matches(search_spec):
                matching_guitars.append(guitar)

        return matching_guitars
