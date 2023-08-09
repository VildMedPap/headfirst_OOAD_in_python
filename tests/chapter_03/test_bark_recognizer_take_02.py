import time

import pytest
from ooad.chapter_03.take_02.bark_recognizer import BarkRecognizer
from ooad.chapter_03.take_02.dog_door import DogDoor


class TestDogDoor:
    @pytest.mark.slow
    def test_dog_door_bark_recognizer(self):
        # Given
        # Initialised DogDoor, and BarkRecognizer objects
        door = DogDoor()
        recognizer = BarkRecognizer(door)

        # When
        # Invoking the BarkRecognizer.recognize method

        # Then
        # The DogDoor should open and close as expected
        print("Fido barks to go outside...")
        recognizer.recognize("Woof")
        assert door.is_open()
        print("Fido has gone outside...")

        print("Fido's all done...")
        time.sleep(10)
        assert not door.is_open()
        print("...but he's stuck outside!")

        print("Fido starts barking...")
        recognizer.recognize("Woof")
        assert door.is_open()
        print("Fido's back inside...")
