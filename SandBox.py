def simple_gen():
    yield 1
    yield 2
    yield 3

nxt = next(simple_gen())
nxt2 = next(simple_gen())

g = simple_gen()
nxt_g = next(g)

print(f'{nxt_g} {nxt_g}')
print(f'{nxt_g} {nxt_g}')

##print(f'{next(g)}')
