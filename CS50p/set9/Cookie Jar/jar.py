class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int):
            raise(ValueError("Invalid number."))
        if capacity < 0:
            raise(ValueError("Invalid number."))
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        output1 = "🍪" * self.cookies
        return(output1)

    def deposit(self, n):
        if not isinstance(n, int):
            raise(ValueError("Invalid number."))
        elif n < 0:
            raise(ValueError("Invalid number."))
        elif self.cookies+n > self._capacity:
            raise(ValueError("Invalid number."))
        self.cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0 or self.cookies - n < 0:
            raise ValueError("Invalid number.")
        elif n<0:
            raise ValueError("Invalid number.")
        elif (self.cookie) - n < 0:
            raise ValueError("Invalid number.")
        self.cookies -= n

    @property
    def capacity(self):
        output2 = self._capacity
        return(output2)

    @property
    def size(self):
        output3 = self.cookies
        return(output3)
