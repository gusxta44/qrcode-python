from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.uic import loadUi
from pyshorteners import Shortener
from PyQt5.QtCore import pyqtSlot
import qrcode
from PyQt5.QtGui import QPixmap

def CREATE_SHORT_URL(url):
    link = Shortener()
    return link.tinyurl.short(url)

def CREATE_QRCODE(qr):
    # qr = qrcode.QRCode()
    # qr.add_data("teste")
    img = qrcode.make(qr)
    img.save("qr.png")
    

class QrCodeBuilder(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interface.ui", self)

    def getURL(self):
        return self.txtUrl.text()
    
    def setURLCurta(self, url):
        self.txtUrlShort.setText(url)

    @pyqtSlot()
    def on_btnGerar_clicked(self):
        valor = self.getURL()
        if valor:
            url = CREATE_SHORT_URL(valor)
            CREATE_QRCODE(url)
            self.setURLCurta(url)
            self.img.setPixmap(QPixmap("qr.png"))
            self.btnSalvar.setEnabled(True)
        else:
            self.showMessage("inválido")

    @pyqtSlot()
    def on_btnSalvar_clicked(self):
        self.salvar()

    def salvar(self):
        nomeArquivo, _ = QFileDialog.getSaveFileName(self, "salvar imagem")
        if nomeArquivo:
            caminho = path.dirname(nomeArquivo)
            nome = nomeArquivo.removeprefix(caminho)

            with open("qrcode.png", "rb") as fotoQrcode:
                dadosQrcode = fotoQrcode.read()
        
            with open(caminho +f"{nome}.png", "wb") as foto:
                foto.write(dadosQrcode)
                

    def showMessage(self, title, message):
        QMessageBox.information(self, title, message)

# -----------------------------
if __name__ == "__main__":
    app = QApplication([])
    window = QrCodeBuilder()
    window.show()
    app.exec_()