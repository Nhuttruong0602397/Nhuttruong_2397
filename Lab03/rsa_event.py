import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối các nút với hàm xử lý
        # Lưu ý: Kiểm tra chính xác tên object btnGen...eKeys trong Designer                                                                          may chu tieng viet doi thanh tieng anh 
        self.ui.btnGenerateKeys.clicked.connect(self.call_api_gen_keys)
        self.ui.btnEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btnDecrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btnSign.clicked.connect(self.call_api_sign)
        self.ui.btnVerify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        try:
            res = requests.get("http://127.0.0.1:5000/api/rsa/generate_keys")
            if res.status_code == 200:
                QMessageBox.information(self, "Thông báo", res.json().get("message", "Đã tạo khóa!"))
            else:
                QMessageBox.warning(self, "Lỗi", "Không thể kết nối API tạo khóa")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi kết nối", str(e))

    def call_api_encrypt(self):
        # Lấy text từ ô txtPlantext (QPlainTextEdit)
        payload = {
            "message": self.ui.txtPlantext.toPlainText(),
            "key_type": "public"
        }
        try:
            res = requests.post("http://127.0.0.1:5000/api/rsa/encrypt", json=payload)
            if res.status_code == 200:
                data = res.json()
                self.ui.txtCiphertext.setPlainText(data.get("encrypted_message", ""))
                QMessageBox.information(self, "Thành công", "Đã mã hóa dữ liệu")
            else:
                QMessageBox.warning(self, "Lỗi", "API mã hóa gặp sự cố")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def call_api_decrypt(self):
        payload = {
            "ciphertext": self.ui.txtCiphertext.toPlainText(),
            "key_type": "private"
        }
        try:
            res = requests.post("http://127.0.0.1:5000/api/rsa/decrypt", json=payload)
            if res.status_code == 200:
                data = res.json()
                self.ui.txtPlantext.setPlainText(data.get("decrypted_message", ""))
                QMessageBox.information(self, "Thành công", "Đã giải mã dữ liệu")
            else:
                QMessageBox.warning(self, "Lỗi", "API giải mã gặp sự cố")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def call_api_sign(self):
        # Lấy dữ liệu từ ô txtInformation (Trong ảnh là txtIn...ation)
        payload = {
            "message": self.ui.txtInformation.toPlainText() 
        }
        try:
            res = requests.post("http://127.0.0.1:5000/api/rsa/sign", json=payload)
            if res.status_code == 200:
                data = res.json()
                self.ui.txtSignature.setPlainText(data.get("signature", ""))
                QMessageBox.information(self, "Thành công", "Đã ký số")
            else:
                QMessageBox.warning(self, "Lỗi", "API ký số gặp sự cố")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def call_api_verify(self):
        payload = {
            "message": self.ui.txtInformation.toPlainText(),
            "signature": self.ui.txtSignature.toPlainText()
        }
        try:
            res = requests.post("http://127.0.0.1:5000/api/rsa/verify", json=payload)
            if res.status_code == 200:
                verified = res.json().get("is_verified", False)
                if verified:
                    QMessageBox.information(self, "Kết quả", "Chữ ký HỢP LỆ!")
                else:
                    QMessageBox.warning(self, "Kết quả", "Chữ ký GIẢ MẠO!")
            else:
                QMessageBox.warning(self, "Lỗi", "API xác minh gặp sự cố")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())