import threading


class DogDoor:
    def __init__(self) -> None:
        self.__open = False

    def open(self) -> None:
        print("The dog door opens.")
        self.__open = True

        timer = threading.Timer(5, self.close)
        timer.start()

    def close(self) -> None:
        print("The dog door closes.")
        self.__open = False

    def is_open(self) -> bool:
        return self.__open
