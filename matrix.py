import random

class Matrix: #m - строки n - столбцы
    def __init__(self, M, N):
        self.matrix = []
        self.m = M
        self.n = N
        for i in range(self.m):
            self.matrix.append([0] * self.n)
        for i in range(self.m):
            for j in range(self.n):
                self.matrix[i][j] = random.randint(0, 10)

    def __add__(self, other):
        if (len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])):
            matrixAdd = Matrix(len(self.matrix), len(self.matrix[0]))
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    matrixAdd.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return matrixAdd.matrix
        else:
            print("Для сложения матрицы должны быть одинакового размера")


    def __sub__(self, other):
        if (len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])):
            matrixSub = Matrix(len(self.matrix), len(self.matrix[0]))
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    matrixSub.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return matrixSub.matrix
        else:
            print("Для вычитания матрицы должны быть одинакового размера")

    def __eq__(self, other):
       return (len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]))

    def __mul__(self, other):
        tmp = []
        matrixMul = Matrix(len(self.matrix), len(other.matrix[0]))
        matrixMul.matrix = []
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                sums = 0
                for k in range(len(other.matrix)):
                    sums = sums + (self.matrix[i][k]*other.matrix[k][j])
                tmp.append(sums)
            matrixMul.matrix.append(tmp)
            tmp = []
        return matrixMul.matrix

    def printMatrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()
        print()

M1 = Matrix(3, 2)
M1.printMatrix()
M2 = Matrix(3, 2)
M2.printMatrix()
print(M1-M2)
