import random
def printMatrix(object):
    for i in range(len(object.matrix)):
        for j in range(len(object.matrix[i])):
            print(object.matrix[i][j], end=' ')
        print()
    print()



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
            if (len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])):
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i])):
                        self.matrix[i][j] += other.matrix[i][j]
            printMatrix(object1)
            else:
                print("Матрицы не равны")

    def matrixSum():
