from ooad.chapter_05.part_01.guitar import Guitar
from ooad.chapter_05.part_01.guitar_spec import GuitarSpec
from ooad.chapter_05.part_01.instrument import Instrument
from ooad.chapter_05.part_01.instrument_spec import InstrumentSpec
from ooad.chapter_05.part_01.mandolin import Mandolin
from ooad.chapter_05.part_01.mandolin_spec import MandolinSpec


class Inventory:
    def __init__(self) -> None:
        self.__inventory: list[Instrument] = []

    def add_instrument(
        self,
        serial_number: str,
        price: float,
        spec: InstrumentSpec,
    ) -> None:
        instrument: Instrument
        if isinstance(spec, GuitarSpec):
            instrument = Guitar(serial_number, price, spec)

        if isinstance(spec, MandolinSpec):
            instrument = Mandolin(serial_number, price, spec)

        self.__inventory.append(instrument)

    def get(self, serial_number: str) -> Instrument | None:
        for instrument in self.__inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument

        return None

    def search(self, search_spec: InstrumentSpec) -> list[Instrument]:
        matching_instruments: list[Instrument] = []

        for instrument in self.__inventory:
            if instrument.get_spec().matches(search_spec):
                matching_instruments.append(instrument)

        return matching_instruments
