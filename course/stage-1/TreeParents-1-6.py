# lst_mro = [
#     'G : F',
#     'A',
#     'B : A',
#     'C : A',
#     'D : B C',
#     'E : D',
#     'F : D',
#     'X',
#     'Y : X A',
#     'Z : X',
#     'V : Z Y',
#     'W : V',
# ]
#
# lst_q = [  # список введённых запросов
#     'A G',  # Yes   # A предок G через B/C, D, F
#     'A Z',  # No    # Y потомок A, но не Y
#     'A W',  # Yes   # A предок W через Y, V
#     'X W',  # Yes   # X предок W через Y, V
#     'X QWE',  # No    # нет такого класса QWE
#     'A X',  # No    # классы есть, но они нет родства :)
#     'X X',  # Yes   # родитель он же потомок
#     '1 1',  # No    # несуществующий класс
# ]

lst_mro = []
lst_q = []
main_map = {}


iter = input()
for i in range(0, int(iter)):
    lst_mro.append(input())

iter = input()
for i in range(0, int(iter)):
    lst_q.append(input())


def search_all_predoks(potomok):
    result = []
    for key, value in main_map.items():
        if potomok in value:
            result.append(key)
            result.extend(search_all_predoks(key))
    return result


def add_potomok(predok, potomok):
    main_map[predok].append(potomok)
    predki = set(search_all_predoks(potomok))
    for pr in predki:
        if pr not in main_map:
            main_map[pr] = []
        if potomok not in main_map[pr]:
            main_map[pr].append(potomok)


def iteration():
    for line in lst_mro:
        if line.__contains__(':'):
            # 'A : B C'
            split = line.split(':')
            potomok = split[0].strip()  # A
            predki = split[1].strip()  # B C

            # создать для potomok место
            if potomok not in main_map:
                main_map[potomok] = []

            # для предков добавить потомка в пулл
            # если предков несколько
            if predki.__contains__(' '):
                predki_split = predki.split(' ')
                for predok in predki_split:
                    if predok not in main_map:
                        main_map[predok] = []
                    add_potomok(predok, potomok)
            else:
                # если предок один
                if predki not in main_map:
                    main_map[predki] = []
                add_potomok(predki, potomok)

        else:
            # 'A'
            if line not in main_map:
                main_map[line] = []

iteration()
iteration()

# print(main_map)
# for key, value in main_map.items():
#     print(key, value)

for s in lst_q:
    split = s.strip().split(' ')
    key = split[0]
    value = split[1]
    if key not in main_map:
        print('No')
        continue

    if key == value:
        print('Yes')
        continue

    if value in main_map[key]:
        print('Yes')
    else:
        print('No')
