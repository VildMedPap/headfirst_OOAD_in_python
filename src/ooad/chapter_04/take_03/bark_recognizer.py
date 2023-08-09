from ooad.chapter_04.take_03.bark import Bark
from ooad.chapter_04.take_03.dog_door import DogDoor


class BarkRecognizer:
    def __init__(self, door: DogDoor) -> None:
        self.__door = door

    def recognize(self, bark: Bark) -> None:
        print(f"BarkRecognizer: Heard a '{bark}'")
        allowed_barks = self.__door.get_allowed_barks()
        for allowed_bark in allowed_barks:
            if allowed_bark.equals(bark):
                self.__door.open()
                return
            else:
                print("This dog is not allowed.")
