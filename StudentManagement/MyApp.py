from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindowEx import MainWindowEx
from MainWindow import Ui_MainWindow
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Tạo một QMainWindow
    MainWindow = QMainWindow()
    ui = MainWindowEx()
    # ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Hiển thị giao diện
    MainWindow.show()

    sys.exit(app.exec())
