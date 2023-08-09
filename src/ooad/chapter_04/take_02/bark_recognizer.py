from ooad.chapter_04.take_02.bark import Bark
from ooad.chapter_04.take_02.dog_door import DogDoor


class BarkRecognizer:
    def __init__(self, door: DogDoor) -> None:
        self.__door = door

    def recognize(self, bark: Bark) -> None:
        print(f"BarkRecognizer: Heard a '{bark}'")
        if self.__door.get_allowed_bark().equals(bark):
            self.__door.open()
        else:
            print("This dog is not allowed.")
