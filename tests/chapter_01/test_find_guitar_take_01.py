import pytest
from ooad.chapter_01.take_01.guitar import Guitar
from ooad.chapter_01.take_01.inventory import Inventory


class TestSearchGuitar:
    @pytest.mark.xfail
    def test_search_guitar(self):
        # Given
        # An initialised Inventory object with some inventory
        inventory = Inventory()
        inventory.add_guitar(
            "V95693", 1499.95, "Fender", "Stratocastor", "electric", "Alder", "Alder"
        )

        # When
        # Invoking the search_guitar method
        what_erin_likes = Guitar("", 0, "fender", "Stratocastor", "electric", "Alder", "Alder")
        guitar = inventory.search_guitar(what_erin_likes)

        # Then
        # It should not be none
        assert guitar is not None, "Sorry, Erin, we have nothing for you."
