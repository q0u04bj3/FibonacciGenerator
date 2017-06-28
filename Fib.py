import sys

#目前項是前兩項的總和
def fib():
    a,b = 0,1
    while True:
        a, b = b, a + b
        yield b

for i in range(1,len(sys.argv)):
    print fib(int(sys.argv[i]))
