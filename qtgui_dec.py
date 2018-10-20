import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import decrypt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Decrypt")
        self.setGeometry(300,300,300,150)
        self.plainText = QTextEdit(self)
        self.plainText.setGeometry(10,30,280,30)
        self.plainText.setEnabled(True)
        self.button = QPushButton("복호화", self)
        self.button.move(10,60)
        self.button.clicked.connect(self.decShow)
        self.result = QTextEdit(self)
        self.result.setGeometry(10,100,280,30)
        self.result.setEnabled(True)
    
    def decShow(self):
        todecrypt = self.plainText.toPlainText()
        if todecrypt.lstrip().rstrip() != '':
            decrypted = decrypt.decrypt(todecrypt)
            if decrypted == '':
                QMessageBox.about(self, "복호화 실패", "복호화에 실패하였습니다.")
            else:
                QMessageBox.about(self, "복호화 완료", "복호화되었습니다. --> %s" % decrypted)
                self.result.setText(decrypted)
        else:
            QMessageBox.about(self, "복호화", "복호화할 텍스트를 넣어주세요.")


def main():
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

if __name__ == "__main__":
    main()
