from ooad.chapter_01.take_01.guitar import Guitar


class Inventory:
    def __init__(self) -> None:
        self.__guitars: list[Guitar] = []

    def add_guitar(
        self,
        serial_number: str,
        price: float,
        builder: str,
        model: str,
        type: str,
        back_wood: str,
        top_wood: str,
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
            builder = search_guitar.get_builder()
            if builder and builder != guitar.get_builder():
                continue

            model = search_guitar.get_model()
            if model and model != guitar.get_model():
                continue

            type = search_guitar.get_type()
            if type and type != guitar.get_type():
                continue

            back_wood = search_guitar.get_back_wood()
            if back_wood and back_wood != guitar.get_back_wood():
                continue

            top_wood = search_guitar.get_top_wood()
            if top_wood and top_wood != guitar.get_top_wood():
                continue

            return guitar

        return None
