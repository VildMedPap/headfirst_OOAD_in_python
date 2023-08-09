# Head First OOA&D - pythonic style 🐍

## Note

Python doesn't have clear distinctions like public, protected, and private members as in some other languages like Java. So, I've adopted these naming conventions:

- For general use: `self.public_member`
- For limited use: `self._protected_member`
- For internal use: `self.__private_member`

All tests in this book are executed using `pytest` and are located in the `tests` directory. I've translated the text-heavy Java tests from the book into clearer `pytest` assertions.

While converting Java code to Python, there were times when a direct match wasn't feasible or when Python offered a more straightforward method. My main aim was to preserve the educational intent of the book, rather than optimising for Python.

I've organized the code in each chapter into sections called "takes" for easier understanding.
