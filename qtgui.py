import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import encrypt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Encrypt")
        self.setGeometry(300,300,300,150)
        self.plainText = QTextEdit(self)
        self.plainText.setGeometry(10,30,280,30)
        self.plainText.setEnabled(True)
        self.button = QPushButton("암호화", self)
        self.button.move(10,60)
        self.button.clicked.connect(self.encShow)
        self.result = QTextEdit(self)
        self.result.setGeometry(10,100,280,30)
        self.result.setEnabled(True)
    
    def encShow(self):
        toEncrypt = self.plainText.toPlainText()
        if toEncrypt.lstrip().rstrip() != '':
            encrypted = encrypt.encrypt(toEncrypt)
            if encrypted == '':
                QMessageBox.about(self, "암호화 실패", "암호화에 실패하였습니다.")
            else:
                QMessageBox.about(self, "암호화 완료", "암호화되었습니다. --> %s" % encrypted)
                self.result.setText(encrypted)
        else:
            QMessageBox.about(self, "암호화", "암호화할 텍스트를 넣어주세요.")

def main():
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

if __name__ == "__main__":
    main()
