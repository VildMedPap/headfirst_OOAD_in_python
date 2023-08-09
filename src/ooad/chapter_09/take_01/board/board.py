from ooad.chapter_09.take_01.board.tile import Tile
from ooad.chapter_09.take_01.units.unit import Unit


class Board:
    __tiles: list[list[Tile]]

    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__initialize()

    def __initialize(self) -> None:
        self._tiles: list[Tile | None] = []
        for i in range(self.__width):
            self.__tiles.append([])
            for _ in range(self.__height):
                self.__tiles[i].append(Tile())

    def get_tile(self, x: int, y: int) -> Tile:
        # Because real people don't start counting from 0
        return self.__tiles[x - 1][y - 1]

    def add_unit(self, unit: Unit, x: int, y: int) -> None:
        tile = self.get_tile(x, y)
        tile._add_unit(unit)

    def remove_unit(self, unit: Unit, x: int, y: int) -> None:
        tile = self.get_tile(x, y)
        tile._remove_unit(unit)

    def get_units(self, x: int, y: int) -> list[Unit | None]:
        tile = self.get_tile(x, y)
        return tile._get_units()

    def remove_units(self, x: int, y: int) -> None:
        tile = self.get_tile(x, y)
        tile._remove_units()
