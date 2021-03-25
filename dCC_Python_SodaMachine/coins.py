class Coin:
    def __init__(self, name, value):
        self.value = value
        self.name = name


class Dime(Coin):
    def __init__(self):
        super(Dime, self).__init__("dime", 0.10)


class Nickel(Coin):
    def __init__(self):
        super(Nickel, self).__init__("nickel", 0.05)


class Penny(Coin):
    def __init__(self):
        super(Penny, self).__init__("penny", 0.01)


class Quarter(Coin):
    def __init__(self):
        super(Quarter, self).__init__("quarter", 0.25)
