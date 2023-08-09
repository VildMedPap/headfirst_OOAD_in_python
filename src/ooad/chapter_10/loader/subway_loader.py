from pathlib import Path
from typing import TextIO

from ooad.chapter_10.subway.subway import Subway


class SubwayLoader:
    __subway: Subway

    def __init__(self) -> None:
        self.__subway = Subway()

    def load_from_file(self, subway_file_path: str) -> Subway:
        path = Path(subway_file_path)
        with path.open() as file:
            self.load_stations(file)
            line_name = file.readline().strip()

            while line_name:
                self.load_line(line_name, file)
                line_name = file.readline().strip()
        return self.__subway

    def load_stations(self, file: TextIO) -> None:
        current_line = file.readline().strip()

        while current_line:
            self.__subway.add_station(current_line)
            current_line = file.readline().strip()

    def load_line(self, line_name: str, file: TextIO) -> None:
        station1_name = file.readline().strip()
        station2_name = file.readline().strip()

        while station2_name:
            self.__subway.add_connection(station1_name, station2_name, line_name)
            station1_name = station2_name
            station2_name = file.readline().strip()
