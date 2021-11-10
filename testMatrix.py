
def readAmatrix(size):
    matr = [[] for i in range(size)]
    with open("matrix.txt", "r") as f:
        for i in range(len(matr)):
            matr[i] = [int(i) for i in f.readline().split()]
    return matr

readAmatrix(writeAmatrix())

