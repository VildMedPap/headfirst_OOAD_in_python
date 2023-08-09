from ooad.chapter_05.part_01.enums import Builder, Style, Type, Wood
from ooad.chapter_05.part_01.instrument_spec import InstrumentSpec


class MandolinSpec(InstrumentSpec):
    def __init__(
        self,
        builder: Builder,
        model: str,
        type: Type,
        style: Style,
        back_wood: Wood,
        top_wood: Wood,
    ) -> None:
        super().__init__(builder, model, type, back_wood, top_wood)
        self.__style = style

    def get_style(self) -> Style:
        return self.__style

    def matches(self, other_spec: InstrumentSpec) -> bool:
        if not super().matches(other_spec):
            return False
        if not isinstance(other_spec, MandolinSpec):
            return False
        if self.get_style() != other_spec.get_style():
            return False

        return True
