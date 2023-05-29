class Car:

    def __init__(self, **kw):
        self.model = kw.get("model")
        self.brand = kw.get("brand")

    def __str__(self):
        return f"{self.brand} - {self.model}"


def add_numbers(*args):
    return sum(args)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(add_numbers(2, 2, 2, 2, 2, 2))
print(calculate(5, add=5, multiply=10))

porch911 = Car(brand="Porch", model="911")
print(porch911)
