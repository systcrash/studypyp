import random
from functions import sort_list_2, sort_2_massive_main, sort_3_massive_main, sort_3_massive_main, sort_list_1

def main0():
    while True:
            quest2 = input("Выберите тип генерируемого массива: 1. Обычный 2. Двумерный")
            if quest2 == "1":
                main1()
            elif quest2 == "2":
                main2()
def main2():
    msv2range = int(input("Введите кол-во цифр в массиве: "))
    msv3range = int(input("Введите кол-во столбцов в массиве: "))
    matrix = [[random.randint(1, 150) for _ in range(msv3range)] for _ in range(msv2range)]
    for row in matrix:
            print("Ваш массив:", row)
    while True:
        msv_quest_2 = input("Отсортировать массив? [y/n] ")
        if msv_quest_2 == "y":
            while True:
                vod_2 = input("Способ сортировки? 1. По возврастанию 2. По убыванию")
                if vod_2 == "1":
                    sort_2_massive_main(matrix)
                elif vod_2 == "2":
                    sort_3_massive_main(matrix)
                    while True:
                        vod_3 = input("Хотите создать другой массив? [y/n] ")
                        if vod_3 == "y":
                            main0()
                        elif vod_3 =="n":
                            exit()
        elif msv_quest_2 == "n":
            exit()
def main1():
    mas2 = int(input("Введите кол-во цифр в массиве: "))

    msv1 = [random.randint(1,150) for _ in range(mas2)]

    print("Ваш массив:", msv1)
    while True:
        msvquest1 = input("Отсортировать массив? [y/n] ")
        if msvquest1 == "y":
            while True:
                vod = input("Способ сортировки? 1. По возврастанию 2. По убыванию")
                if vod == "1":
                    sort_list_1(msv1)
                elif vod == "2":
                    sort_list_2(msv1)
                    while True:
                        vod_4 = input("Хотите создать другой массив? [y/n] ")
                        if vod_4 == "y":
                            main0()
                        elif vod_4 == "n":
                            exit()
        elif msvquest1 == "n":
            exit()
if __name__ == "__main__":
    main0()