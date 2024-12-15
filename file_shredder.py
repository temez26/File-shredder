import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox

def remove_json_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")

class FileShredder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Shredder')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.button = QPushButton('Browse', self)
        self.button.clicked.connect(self.select_directory)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if directory:
            remove_json_files(directory)
            QMessageBox.information(self, 'Success', 'JSON files removed successfully!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileShredder()
    ex.show()
    sys.exit(app.exec_())