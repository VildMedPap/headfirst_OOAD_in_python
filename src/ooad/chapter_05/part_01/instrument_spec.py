from abc import ABC

from ooad.chapter_05.part_01.enums import Builder, Type, Wood


class InstrumentSpec(ABC):
    def __init__(
        self,
        builder: Builder,
        model: str,
        type: Type,
        back_wood: Wood,
        top_wood: Wood,
    ) -> None:
        super().__init__()
        self.__builder = builder
        self.__model = model
        self.__type = type
        self.__back_wood = back_wood
        self.__top_wood = top_wood

    def get_builder(self) -> Builder:
        return self.__builder

    def get_model(self) -> str:
        return self.__model

    def get_type(self) -> Type:
        return self.__type

    def get_back_wood(self) -> Wood:
        return self.__back_wood

    def get_top_wood(self) -> Wood:
        return self.__top_wood

    def matches(self, other_spec: "InstrumentSpec") -> bool:
        if self.get_builder() != other_spec.get_builder():
            return False

        if self.get_model() and self.get_model().lower() != other_spec.get_model().lower():
            return False

        if self.get_type() != other_spec.get_type():
            return False

        if self.get_back_wood() != other_spec.get_back_wood():
            return False

        if self.get_top_wood() != other_spec.get_top_wood():
            return False

        return True
