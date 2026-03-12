class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        if capacity < 0:
            raise ValueError
        self._size = 0

    def __str__(self):
        cookies = "🍪"*self._size
        return cookies

    def deposit(self, n):
        if n>self._capacity-self._size:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if n>self._size:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

#jar = Jar()
#jar.deposit(7)
#jar.withdraw(6)
#print(jar)
