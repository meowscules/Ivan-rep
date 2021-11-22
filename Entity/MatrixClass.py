import random
from Entity.MatrixException import *


def setMatrixRows():
    return int(input("Введите количество строк матрицы: "))


def setMatrixCols():
    return int(input("Введите количество столбцов матрицы: "))


class Matrix:
    def __init__(self, rows, cols):
        self.body = []
        self.rows = rows
        self.cols = cols
        for i in range(rows):
            self.body.append([0] * cols)
        for i in range(self.rows):
            for j in range(self.cols):
                self.body[i][j] = readMatrix

    def validationFunction(self, other):
        if self == other and isinstance(self, Matrix) and isinstance(other, Matrix):
            return True
        else:
            raise MatrixSizeError

    def __eq__(self, other):
        return len(self.body) == len(other.body) and len(self.body[0]) == len(other.body[0])

    def __add__(self, other):
        if self.validationFunction(other):
            matrixAdd = Matrix(len(self.body), len(self.body[0]))
            for i in range(len(self.body)):
                for j in range(len(self.body[i])):
                    matrixAdd.body[i][j] = self.body[i][j] + other.body[i][j]
            return matrixAdd.body
        else:
            pass

    def __sub__(self, other):
        if self.validationFunction(other):
            matrixSub = Matrix(len(self.body), len(self.body[0]))
            for i in range(len(self.body)):
                for j in range(len(self.body[i])):
                    matrixSub.body[i][j] = self.body[i][j] - other.body[i][j]
            return matrixSub.body
        else:
            pass

    def __mul__(self, other):
        try:
            if isinstance(other, int):
                matrixMul = Matrix(len(self.body), len(self.body[0]))
                for i in range(len(self.body)):
                    for j in range(len(self.body[0])):
                        matrixMul.body[i][j] = other * self.body[i][j]
                return matrixMul.body
            elif isinstance(other, Matrix):
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
        except MatrixError:
            raise MatrixError

    def transposeMatrix(self):
        try:
            tmp = [[0] * len(x) for x in self.body]
            for i in range(len(self.body)):
                for j in range(len(self.body[0])):
                    tmp[i][j] = self.body[j][i]
            return tmp
        except MatrixSizeError:
            raise MatrixSizeError

    def printMatrix(self):
        for i in range(len(self.body)):
            for j in range(len(self.body[i])):
                print(self.body[i][j], end=' ')
            print()
        print()
