import sqlite3
from Entity.DataBaseException import *


class DataBase:
    global db
    global cur
    db = sqlite3.connect('matrix.db')
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS matrices
                                     (MatrixName varchar(24) NOT NULL,
                                     RowNo smallint NOT NULL,
                                     ColNo smallint NOT NULL,
                                     CellValue varchar(50) NULL)
                                     """)
    db.commit()

    @staticmethod
    def createMatrix():
        MatrixName = input("Matrix name: ")
        RowNo = input("Enter rows quantity")
        ColNo = input("Enter cols quantity")
        CellValue = input("Enter values")
        cur.execute("INSERT INTO matrices VALUES (?, ?, ?, ?)", (MatrixName, RowNo, ColNo, CellValue))
        db.commit()

    @staticmethod
    def deleteMatrix():
        cur.execute("SELECT * FROM matrices")
        if cur.fetchone() is not None:
            matrixName = input("Print matrix name for deleting matrix: ")
            cur.execute("SELECT MatrixName FROM matrices")
            tmp = cur.fetchone()
            if tmp == matrixName:
                cur.execute(f"DELETE FROM matrices WHERE MatrixName = '{matrixName}'")
                db.commit()
                print("Matrix deleted!")
                print()
            else:
                print("Record is missing")
        else:
            raise DataBaseRecordError

    @staticmethod
    def printMatrix():
        cur.execute("SELECT MatrixName FROM matrices")
        if cur.fetchone() is not None:
            for value in cur.execute("SELECT * FROM matrices"):
                print(value)
                print()
        else:
            raise DataBaseRecordError

    @staticmethod
    def readMatrix():
        for value in cur.execute("SELECT CellValue FROM matrices"):
            for i in value:
                for j in range(len(i)):
                    return i[j]





