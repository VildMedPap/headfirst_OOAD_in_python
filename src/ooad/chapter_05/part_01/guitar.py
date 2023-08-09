from ooad.chapter_05.part_01.guitar_spec import GuitarSpec
from ooad.chapter_05.part_01.instrument import Instrument


class Guitar(Instrument):
    def __init__(self, serial_number: str, price: float, spec: GuitarSpec) -> None:
        super().__init__(serial_number, price, spec)
