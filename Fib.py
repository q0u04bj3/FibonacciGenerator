def fib():
    f1, f2 = 1, 2
    while True:
        f1, f2 = f2, f1 + f2
        yield f2

c = fib()
print c.next()
print c.next()
print c.next()
print c.next()
print c.next()
