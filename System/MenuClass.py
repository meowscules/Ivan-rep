from Entity.MatrixClass import *


class Menu:
    @staticmethod
    def menu():
        for chose in range(1):
            print(f"{chose + 1}: Create matrix")
            print(f"{chose + 1}: Calculate")
            print(f"{chose + 1}: temporary is missing")
            print(f"{chose + 1}: temporary is missing")
            print(f"{chose + 1}: temporary is missing")

    def menuStart(self):
        self.menu()
        chose = input("Make a choice")
        while True:
            if chose == 1:
                self.createMatrix()
            if chose == 2:

    def createMatrix(self):
        m1 = Matrix(setMatrixRows(), setMatrixCols())

