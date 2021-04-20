import abc

# The interface segregation principle
# Many client-specific interfaces is better then one general-purpose interface.


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


# The interface defined above has many functionalities
# therefore it fits nicely with a modern MultiFunctionPrinter:
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


# But what about a very old kind of printer?
class OldFashionedPrinter(Machine):
    def print(self, document):
        # This would be ok.
        pass

    def fax(self, document):
        # This is not supported by the old printer.
        pass

    def scan(self, document):
        # This is also not supported by the old print.
        pass


# Why is this bad?
# -> Now the `OldFashionedPrinter` does have the methods `fax` and `scan` in
# its interface although it does not do anything. This might confuse users.
# Another option would be to raise `NotImplementedErrors`:
class EvenOlderFashionedPrinter(Machine):
    def print(self, document):
        # This would be ok.
        pass

    def fax(self, document):
        # This is not supported by the old printer.
        raise NotImplementedError

    def scan(self, document):
        # This is also not supported by the old print.
        raise NotImplementedError


# For application with users this might work.
# But for a web-server for example, it might happen that these
# methods are provided and then the service would be crashed.
# Of course, we could send back error codes, but fundemantally,
# the problem remains that the interace has methods that are
# not supported.

# Better option:
# Create one interface for printer, fax and scanner:


class Printer:
    @abc.abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abc.abstractmethod
    def scan(self):
        pass


class Fax:
    @abc.abstractmethod
    def fax(self, document):
        pass


# Now we can simply pick the interfaces that fit our
#  object. Let's take our old fashioned printer, now it
# would simply be


class SimplePrinter(Printer):
    def print(self, document):
        print(document)


# But also a more new-fashioned print with a scanner and fax would be support
class ComplexPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(document)

    def fax(self, document):
        pass

    def scan(self):
        pass


# We could even combine multiple interface into one subclass like so:
class PrinterFaxDevice(Printer, Fax):
    @abc.abstractmethod
    def print(self, document):
        pass

    @abc.abstractmethod
    def fax(scan):
        pass


class PrinterFax(PrinterFaxDevice):
    def print(self, document):
        print(document)

    def fax(self):
        pass


# We could even have both a printer and scanner in the class:
class PrinterFax2(PrinterFaxDevice):
    def __init__(self, printer, fax):
        self.fax = fax
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def fax(self, document):
        self.fax.fax(document)
