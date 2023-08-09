from ooad.chapter_05.part_01.enums import Builder, Type, Wood
from ooad.chapter_05.part_01.instrument_spec import InstrumentSpec


class GuitarSpec(InstrumentSpec):
    def __init__(
        self,
        builder: Builder,
        model: str,
        type: Type,
        num_strings: int,
        back_wood: Wood,
        top_wood: Wood,
    ) -> None:
        super().__init__(builder, model, type, back_wood, top_wood)
        self.__num_strings = num_strings

    def get_num_strings(self) -> int:
        return self.__num_strings

    def matches(self, other_spec: InstrumentSpec) -> bool:
        if not super().matches(other_spec):
            return False
        if not isinstance(other_spec, GuitarSpec):
            return False
        if self.get_num_strings() != other_spec.get_num_strings():
            return False

        return True
