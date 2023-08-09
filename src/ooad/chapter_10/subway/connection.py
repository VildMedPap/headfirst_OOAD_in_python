from ooad.chapter_10.subway.station import Station


class Connection:
    __station1: Station
    __station2: Station
    __line_name: str

    def __init__(self, station1: Station, station2: Station, line_name: str) -> None:
        self.__station1 = station1
        self.__station2 = station2
        self.__line_name = line_name

    def get_station1(self) -> Station:
        return self.__station1

    def get_station2(self) -> Station:
        return self.__station2

    def get_line_name(self) -> str:
        return self.__line_name
