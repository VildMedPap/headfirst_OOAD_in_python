import threading

from ooad.chapter_03.take_01.dog_door import DogDoor


class Remote:
    def __init__(self, door: DogDoor) -> None:
        self.__door = door

    def press_button(self) -> None:
        print("Pressing the remote control button...")
        if self.__door.is_open():
            self.__door.close()
        else:
            self.__door.open()

            timer = threading.Timer(5, self.__door.close)
            timer.start()
