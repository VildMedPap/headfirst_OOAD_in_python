from ooad.chapter_05.part_02.enums import Builder, InstrumentType, Type, Wood
from ooad.chapter_05.part_02.instrument_spec import InstrumentSpec
from ooad.chapter_05.part_02.inventory import Inventory


class TestSearchGuitar:
    def test_search_instrument(self):
        # Given
        # An initialised Inventory object with some instruments (3 guitars, 1 mandolin)
        inventory = self.get_ricks_inventory()

        # When
        # Invoking the search method
        client_request = InstrumentSpec({"builder": Builder.GIBSON, "back_wood": Wood.MAPLE})
        instruments = inventory.search(client_request)

        # Then
        # It should not be an empty list
        assert instruments is not None, "Sorry, we have nothing for you."
        assert len(instruments) == 3

    def get_ricks_inventory(self) -> Inventory:
        inventory = Inventory()

        # Add instrument 11277
        specs = {}
        specs["intrument_type"] = InstrumentType.GUITAR
        specs["builder"] = Builder.COLLINGS
        specs["model"] = "CJ"
        specs["type"] = Type.ACOUSTIC
        specs["num_strings"] = 6
        specs["back_wood"] = Wood.INDIAN_ROSEWOOD
        specs["top_wood"] = Wood.SITKA

        arguments = {}
        arguments["serial_number"] = "11277"
        arguments["price"] = 3999.95
        arguments["spec"] = InstrumentSpec(specs)

        inventory.add_instrument(**arguments)

        # Add instrument 122784
        specs = {}
        specs["instrument_type"] = InstrumentType.GUITAR
        specs["builder"] = Builder.MARTIN
        specs["model"] = "D-18"
        specs["type"] = Type.ACOUSTIC
        specs["num_strings"] = 6
        specs["back_wood"] = Wood.MAHOGANY
        specs["top_wood"] = Wood.ADIRONDACK

        arguments = {}
        arguments["serial_number"] = "122784"
        arguments["price"] = 5495.95
        arguments["spec"] = InstrumentSpec(specs)

        inventory.add_instrument(**arguments)

        # Add instrument V95693
        specs = {}
        specs["instrument_type"] = InstrumentType.GUITAR
        specs["builder"] = Builder.FENDER
        specs["model"] = "Stratocaster"
        specs["type"] = Type.ELECTRIC
        specs["num_strings"] = 6
        specs["back_wood"] = Wood.ALDER
        specs["top_wood"] = Wood.ALDER

        arguments = {}
        arguments["serial_number"] = "V95693"
        arguments["price"] = 1499.95
        arguments["spec"] = InstrumentSpec(specs)

        inventory.add_instrument(**arguments)

        # Add instrument V9512
        specs = {}
        specs["instrument_type"] = InstrumentType.GUITAR
        specs["builder"] = Builder.FENDER
        specs["model"] = "Stratocaster"
        specs["type"] = Type.ELECTRIC
        specs["num_strings"] = 6
        specs["back_wood"] = Wood.ALDER
        specs["top_wood"] = Wood.ALDER

        arguments = {}
        arguments["serial_number"] = "V9512"
        arguments["price"] = 1549.95
        arguments["spec"] = InstrumentSpec(specs)

        inventory.add_instrument(**arguments)

        # Add instrument 82765501
        specs = {}
        specs["instrument_type"] = InstrumentType.GUITAR
        specs["builder"] = Builder.GIBSON
        specs["model"] = "SG '61 Reissue"
        specs["type"] = Type.ELECTRIC
        specs["num_strings"] = 6
        specs["back_wood"] = Wood.MAHOGANY
        specs["top_wood"] = Wood.MAHOGANY

        arguments = {}
        arguments["serial_number"] = "82765501"
        arguments["price"] = 1890.95
        arguments["spec"] = InstrumentSpec(specs)

        inventory.add_instrument(**arguments)

        # Add instrument 70108276
        specs = {}
        specs["instrument_type"] = InstrumentType.GUITAR
        specs["builder"] = Builder.GIBSON
        specs["model"] = "Les Paul"
        specs["type"] = Type.ELECTRIC
        specs["num_strings"] = 6
        specs["back_wood"] = Wood.MAPLE
        specs["top_wood"] = Wood.MAPLE

        arguments = {}
        arguments["serial_number"] = "70108276"
        arguments["price"] = 2295.95
        arguments["spec"] = InstrumentSpec(specs)

        inventory.add_instrument(**arguments)

        # Add instrument 9019920
        specs = {}
        specs["instrument_type"] = InstrumentType.MANDOLIN
        specs["builder"] = Builder.GIBSON
        specs["model"] = "F5-G"
        specs["type"] = Type.ACOUSTIC
        specs["back_wood"] = Wood.MAPLE
        specs["top_wood"] = Wood.MAPLE

        arguments = {}
        arguments["serial_number"] = "9019920"
        arguments["price"] = 5495.99
        arguments["spec"] = InstrumentSpec(specs)

        inventory.add_instrument(**arguments)

        # Add instrument 8900231
        specs = {}
        specs["instrument_type"] = InstrumentType.BANJO
        specs["builder"] = Builder.GIBSON
        specs["model"] = "RB-3"
        specs["num_strings"] = 5
        specs["type"] = Type.ACOUSTIC
        specs["back_wood"] = Wood.MAPLE

        arguments = {}
        arguments["serial_number"] = "8900231"
        arguments["price"] = 2945.95
        arguments["spec"] = InstrumentSpec(specs)

        inventory.add_instrument(**arguments)

        return inventory
