import random





def writeMatrixFromClass(matrix):
    with open("matrix.txt", "w") as f:
        for i in range(len(matrix.body)):
            # f.writelines((input(f"Введите строку {i+1}:"))+'\n')
            f.writelines(str(matrix.body))


def writeMatrixFromKeyboard(matrix):
    pass






