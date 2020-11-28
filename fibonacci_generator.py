def fibonacci():
    f0 = 0
    f1 = 1
    while True:
        yield f0
        f0, f1 = f1, f0 + f1


generator = fibonacci()
for i in range(5):
    print(next(generator))
