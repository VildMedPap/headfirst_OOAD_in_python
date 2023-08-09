from ooad.chapter_08.board.board import Board
from ooad.chapter_08.board.tile import Tile
from ooad.chapter_08.units.unit import Unit


class Board3D:
    __3dtiles: list[Board | None]

    def __init__(self, width: int, height: int, depth: int) -> None:
        self.__width = width
        self.__height = height
        self.__depth = depth
        self.__initialize()

    def __initialize(self) -> None:
        self.__3dtiles: list[Board | None] = []
        for _ in range(self.__depth):
            self.__3dtiles.append(Board(self.__width, self.__height))

    def get_tile(self, x: int, y: int, z: int) -> Tile:
        # Because real people don't start counting from 0
        board = self.__3dtiles[x - 1]
        if board:
            return board.get_tile(x, y)
        else:
            raise ValueError

    def add_unit(self, unit: Unit, x: int, y: int, z: int) -> None:
        tile = self.get_tile(x, y, z)
        tile._add_unit(unit)

    def remove_unit(self, unit: Unit, x: int, y: int, z: int) -> None:
        tile = self.get_tile(x, y, z)
        tile._remove_unit(unit)

    def get_units(self, x: int, y: int, z: int) -> list[Unit | None]:
        tile = self.get_tile(x, y, z)
        return tile._get_units()

    def remove_units(self, x: int, y: int, z: int) -> None:
        tile = self.get_tile(x, y, z)
        tile._remove_units()
