class ContiguousType:
    def __init__(self, name: str, length: int):
        self.name = name
        self.length = int(length)


class String(ContiguousType):

    def __init__(self, name: str, length: int):
        super().__init__(name, length)


class Number(ContiguousType):
    """
    The number class inherits a great deal from COBOL. We use the same
    terminology as COBOL's data divisions to define numbers, and they are
    intended to behave in the same way. For more information on the syntax for
    initialising a number, please see the documentation in the README.md, in
    addition to the tests and examples below.

    >>> balance = Number("balance", "S9(4)")
    >>> balance.set(-41)
    >>> output = balance.get()
    >>> "-0041"
    """

    def __init__(self, name: str, format: str):
        self.name = name
        self.length = len(format)
        self.format = format