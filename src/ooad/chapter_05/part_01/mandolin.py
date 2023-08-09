from ooad.chapter_05.part_01.instrument import Instrument
from ooad.chapter_05.part_01.mandolin_spec import MandolinSpec


class Mandolin(Instrument):
    def __init__(self, serial_number: str, price: float, spec: MandolinSpec) -> None:
        super().__init__(serial_number, price, spec)
