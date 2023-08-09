from ooad.chapter_01.take_02.enums import Builder, Type, Wood
from ooad.chapter_01.take_02.guitar import Guitar


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

    def search_guitar(self, search_guitar: Guitar) -> Guitar | None:
        for guitar in self.__guitars:
            # Ignore serial number since that’s unique
            # Ignore price since that’s unique
            if search_guitar.get_builder() != guitar.get_builder():
                continue

            model = search_guitar.get_model().lower()
            if model and model != guitar.get_model().lower():
                continue

            if search_guitar.get_type() != guitar.get_type():
                continue

            if search_guitar.get_back_wood() != guitar.get_back_wood():
                continue

            if search_guitar.get_top_wood() != guitar.get_top_wood():
                continue

            return guitar

        return None
