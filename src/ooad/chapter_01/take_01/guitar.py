class Guitar:
    def __init__(
        self,
        serial_number: str,
        price: float,
        builder: str,
        model: str,
        type: str,
        back_wood: str,
        top_wood: str,
    ) -> None:
        self.__serial_number = serial_number
        self.__price = price
        self.__builder = builder
        self.__model = model
        self.__type = type
        self.__back_wood = back_wood
        self.__top_wood = top_wood

    def get_serial_number(self) -> str:
        return self.__serial_number

    def get_price(self) -> float:
        return self.__price

    def set_price(self, new_price: float) -> None:
        self.__price = new_price

    def get_builder(self) -> str:
        return self.__builder

    def get_model(self) -> str:
        return self.__model

    def get_type(self) -> str:
        return self.__type

    def get_back_wood(self) -> str:
        return self.__back_wood

    def get_top_wood(self) -> str:
        return self.__top_wood
