class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Can not divide by zero!"
        return x / y


c = Calculator()

print(c.add(1, 2))
print(c.subtract(1, 2))
print(c.multiply(1, 2))
print(c.divide(1, 2))

print(c.divide(1, 0))
