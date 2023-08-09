from ooad.chapter_05.part_02.instrument import Instrument
from ooad.chapter_05.part_02.instrument_spec import InstrumentSpec


class Inventory:
    def __init__(self) -> None:
        self.__inventory: list[Instrument] = []

    def add_instrument(
        self,
        serial_number: str,
        price: float,
        spec: InstrumentSpec,
    ) -> None:
        instrument = Instrument(serial_number, price, spec)
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
