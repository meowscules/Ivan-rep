import random

def setMatrixSize():
    row = int(input("Введите количество строк матрицы: "))
    col = int(input("Введите количество столбцов матрицы: "))
    return row, col

def writeMatrixFromClass(matrix):
    with open("matrix.txt", "w") as f:
        for i in range(len(matrix.body)):
            #f.writelines((input(f"Введите строку {i+1}:"))+'\n')
            f.writelines(str(matrix.body))

def writeMatrixFromKeyboard(matrix):
    pass

class Matrix: #m - строки n - столбцы
    def __init__(self, size):
        self.body = []
        self.m = size[0]
        self.n = size[1]
        for i in range(size[0]):
             self.body.append([0] * size[1])
        for i in range(self.m):
            for j in range(self.n):
                self.body[i][j] = random.randint(0, 10)

    def __add__(self, other):
        if (len(self.body) == len(other.body) and len(self.body[0]) == len(other.body[0])):
            matrixAdd = Matrix(len(self.body))
            for i in range(len(self.body)):
                for j in range(len(self.body[i])):
                    matrixAdd.body[i][j] = self.body[i][j] + other.body[i][j]
            return matrixAdd.body
        else:
            print("Для сложения матрицы должны быть одинакового размера")


    def __sub__(self, other):
        if self != other:
            print("Для вычитания матрицы должны быть одинакового размера")
        else:
            matrixSub = Matrix(len(self.body))
            for i in range(len(self.body)):
                for j in range(len(self.body[i])):
                    matrixSub.body[i][j] = self.body[i][j] - other.matrix[i][j]
            return matrixSub.body

    def __eq__(self, other):
       return (len(self.body) == len(other.body) and len(self.body[0]) == len(other.body[0]))

    def __mul__(self, other):
        if isinstance(other, int):
            matrixMul = Matrix(len(self.body))
            for i in range(len(self.body)):
                for j in range(len(self.body[0])):
                    matrixMul.body[i][j] = other * self.body[i][j]
            return matrixMul.body
        elif isinstance(other, object):
            tmp = []
            matrixMul = Matrix(len(self.body))
            matrixMul.matrix = []
            for i in range(len(self.body)):
                for j in range(len(other.body[0])):
                    sums = 0
                    for k in range(len(other.body)):
                        sums = sums + (self.body[i][k]*other.body[k][j])
                    tmp.append(sums)
                matrixMul.body.append(tmp)
                tmp = []
            return matrixMul.body

    def transposeMatrix(self):
        tmp = [[None] * len(x) for x in self.body]
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

M1 = Matrix(setMatrixSize())
print(M1.body)
M2 = Matrix(setMatrixSize())
print(M2.body)
print(M1-M2)

