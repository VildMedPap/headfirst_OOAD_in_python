from ooad.chapter_02.take_01.dog_door import DogDoor
from ooad.chapter_02.take_01.remote import Remote


class TestDogDoor:
    def test_dog_door(self):
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
        remote.press_button()
        assert not door.is_open()

        print("Fido's all done...")
        remote.press_button()
        assert door.is_open()

        print("Fido's back inside...")
        remote.press_button()
        assert not door.is_open()
