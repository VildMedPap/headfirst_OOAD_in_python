import time

import pytest
from ooad.chapter_04.take_01.bark_recognizer import BarkRecognizer
from ooad.chapter_04.take_01.dog_door import DogDoor


class TestDogDoor:
    @pytest.mark.slow
    def test_dog_door_bark_aware_recognizer(self):
        # Given
        # Initialised DogDoor, and BarkRecognizer objects
        door = DogDoor()
        door.set_allowed_bark("Rawlf! Rawlf!")
        recognizer = BarkRecognizer(door)

        # When
        # Invoking the BarkRecognizer.recognize method

        # Then
        # The DogDoor should open and close as expected
        print("Bruce starts barking.")
        recognizer.recognize("Rawlf! Rawlf!")
        assert door.is_open()
        print("Bruce has gone outside...")

        print("Bruce's all done...")
        time.sleep(10)
        assert not door.is_open()
        print("...but he's stuck outside!")

        print("A small dog (not Bruce) starts barking.")
        recognizer.recognize("yip")
        assert not door.is_open()

        print("Bruce starts barking.")
        recognizer.recognize("Rawlf! Rawlf!")
        assert door.is_open()
        print("Bruce's back inside...")
