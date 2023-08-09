import threading

from ooad.chapter_04.take_02.bark import Bark


class DogDoor:
    __allowed_bark: Bark

    def __init__(self) -> None:
        self.__open = False

    def set_allowed_bark(self, bark: Bark) -> None:
        self.__allowed_bark = bark

    def get_allowed_bark(self) -> Bark:
        return self.__allowed_bark

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
