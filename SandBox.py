def accumulator():
    accum = 0
    while True:
        x = yield accum

        if x is not None:
            accum += x

        print(f'*****************')
        print(f'Received    -> {x}')
        print(f'Accumulator -> {accum}')
        print(f'*****************')



gen = accumulator()

print(next(gen))
print(gen.send(4))
print(gen.send(5))
print(gen.send(7))

print(next(gen))
print(next(gen))