from ooad.chapter_01.take_04.enums import Builder, Type, Wood
from ooad.chapter_01.take_04.guitar import Guitar
from ooad.chapter_01.take_04.guitar_spec import GuitarSpec


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
        back_wood: Wood,
        top_wood: Wood,
    ) -> None:
        guitar = Guitar(serial_number, price, builder, model, type, back_wood, top_wood)
        self.__guitars.append(guitar)

    def get_guitar(self, serial_number: str) -> Guitar | None:
        for guitar in self.__guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar

        return None

    def search_guitar(self, search_spec: GuitarSpec) -> list[Guitar] | None:
        matching_guitars: list[Guitar] = []

        for guitar in self.__guitars:
            # Ignore serial number since that’s unique
            # Ignore price since that’s unique
            guitar_spec = guitar.get_spec()
            if search_spec.get_builder() != guitar_spec.get_builder():
                continue

            model = search_spec.get_model().lower()
            if model and model != guitar_spec.get_model().lower():
                continue

            if search_spec.get_type() != guitar_spec.get_type():
                continue

            if search_spec.get_back_wood() != guitar_spec.get_back_wood():
                continue

            if search_spec.get_top_wood() != guitar_spec.get_top_wood():
                continue

            matching_guitars.append(guitar)

        return matching_guitars
