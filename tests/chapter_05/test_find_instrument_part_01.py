from ooad.chapter_05.part_01.enums import Builder, Style, Type, Wood
from ooad.chapter_05.part_01.guitar_spec import GuitarSpec
from ooad.chapter_05.part_01.inventory import Inventory
from ooad.chapter_05.part_01.mandolin_spec import MandolinSpec


class TestSearchGuitar:
    def test_search_instrument(self):
        # Given
        # An initialised Inventory object with some instruments (3 guitars, 1 mandolin)
        inventory = Inventory()
        inventory.add_instrument(
            "V95693",
            1499.95,
            GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, 6, Wood.ALDER, Wood.ALDER),
        )
        inventory.add_instrument(
            "V9512",
            1549.95,
            GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, 6, Wood.ALDER, Wood.ALDER),
        )
        inventory.add_instrument(
            "V9999",
            9999.99,
            GuitarSpec(
                Builder.GIBSON, "Art", Type.ACOUSTIC, 8, Wood.BRAZILIAN_ROSEWOOD, Wood.CEDAR
            ),
        )
        inventory.add_instrument(
            "V1111",
            1111.11,
            MandolinSpec(
                Builder.FENDER, "Vandelay", Type.ACOUSTIC, Style.A, Wood.ALDER, Wood.ALDER
            ),
        )

        # When
        # Invoking the search method
        what_erin_likes = GuitarSpec(
            Builder.FENDER, "Stratocastor", Type.ELECTRIC, 6, Wood.ALDER, Wood.ALDER
        )
        instruments = inventory.search(what_erin_likes)

        # Then
        # It should not be an empty list
        assert len(instruments) == 2, "Sorry, Erin, we have nothing for you."
