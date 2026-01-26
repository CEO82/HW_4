'''from itertools import cycle, count, takewhile

def traffik_light():
    ligth_list = ['Red', 'Yellow', 'Green']
    return cycle(ligth_list)

rep = 6
for i in traffik_light():
    if rep > 0:
        rep -= 1
        print(i)
    else:
        break'''

from itertools import cycle, count, takewhile
def traffic_light():
    light_list = ['Red', 'Yellow', 'Green']
    # Склеиваем бесконечный цикл со счетчиком 1, 2, 3...
    combined = zip(count(1), cycle(light_list))

    # Говорим: "Бери, пока номер шага (x[0]) <= 6"
    return takewhile(lambda x: x[0] <= 6, combined)


for step, color in traffic_light():
    print(f"Шаг {step}: {color}")


