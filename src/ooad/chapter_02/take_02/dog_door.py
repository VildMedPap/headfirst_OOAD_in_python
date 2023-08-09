class DogDoor:
    def __init__(self) -> None:
        self.__open = False

    def open(self) -> None:
        print("The dog door opens.")
        self.__open = True

    def close(self) -> None:
        print("The dog door closes.")
        self.__open = False

    def is_open(self) -> bool:
        return self.__open
