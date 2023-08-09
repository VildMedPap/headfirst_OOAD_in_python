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

## Chapter 4 - Taking Your Software Into the Real World: _analysis_

- [Take 1](./src/ooad/chapter_04/take_01/): Ryan's quick and dirty solution
- [Take 2](./src/ooad/chapter_04/take_02/): Sam's objects and delegation obsessed solution
- [Take 3](./src/ooad/chapter_04/take_03/): Maria's textual analysis solution

## Chapter 5

### Part 1 - Nothing Ever Stays the Same: _good design_

- [Part 1](./src/ooad/chapter_05/part_01/): Rick's new application - ABC, inheritance, and aggregation

### Part 2 - Give Your Software a 30-minute Workout: _flexible software_

- [Part 2](./src/ooad/chapter_05/part_02/): Rick's new application - More cohesive software

## Chapter 6 - "My Name is Art Vandelay": _solving really big problems_

- [Chapter 6](./src/ooad/chapter_06/): The Big Break-Up and a quick and dirty `Unit` class
