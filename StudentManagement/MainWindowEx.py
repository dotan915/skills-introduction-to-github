import base64
import traceback
import mysql.connector
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog, QMessageBox
from MainWindow import Ui_MainWindow


class MainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()        # QMainWindow init
        # avatar mặc định
        self.default_avatar = "images/ic_no_avatar.jpg"

        # biến dữ liệu
        self.id = None
        self.code = None
        self.name = None
        self.age = None
        self.avatar = None
        self.intro = None

        # gắn signal/slot
        self.tableWidgetStudent.itemSelectionChanged.connect(self.processItemSelection)
        self.pushButtonAvatar.clicked.connect(self.pickAvatar)
        self.pushButtonRemoveAvatar.clicked.connect(self.removeAvatar)
        self.pushButtonInsert.clicked.connect(self.processInsert)
        self.pushButtonUpdate.clicked.connect(self.processUpdate)
        self.pushButtonRemove.clicked.connect(self.processRemove)

        # kết nối DB và load dữ liệu
        try:
            self.connectMySQL()
            print("✅ Connected to MySQL")
            self.selectAllStudent()
        except:
            traceback.print_exc()


    # ------------------- DATABASE -------------------
    def connectMySQL(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            database="studentmanagement",
            user="root",
            password="tan@12345"
        )

    def selectAllStudent(self):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        dataset = cursor.fetchall()

        self.tableWidgetStudent.setRowCount(0)
        for item in dataset:
            row = self.tableWidgetStudent.rowCount()
            self.tableWidgetStudent.insertRow(row)

            self.id = item[0]
            self.code = item[1]
            self.name = item[2]
            self.age = item[3]
            self.avatar = item[4]
            self.intro = item[5]

            self.tableWidgetStudent.setItem(row, 0, QTableWidgetItem(str(self.id)))
            self.tableWidgetStudent.setItem(row, 1, QTableWidgetItem(self.code))
            self.tableWidgetStudent.setItem(row, 2, QTableWidgetItem(self.name))
            self.tableWidgetStudent.setItem(row, 3, QTableWidgetItem(str(self.age)))

        cursor.close()

    # ------------------- CRUD -------------------
    def processItemSelection(self):
        row = self.tableWidgetStudent.currentRow()
        if row == -1:
            return
        try:
            code = self.tableWidgetStudent.item(row, 1).text()
            cursor = self.conn.cursor()
            sql = "SELECT * FROM student WHERE code=%s"
            cursor.execute(sql, (code,))
            item = cursor.fetchone()
            if item:
                self.id = item[0]
                self.code = item[1]
                self.name = item[2]
                self.age = item[3]
                self.avatar = item[4]
                self.intro = item[5]

                self.lineEditId.setText(str(self.id))
                self.lineEditCode.setText(self.code)
                self.lineEditName.setText(self.name)
                self.lineEditAge.setText(str(self.age))
                self.lineEditIntro.setText(self.intro)

                if self.avatar:
                    imgdata = base64.b64decode(self.avatar)
                    pixmap = QPixmap()
                    pixmap.loadFromData(imgdata)
                    self.labelAvatar.setPixmap(pixmap)
                else:
                    self.labelAvatar.setPixmap(QPixmap(self.default_avatar))
            cursor.close()
        except:
            traceback.print_exc()

    def pickAvatar(self):
        filters = "Picture PNG (*.png);;All files(*)"
        filename, _ = QFileDialog.getOpenFileName(self, filter=filters)
        if filename == "":
            return
        pixmap = QPixmap(filename)
        self.labelAvatar.setPixmap(pixmap)

        with open(filename, "rb") as image_file:
            self.avatar = base64.b64encode(image_file.read())

    def removeAvatar(self):
        self.avatar = None
        self.labelAvatar.setPixmap(QPixmap(self.default_avatar))

    def processInsert(self):
        try:
            cursor = self.conn.cursor()
            sql = "INSERT INTO student(Code,Name,Age,Avatar,Intro) VALUES(%s,%s,%s,%s,%s)"

            self.code = self.lineEditCode.text()
            self.name = self.lineEditName.text()
            self.age = int(self.lineEditAge.text())
            self.intro = self.lineEditIntro.text()

            val = (self.code, self.name, self.age, self.avatar, self.intro)
            cursor.execute(sql, val)
            self.conn.commit()

            self.lineEditId.setText(str(cursor.lastrowid))
            cursor.close()
            self.selectAllStudent()
        except:
            traceback.print_exc()

    def processUpdate(self):
        try:
            cursor = self.conn.cursor()
            sql = """UPDATE student 
                     SET Code=%s, Name=%s, Age=%s, Avatar=%s, Intro=%s 
                     WHERE Id=%s"""

            self.id = int(self.lineEditId.text())
            self.code = self.lineEditCode.text()
            self.name = self.lineEditName.text()
            self.age = int(self.lineEditAge.text())
            self.intro = self.lineEditIntro.text()

            val = (self.code, self.name, self.age, self.avatar, self.intro, self.id)
            cursor.execute(sql, val)
            self.conn.commit()
            cursor.close()
            self.selectAllStudent()
        except:
            traceback.print_exc()

    def processRemove(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Confirmation Deleting")
        dlg.setText("Are you sure you want to delete?")
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if dlg.exec() == QMessageBox.StandardButton.No:
            return

        try:
            cursor = self.conn.cursor()
            sql = "DELETE FROM student WHERE Id=%s"
            val = (self.lineEditId.text(),)
            cursor.execute(sql, val)
            self.conn.commit()
            cursor.close()
            self.selectAllStudent()
            self.clearData()
        except:
            traceback.print_exc()

    def clearData(self):
        self.lineEditId.setText("")
        self.lineEditCode.setText("")
        self.lineEditName.setText("")
        self.lineEditAge.setText("")
        self.lineEditIntro.setText("")
        self.avatar = None
        self.labelAvatar.setPixmap(QPixmap(self.default_avatar))
