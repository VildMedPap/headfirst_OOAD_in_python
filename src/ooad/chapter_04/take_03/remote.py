from ooad.chapter_04.take_03.dog_door import DogDoor


class Remote:
    def __init__(self, door: DogDoor) -> None:
        self.__door = door

    def press_button(self) -> None:
        print("Pressing the remote control button...")
        self.__door.close() if self.__door.is_open() else self.__door.open()
