import time

import pytest
from ooad.chapter_02.take_02.dog_door import DogDoor
from ooad.chapter_02.take_02.remote import Remote


class TestDogDoor:
    @pytest.mark.slow
    def test_dog_door_happy_path(self):
        # Given
        # Initialised DogDoor and Remote objects
        door = DogDoor()
        remote = Remote(door)

        # When
        # Invoking the Remote.press_button method

        # Then
        # The DogDoor should open and close as expected
        print("Fido barks to go outside...")
        remote.press_button()
        time.sleep(1)
        assert door.is_open()

        print("Fido has gone outside...")
        time.sleep(1)
        assert door.is_open()

        print("Fido's all done...")
        time.sleep(1)
        assert door.is_open()

        print("Fido's back inside...")
        time.sleep(3)
        assert not door.is_open()

    @pytest.mark.slow
    def test_dog_door_alternative_path(self):
        # Given
        # Initialised DogDoor and Remote objects
        door = DogDoor()
        remote = Remote(door)

        # When
        # Invoking the Remote.press_button method

        # Then
        # The DogDoor should open and close as expected
        print("Fido barks to go outside...")
        remote.press_button()
        assert door.is_open()

        print("Fido has gone outside...")
        print("Fido's all done...")
        time.sleep(10)
        assert not door.is_open()

        print("...but he's stuck outside!")
        print("Fido starts barking...")
        print("...so Gina grabs the remote control.")
        remote.press_button()
        assert door.is_open()
        print("Fido's back inside...")
