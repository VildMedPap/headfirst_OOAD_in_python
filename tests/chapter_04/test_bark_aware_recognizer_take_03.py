import time

import pytest
from ooad.chapter_04.take_03.bark import Bark
from ooad.chapter_04.take_03.bark_recognizer import BarkRecognizer
from ooad.chapter_04.take_03.dog_door import DogDoor
from ooad.chapter_04.take_03.remote import Remote


class TestDogDoor:
    @pytest.mark.slow
    def test_dog_door_bark_aware_recognizer(self):
        # Given
        # Initialised DogDoor, BarkRecognizer, and Remote objects
        door = DogDoor()
        door.set_allowed_bark(Bark("rowlf"))
        door.set_allowed_bark(Bark("rooowlf"))
        door.set_allowed_bark(Bark("rawlf"))
        door.set_allowed_bark(Bark("woof"))
        recognizer = BarkRecognizer(door)
        remote = Remote(door)

        # When
        # Invoking the BarkRecognizer.recognize method

        # Then
        # The DogDoor should open and close as expected
        print("Bruce starts barking.")
        recognizer.recognize(Bark("rowlf"))
        assert door.is_open()
        print("Bruce has gone outside...")

        print("Bruce's all done...")
        time.sleep(10)
        assert not door.is_open()
        print("...but he's stuck outside!")

        print("A small dog (not Bruce) starts barking.")
        recognizer.recognize(Bark("yip"))
        assert not door.is_open()

        print("Bruce starts barking.")
        recognizer.recognize(Bark("rooowlf"))
        assert door.is_open()
        print("Bruce's back inside...")
