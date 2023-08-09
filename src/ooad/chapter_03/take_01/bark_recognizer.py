from ooad.chapter_03.take_01.dog_door import DogDoor


class BarkRecognizer:
    def __init__(self, door: DogDoor) -> None:
        self.__door = door

    def recognize(self, bark: str) -> None:
        print(f"BarkRecognizer: Heard a '{bark}'")
        self.__door.open()
