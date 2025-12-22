import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6 import uic

class MyApp(QWidget):
    def __init__ (self):
        super().__init__()
        #Initialize Window
        self.setWindowTitle("Hello")
        self.setWindowIcon(QIcon('c:\\Users\\docto\\OneDrive\\Documents\\Github\\Personal-and-University-Projects\\Python\\PyQt6\\z.ico'))
        self.resize(1080, 720)

        #Initialize Layout
        layout= QVBoxLayout()
        self.setLayout(layout)
        
        #Initialize Contents
        self.input= QLineEdit()
        self.button= QPushButton("Say Hello")
        self.button.clicked.connect(self.sayHello)
        self.output= QTextEdit()

        #Connect Contents to the Layout Window
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.output)

    def sayHello(self):
        self.output.setText('Hello {0}'.format(self.input.text()))

app= QApplication([])
window= MyApp()
window.show()
app.exec()