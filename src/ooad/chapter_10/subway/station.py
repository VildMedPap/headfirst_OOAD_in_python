class Station:
    __name: str

    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Station):
            return self.get_name().lower() == other.get_name().lower()
        return False

    def __hash__(self) -> int:
        return hash(self.get_name().lower())
