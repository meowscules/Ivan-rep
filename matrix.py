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
                self.matrix[i][j] = random.randint(0, 1000)

    def __add__(self, other):
        matrixSum = Matrix(len(self.matrix), len(self.matrix[0]))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrixSum.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return matrixSum.matrix

    def __eq__(self, other):
       return (len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]))

    def printMatrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()
        print()