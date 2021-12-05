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
                cls.printMatrices()
            if chose == 4:
                cls.calculateMatrixRows()

    @staticmethod
    def createMatrix():
        db = DataBase()
        MatrixName = input("Matrix name: ")
        RowNo = input("Enter rows quantity: ")
        ColNo = input("Enter cols quantity: ")
        CellValue = input("Enter values: ")
        db.createMatrix(MatrixName, RowNo, ColNo, CellValue)

    @staticmethod
    def deleteMatrix():
        db = DataBase()
        matrixName = input("Print matrix name for deleting matrix: ")
        db.deleteMatrix(matrixName)

    @staticmethod
    def printMatrices():
        db = DataBase()
        db.printMatrix()

    @staticmethod
    def calculateMatrixRows():
        db = DataBase()
        matrixName = input("Select matrix: ")
        M1 = Matrix(db.readMatrixRows(matrixName), db.readMatrixRows(matrixName), db.readMatrixValues(matrixName))
        M1.printMatrix()
        print(M1.body)
Menu()

