'''
1️⃣ Генератор sub_generator()
Он должен выдавать:
"A"
"B"
"C"
2️⃣ Генератор main_generator()
Он должен:
Сначала выдавать строку "Start"
Затем выдавать ВСЕ значения из sub_generator
Затем выдавать "End"
⚠️ ВАЖНО
В main_generator() обязательно используй:
yield from
💡 Ожидаемый вывод:
Start
A
B
C
End
'''

def sub_generator():
    for l in ['A', 'B', 'C']:
        yield l

def main_generator():
    yield 'start'
    yield from sub_generator()
    yield  'end'

def generator_print(gen_obj):
    for r in gen_obj:
        print(r)

def main_func_for_gen():
    generator_print(main_generator())


if __name__ == '__main__':
    main_func_for_gen()
    pass