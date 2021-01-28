import sys
from PyQt5 import QtWidgets
import sqlite3

class Window(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.make_connection()

        self.init_ui()
    def make_connection(self): #database connector
        connection = sqlite3.connect("../database.db")

        self.cursor = connection.cursor()

        self.cursor.execute("Create table if not exists Users (user_name TEXT, user_password TEXT)")

        connection.commit()

    def init_ui(self):

        self.user_name = QtWidgets.QLineEdit()
        self.user_password = QtWidgets.QLineEdit()
        self.user_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")
        self.signup = QtWidgets.QPushButton("Create New Account")

        self.text_area = QtWidgets.QLabel("")

        self.login.setStyleSheet("background-color : blue")
        self.signup.setStyleSheet("background-color : green")


        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.user_name)
        v_box.addWidget(self.user_password)
        v_box.addWidget(self.text_area)
        v_box.addStretch()
        v_box.addWidget(self.login)
        v_box.addWidget(self.signup)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.setWindowTitle("Login Window")
        self.login.clicked.connect(self.login_func)
        self.signup.clicked.connect(self.signup_func)
        self.show()

    def login_func(self):
        name = self.user_name.text()
        password= self.user_password.text()

        self.cursor.execute("Select * from Users where user_name = ? and user_password = ?",(name,password))

        data = self.cursor.fetchall()

        if len(data)==0:
            self.text_area.setText("User name can not be emtpy\n")
        else:
            self.text_area.setText("Welcome Dear " + name)
    def signup_func(self):
        self.newWindow = SignupWindow()
        self.newWindow.setGeometry(500,250,300,300)
        self.newWindow.show()

class SignupWindow(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.make_connection()

        self.init_ui()
    def make_connection(self): #database connector
        connection = sqlite3.connect("../database.db")

        self.cursor = connection.cursor()

        self.cursor.execute("Create table if not exists Users (user_name TEXT, user_password TEXT)")

        connection.commit()

    def init_ui(self):
        self.user_name = QtWidgets.QLineEdit()
        self.user_password1 = QtWidgets.QLineEdit()
        self.user_password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.user_password2 = QtWidgets.QLineEdit()
        self.user_password2.setEchoMode(QtWidgets.QLineEdit.Password)
        if self.user_password1 == self.user_password2:
            flag = 1
        self.signup = QtWidgets.QPushButton("Create New Account")

        self.text_area = QtWidgets.QLabel("")
        self.text_area1 = QtWidgets.QLabel("User Name")
        self.text_area2 = QtWidgets.QLabel("Password")
        self.text_area3 = QtWidgets.QLabel("Password(Again)")


        self.signup.setStyleSheet("background-color : green")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.text_area1)
        v_box.addWidget(self.user_name)
        v_box.addWidget(self.text_area2)
        v_box.addWidget(self.user_password1)
        v_box.addWidget(self.text_area3)
        v_box.addWidget(self.user_password2)
        v_box.addWidget(self.text_area)
        v_box.addStretch()
        v_box.addWidget(self.signup)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.signup.clicked.connect(self.signup_func)

    def signup_func(self):
        if (self.user_password1.text() != self.user_password2.text() or self.user_password1== "" or self.user_password2 == ""):
            self.text_area.setText("The passwords are not same.\n")
        elif(self.user_password1.text()==self.user_password2.text()):
            name = self.user_name.text()
            password = self.user_password1.text()
            connection = sqlite3.connect("../database.db")
            self.cursor.execute("Insert into Users Values(?,?)",(name,password))
            self.text_area.setText("The registration has been completed successfully.\n")
            connection.commit()
        elif(self.user_name.text() == "" or self.user_name.text() == " "):
            self.text_area.setText("Name can not be empty.\n")
        else:
            self.text_area.setText("Lütfen şifre ve ismi kontrol ediniz.")


app = QtWidgets.QApplication(sys.argv)

window = Window()
window.setGeometry(400,200,300,300)

sys.exit(app.exec_())
