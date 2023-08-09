from ooad.chapter_09.take_03.units.unit import Unit


class Tile:
    def __init__(self) -> None:
        self.__units: list[Unit | None] = []

    def _add_unit(self, unit: Unit) -> None:
        self.__units.append(unit)

    def _remove_unit(self, unit: Unit) -> None:
        # If we simply used .remove() or .pop() in the units list, we just remove the first
        # occurrence of an unit from the list and not the specific unit
        index_to_remove = None

        for idx, u in enumerate(self.__units):
            if u is unit:
                index_to_remove = idx
                break

        if index_to_remove:
            self.__units.pop(index_to_remove)

    def _remove_units(self) -> None:
        self.__units.clear()

    def _get_units(self) -> list[Unit | None]:
        return self.__units
