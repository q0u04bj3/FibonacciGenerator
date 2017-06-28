import sys

def fib():
    a,b = 0,1
    while True:
        a, b = b, a + b
        yield b

sys.argv[1] = fib()
print sys.argv[1].next()
print sys.argv[1].next()
print sys.argv[1].next()
print sys.argv[1].next()
print sys.argv[1].next()
