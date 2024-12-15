from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon
from file_remover import remove_json_files

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Shredder')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.setWindowIcon(QIcon('shredder.png'))


        self.button = QPushButton('Browse', self)
        self.button.clicked.connect(self.select_directory)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if directory:
            remove_json_files(directory)
            QMessageBox.information(self, 'Success', 'JSON files removed successfully!')