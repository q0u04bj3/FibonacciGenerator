def fib():
    a,b = 0,1
    while True:
        a, b = b, a + b
        yield b

#目前項是前兩項的總和
