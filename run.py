from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from pyshorteners import Shortener
from PyQt5.QtCore import pyqtSlot

def CREATE_SHORT_URL(url):
    link = Shortener()
    return link.tinyurl.short(url)

class qrCode(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interface.ui", self)
        self.show()
        self.btn1.clicked.connect(self.btn1_clicked)
    def getURL(self):
        return self.lineEdit.text()
    
    def setURLcurta(self, url):
        self.lineEdit_2.setText(url)
        
    @pyqtSlot()
    def btn1_clicked(self):
        valor = self.getURL()
        if valor:
            url = CREATE_SHORT_URL(valor)
            self.setURLcurta(url)
        else:
            self.showMessage("errou, digite algo")

    def showMessage(self, title, message):
        QMessageBox.information(self, title, message)
    
if __name__ == "__main__":
    app = QApplication([])
    tela = qrCode()
    app.exec_()
