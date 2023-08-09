# Head First OOA&D - pythonic style 🐍

## Note

Python doesn't have clear distinctions like public, protected, and private members as in some other languages like Java. So, I've adopted these naming conventions:

- For general use: `self.public_member`
- For limited use: `self._protected_member`
- For internal use: `self.__private_member`

All tests in this book are executed using `pytest` and are located in the `tests` directory. I've translated the text-heavy Java tests from the book into clearer `pytest` assertions.

While converting Java code to Python, there were times when a direct match wasn't feasible or when Python offered a more straightforward method. My main aim was to preserve the educational intent of the book, rather than optimising for Python.

I've organized the code in each chapter into sections called "takes" for easier understanding.

## Chapter 1 - Great Software Begins Here: _well-designed apps rock_

- [Take 1](./src/ooad/chapter_01/take_01/): Quick and dirty
- [Take 2](./src/ooad/chapter_01/take_02/): Adding enums
- [Take 3](./src/ooad/chapter_01/take_03/): Making `Inventory.search_guitar` return a list
- [Take 4](./src/ooad/chapter_01/take_04/): Encapsulating what varies, introducing `GuitarSpec`
- [Take 5](./src/ooad/chapter_01/take_05/): Delegating `Inventory.search_guitar` to `GuitarSpec.matches`

## Chapter 2 - Give Them What They Want: _gathering requirements_

- [Take 1](./src/ooad/chapter_02/take_01/): Quick and dirty
- [Take 2](./src/ooad/chapter_02/take_02/): Setting up an automatic closure for the `DogDoor`

## Chapter 3 - I Love You, You’re Perfect... Now Change: _requirements change_

- [Take 1](./src/ooad/chapter_03/take_01/): Add a `BarkRecognizer` to open `DogDoor`
- [Take 2](./src/ooad/chapter_03/take_02/): Change design decision; move timer from `Remote` to `DogDoor`
