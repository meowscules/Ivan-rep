import random

def setMatrixSize():
    row = int(input("Введите количество строк матрицы: "))
    col = int(input("Введите количество столбцов матрицы: "))
    return row, col

def writeAmatrixfromclass(object):
    with open("matrix.txt", "w") as f:
        for i in range(len(object.matrix)):
            #f.writelines((input(f"Введите строку {i+1}:"))+'\n')
            f.writelines(str(object.matrix))
def writeAmatrixfromkeyboard(object):
    pass

class Matrix: #m - строки n - столбцы
    def __init__(self,size):
        self.matrix = []
        self.m = size[0]
        self.n = size[1]
        for i in range(size[0]):
             self.matrix.append([0] * size[1])
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
        if isinstance(other,int):
            matrixMul = Matrix(len(self.matrix), len(self.matrix[0]))
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    matrixMul.matrix[i][j] = other * self.matrix[i][j]
            return matrixMul.matrix
        elif isinstance(other,object):
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

    def transposeMatrix(self):
        tmp = [[None]* len(x) for x in self.matrix]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                tmp[i][j] = self.matrix[j][i]
        return tmp

    def printMatrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()
        print()

M1 = Matrix(setMatrixSize())
writeAmatrix(M1)