from ooad.chapter_01.take_02.enums import Builder, Type, Wood
from ooad.chapter_01.take_02.guitar import Guitar
from ooad.chapter_01.take_02.inventory import Inventory


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

        # When
        # Invoking the search_guitar method
        what_erin_likes = Guitar(
            "", 0, Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER
        )
        guitar = inventory.search_guitar(what_erin_likes)

        # Then
        # It should not be none
        assert guitar is not None, "Sorry, Erin, we have nothing for you."
