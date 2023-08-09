from ooad.chapter_09.take_01.units.unit import Unit
from ooad.chapter_09.take_01.units.weapon import Weapon


class TestUnit:
    def test_setting_getting_type_property(self):
        # Given
        # Existing Unit object
        unit = Unit(id=42)

        # When
        # Setting and getting the type property
        unit.set_type(new_type="infantry")
        actual = unit.get_type()

        # Then
        # It should be as expected
        expected = "infantry"
        assert actual == expected

    def test_setting_getting_unit_specific_property(self):
        # Given
        # Existing Unit object
        unit = Unit(id=42)

        # When
        # Setting and getting a unit specific property
        unit.set_property(property="hitPoints", value=25)
        actual = unit.get_property(property="hitPoints")

        # Then
        # It should be as expected
        expected = 25
        assert actual == expected

    def test_changing_an_existing_property_value(self):
        # Given
        # Existing Unit object, with unit specific property set
        unit = Unit(id=42)
        unit.set_property(property="hitPoints", value=25)

        # When
        # Changing the unit specific property and getting it again
        unit.set_property(property="hitPoints", value=15)
        actual = unit.get_property(property="hitPoints")

        # Then
        # It should be as expected
        expected = 15
        assert actual == expected

    def test_getting_a_non_existing_property(self):
        # Given
        # Existing Unit object
        unit = Unit(id=42)

        # When
        # Getting a non-existing property
        actual = unit.get_property(property="strengt")

        # Then
        # It should be as expected
        assert actual is None

    def test_getting_the_id_property(self):
        # Given
        # Existing Unit object
        unit = Unit(id=42)

        # When
        # Getting the id property
        actual = unit.get_id()

        # Then
        # It should be as expected
        expected = 42
        assert actual == expected

    def test_setting_getting_the_name_property(self):
        # Given
        # Existing Unit object
        unit = Unit(id=42)

        # When
        # Setting and getting the name property
        unit.set_name(new_name="Damon")
        actual = unit.get_name()

        # Then
        # It should be as expected
        expected = "Damon"
        assert actual == expected

    def test_adding_getting_a_weapon(self):
        # Given
        # Existing Unit object
        unit = Unit(id=42)

        # When
        # Setting and getting the name property
        weapon = Weapon()
        unit.add_weapon(weapon)
        actual = unit.get_weapons()

        # Then
        # It should be as expected
        expected = [weapon]
        assert actual == expected
