from ooad.chapter_04.take_01.dog_door import DogDoor


class BarkRecognizer:
    def __init__(self, door: DogDoor) -> None:
        self.__door = door

    def recognize(self, bark: str) -> None:
        print(f"BarkRecognizer: Heard a '{bark}'")
        if self.__door.get_allowed_bark().lower() == bark.lower():
            self.__door.open()
        else:
            print("This dog is not allowed.")
