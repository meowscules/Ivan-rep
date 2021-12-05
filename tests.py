
from Entity.MatrixClass import *

if __name__ == '__main__':
    M1 = Matrix(1, setMatrixRows(), )
    M2 = Matrix(1, setMatrixRows(), )
    # test1
    M1.printMatrix()
    M2.printMatrix()
    # # test2
    # print(M1.transposeMatrix())
    # print(M2.transposeMatrix())
    # # test3
    # print(M1 * M2)
    # # test4
    print(M1 == M2)
    # # test5
    # print(M1 - M2)
    # # test6
    # print(M1 * 3)