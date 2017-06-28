def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b

c = fib()
print c.next()
print c.next()
print c.next()
print c.next()
print c.next()
