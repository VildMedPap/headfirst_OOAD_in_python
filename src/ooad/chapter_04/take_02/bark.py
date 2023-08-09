class Bark:
    def __init__(self, sound: str) -> None:
        self.__sound = sound

    def get_sound(self) -> str:
        return self.__sound

    def equals(self, bark: "Bark") -> bool:
        if isinstance(bark, Bark):
            other_bark: Bark = bark
            if self.get_sound().lower() == other_bark.get_sound().lower():
                return True

        return False
