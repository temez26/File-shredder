from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QFileDialog, QMessageBox, QLabel, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt, QEvent, QPropertyAnimation, QEasingCurve
from file_remover import remove_json_files

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Shredder')
        self.setGeometry(100, 100, 300, 200)

        layout = QGridLayout()
        self.setWindowIcon(QIcon('shredder.png'))

        self.label = QLabel('Select Directory', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_label_style()

        self.button = QPushButton('Browse', self)
        
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #0078f2;
                color: white;
                font-size: 20px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
        """)
        self.button.clicked.connect(self.select_directory)

        self.button_animation = QPropertyAnimation(self.button, b"geometry")
        self.button_animation.setDuration(300)
        self.button_animation.setStartValue(self.button.geometry())
        self.button_animation.setEndValue(self.button.geometry().adjusted(0, 0, 10, 10))
        self.button_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.button, 0, 1)
        layout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum), 0, 2)

        self.setLayout(layout)
        self.setStyleSheet("""
            background-color: #121212;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        """)
        self.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.Resize:
            self.update_label_style()
        elif event.type() == QEvent.Type.Enter and source == self.button:
            self.button_animation.start()
        return super().eventFilter(source, event)

    def update_label_style(self):
        window_width = self.width()
        padding_left = window_width * 0.1  # 10% of the window width
        self.label.setStyleSheet(f"""
            padding-left: {padding_left}px;
            font-size: 20px;
            color: white;
        """)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if directory:
            remove_json_files(directory)
            QMessageBox.information(self, 'Success', 'JSON files removed successfully!')