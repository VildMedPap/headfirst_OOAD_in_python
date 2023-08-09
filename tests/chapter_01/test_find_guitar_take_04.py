from ooad.chapter_01.take_04.enums import Builder, Type, Wood
from ooad.chapter_01.take_04.guitar_spec import GuitarSpec
from ooad.chapter_01.take_04.inventory import Inventory


class TestSearchGuitar:
    def test_search_guitar(self):
        # Given
        # An initialised Inventory object with some inventory
        inventory = Inventory()
        inventory.add_guitar(
            "V95693",
            1499.95,
            Builder.FENDER,
            "Stratocastor",
            Type.ELECTRIC,
            Wood.ALDER,
            Wood.ALDER,
        )
        inventory.add_guitar(
            "V9512",
            1549.95,
            Builder.FENDER,
            "Stratocastor",
            Type.ELECTRIC,
            Wood.ALDER,
            Wood.ALDER,
        )
        inventory.add_guitar(
            "V9999",
            9999.99,
            Builder.GIBSON,
            "ArtVandelay",
            Type.ACOUSTIC,
            Wood.BRAZILIAN_ROSEWOOD,
            Wood.CEDAR,
        )

        # When
        # Invoking the search_guitar method
        what_erin_likes = GuitarSpec(
            Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER
        )
        guitar = inventory.search_guitar(what_erin_likes)

        # Then
        # It should not be an empty list
        assert len(guitar) == 2, "Sorry, Erin, we have nothing for you."
