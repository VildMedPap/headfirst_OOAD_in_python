from ooad.chapter_07.units.unit import Unit


class Tile:
    def __init__(self) -> None:
        self.__units: list[Unit | None] = []

    def _add_unit(self, unit: Unit) -> None:
        self.__units.append(unit)

    def _remove_unit(self, unit: Unit) -> None:
        self.__units.remove(unit)

    def _remove_units(self) -> None:
        self.__units.clear()

    def _get_units(self) -> list[Unit | None]:
        return self.__units
