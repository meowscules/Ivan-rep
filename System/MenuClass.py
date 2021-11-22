from Entity.MatrixClass import Matrix
from Entity.DataBaseClass import DataBase



class Menu:
    @staticmethod
    def mainMenu():
        print("1: Create matrix")
        print("2: Delete matrix")
        print("3: Show existing records")
        print("4: Calculate matrices")
        print("5: temporary is missing")
        print()

    @staticmethod
    def calculateMenu():
        print("1: Compare matrices")
        print("2: Sum up matrices")
        print("3: Subtract first matrix from second")
        print("4: Transpose matrices")
        print("5: Multiply matrices")
        print("6: Multiply matrix on number")
        print()

    def __new__(cls):
        while True:
            cls.mainMenu()
            chose = int(input("Make a choice "))
            if chose == 1:
                cls.createMatrix()
            if chose == 2:
                cls.deleteMatrix()
            if chose == 3:
                cls.printMatrix()
            if chose == 4:
                cls.calculateMatrix()

    @staticmethod
    def createMatrix():
        db = DataBase()
        db.createMatrix()

    @staticmethod
    def deleteMatrix():
        db = DataBase()
        db.deleteMatrix()

    @staticmethod
    def printMatrix():
        db = DataBase()
        db.printMatrix()

    @staticmethod
    def calculateMatrix():
        db = DataBase()



Menu()

