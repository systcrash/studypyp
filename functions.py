

if __name__ == "__main__":
    main = print("Этот файл отвечает за сортировку массивов, он не может быть выполнен самостоятельно!")

def sort_list_1(msv1):
    msv1.sort()
    print(msv1)
def sort_list_2(msv1):
    msv1.sort(reverse=True)
    print(msv1)
def sort_2_massive_main(matrix):
    for row in matrix:
        row.sort()
    for row in matrix:
        print(row)
def sort_3_massive_main(matrix):
    for row in matrix:
        row.sort(reverse=True)
    for row in matrix:
        print(row)