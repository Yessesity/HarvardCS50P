class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return ("🍪" * self.size)

    def deposit(self, n):
        self.size += n
        self.capacity -= n

    def withdraw(self, n):
        self.size -= n
        self.capacity += n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, n):
        if not n >= 0:
            raise ValueError
        self._capacity = n
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, n):
        if not n >= 0:
            raise ValueError
        self._size = n


def main():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    print(f"Cookies: {jar}\nCapacity: {jar.capacity}\nNo. of Cookies: {jar.size}")


if __name__ == "__main__":
    main()