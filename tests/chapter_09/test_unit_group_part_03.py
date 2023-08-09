import pytest
from ooad.chapter_09.take_03.units.unit import Unit
from ooad.chapter_09.take_03.units.unit_group import UnitGroup


class TestUnitGroup:
    def test_getting_units_from_a_group(self):
        # Given
        # Existing list of Unit objects
        unit_list = [Unit(id=97), Unit(id=98), Unit(id=99)]

        # When
        # Initiating a new UnitGroup instance with the unit list and getting all
        # the units again
        unit_group = UnitGroup(unit_list)
        actual = unit_group.get_units()

        # Then
        # It should be as expected
        expected = unit_list
        assert actual == expected

    def test_adding_a_unit_to_a_group(self):
        # Given
        # Initialised UnitGroup instance without any Units
        unit_group = UnitGroup([])

        # When
        # Adding a Unit to the group
        new_unit = Unit(id=100)
        unit_group.add_unit(new_unit)

        # Then
        # It should be part of the group
        assert new_unit in unit_group.get_units()

    def test_getting_a_unit_from_the_group_by_the_id(self):
        # Given
        # Initialised UnitGroup instance without any Units
        expected = Unit(id=100)
        unit_list = [expected]
        unit_group = UnitGroup(unit_list)

        # When
        # Getting a unit by the id
        actual = unit_group.get_unit(id=100)

        # Then
        # It should be as expected
        assert actual == expected

    def test_getting_all_units_from_the_group(self):
        # Given
        # Initialised UnitGroup instance without any Units
        expected = [Unit(id=97), Unit(id=98), Unit(id=99)]
        unit_group = UnitGroup(expected)

        # When
        # Getting all units from the group
        actual = unit_group.get_units()

        # Then
        # It should be as expected
        assert actual == expected

    def test_removing_a_unit_from_the_group_by_id(self):
        # Given
        # Initialised UnitGroup instance without any Units
        unit_list = [Unit(id=97), Unit(id=98), Unit(id=99), Unit(id=100)]
        unit_group = UnitGroup(unit_list)

        # When
        # Removing a unit from the group
        unit_group.remove_unit(100)

        # Then
        # It shouldn't be in the list of units
        assert all(unit.get_id() != 100 for unit in unit_group.get_units())

    def test_removing_a_unit_from_the_group_by_unit(self):
        # Given
        # Initialised UnitGroup instance without any Units
        unit_100 = Unit(id=100)
        unit_list = [Unit(id=97), Unit(id=98), Unit(id=99), unit_100]
        unit_group = UnitGroup(unit_list)

        # When
        # Removing a unit from the group
        unit_group.remove_unit(unit_100)

        # Then
        # It shouldn't be in the list of units
        assert all(unit.get_id() != 100 for unit in unit_group.get_units())
