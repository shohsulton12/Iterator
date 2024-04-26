def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
for i, fib in enumerate(fibonacci()):
    if i >= 10:
        break
    print(fib)