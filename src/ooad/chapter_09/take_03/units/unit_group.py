from ooad.chapter_09.take_03.units.unit import Unit


class UnitGroup:
    __units: dict[int, Unit]

    def __init__(self, unit_list: list[Unit]) -> None:
        self.__units = {}
        for unit in unit_list:
            self.__units[unit.get_id()] = unit

    def add_unit(self, unit: Unit) -> None:
        self.__units[unit.get_id()] = unit

    def remove_unit(self, unit_or_id: Unit | int) -> None:
        if isinstance(unit_or_id, Unit):
            unit = unit_or_id
            id = unit.get_id()

        if isinstance(unit_or_id, int):
            id = unit_or_id

        _ = self.__units.pop(id, None)

    def get_unit(self, id: int) -> Unit | None:
        return self.__units.get(id, None)

    def get_units(self) -> list[Unit]:
        return list(self.__units.values())
