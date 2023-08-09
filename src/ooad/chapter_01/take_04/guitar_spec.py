from ooad.chapter_01.take_04.enums import Builder, Type, Wood


class GuitarSpec:
    def __init__(
        self,
        builder: Builder,
        model: str,
        type: Type,
        back_wood: Wood,
        top_wood: Wood,
    ) -> None:
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
