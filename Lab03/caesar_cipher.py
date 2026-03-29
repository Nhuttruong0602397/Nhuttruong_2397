import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"

        key_text = self.ui.txt_key.toPlainText().strip()
        if not key_text.isdigit():
            QMessageBox.critical(self, "Invalid Key", "Key must be an integer.")
            return

        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": int(key_text)
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data.get("encrypted_message", ""))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                QMessageBox.critical(self, "API Error", f"Status {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"

        key_text = self.ui.txt_key.text().strip()
        if not key_text.isdigit():
            QMessageBox.critical(self, "Invalid Key", "Key must be an integer.")
            return

        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": int(key_text)
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data.get("decrypted_message", ""))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                QMessageBox.critical(self, "API Error", f"Status {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())