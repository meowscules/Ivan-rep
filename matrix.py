import random


def setMatrixRows():
    rows = int(input("Введите количество строк матрицы: "))
    return rows


def setMatrixCols():
    cols = int(input("Введите количество столбцов матрицы: "))
    return cols


def writeMatrixFromClass(matrix):
    with open("matrix.txt", "w") as f:
        for i in range(len(matrix.body)):
            # f.writelines((input(f"Введите строку {i+1}:"))+'\n')
            f.writelines(str(matrix.body))


def writeMatrixFromKeyboard(matrix):
    pass


class Matrix:  # m - строки n - столбцы
    def __init__(self, rows, cols):
        self.body = []
        self.m = rows
        self.n = cols
        for i in range(rows):
            self.body.append([0] * cols)
        for i in range(self.m):
            for j in range(self.n):
                self.body[i][j] = random.randint(0, 10)

    def __add__(self, other):
        if self != other:
            print("Для сложения матрицы должны быть одинакового размера")
        else:
            matrixAdd = Matrix(len(self.body), len(self.body[0]))
            for i in range(len(self.body)):
                for j in range(len(self.body[i])):
                    matrixAdd.body[i][j] = self.body[i][j] + other.body[i][j]
            return matrixAdd.body

    def __sub__(self, other):
        if self != other:
            print("Для вычитания матрицы должны быть одинакового размера")
        else:
            matrixSub = Matrix(len(self.body), len(self.body[0]))
            for i in range(len(self.body)):
                for j in range(len(self.body[i])):
                    matrixSub.body[i][j] = self.body[i][j] - other.body[i][j]
            return matrixSub.body

    def __eq__(self, other):
        return len(self.body) == len(other.body) and len(self.body[0]) == len(other.body[0])

    def __mul__(self, other):
        if isinstance(other, int):
            matrixMul = Matrix(len(self.body), len(self.body[0]))
            for i in range(len(self.body)):
                for j in range(len(self.body[0])):
                    matrixMul.body[i][j] = other * self.body[i][j]
            return matrixMul.body
        elif isinstance(other, Matrix.__class__):
            tmp = []
            matrixMul = Matrix(len(self.body), len(self.body[0]))
            matrixMul.body = []
            for i in range(len(self.body)):
                for j in range(len(other.body[0])):
                    sums = 0
                    for k in range(len(other.body)):
                        sums = sums + (self.body[i][k] * other.body[k][j])
                    tmp.append(sums)
                matrixMul.body.append(tmp)
                tmp = []
            return matrixMul.body

    def transposeMatrix(self):
        tmp = [[0] * len(x) for x in self.body]
        for i in range(len(self.body)):
            for j in range(len(self.body[0])):
                tmp[i][j] = self.body[j][i]
        return tmp

    def printMatrix(self):
        for i in range(len(self.body)):
            for j in range(len(self.body[i])):
                print(self.body[i][j], end=' ')
            print()
        print()


if __name__ == '__main__':
    M1 = Matrix(setMatrixRows(), setMatrixCols())
    M2 = Matrix(setMatrixRows(), setMatrixCols())
    #test1
    M1.printMatrix()
    M2.printMatrix()
    #test2
    print(M1.transposeMatrix())
    print(M2.transposeMatrix())
    #test3
    print(M1 * M2)
    #test4
    print(M1 + M2)
    #test5
    print(M1 - M2)
    #test6
    print(M1 * 3)

