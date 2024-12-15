from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QFileDialog, QLabel, QSpacerItem, QSizePolicy, QScrollArea, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QEvent, QPropertyAnimation, QEasingCurve
from file_remover import remove_json_files
import webbrowser

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Shredder')
        self.setGeometry(100, 100, 400, 300)

        layout = QGridLayout()
        self.setWindowIcon(QIcon('shredder.png'))

        self.title_label = QLabel('File Shredder', self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_title_label_style()

        self.instructions_label = QLabel('Select a directory to remove all JSON files.', self)
        self.instructions_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_instructions_label_style()

        self.label = QLabel('Select Directory', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_label_style()

        self.button = QPushButton('Browse', self)
        self.button.setFixedSize(150, 40)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #0078f2;
                color: white;
                font-size: 20px;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
        """)
        self.button.clicked.connect(self.select_directory)

        self.result_label = QLabel('', self)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("""
            background-color:red;
            font-size: 16px;
            color: white;
        """)

        self.failed_paths_area = QScrollArea(self)
        self.failed_paths_area.setWidgetResizable(True)
        self.failed_paths_widget = QWidget()
        self.failed_paths_layout = QVBoxLayout()
        self.failed_paths_widget.setLayout(self.failed_paths_layout)
        self.failed_paths_area.setWidget(self.failed_paths_widget)
        self.failed_paths_area.setFixedHeight(100)

        self.button_animation = QPropertyAnimation(self.button, b"geometry")
        self.button_animation.setDuration(300)
        self.button_animation.setStartValue(self.button.geometry())
        self.button_animation.setEndValue(self.button.geometry().adjusted(0, 0, 10, 10))
        self.button_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        layout.addWidget(self.title_label, 0, 0, 1, 3)
        layout.addWidget(self.instructions_label, 1, 0, 1, 3)
        layout.addWidget(self.label, 2, 0)
        layout.addWidget(self.button, 2, 1)
        layout.addWidget(self.result_label, 3, 0, 1, 3)
        layout.addWidget(self.failed_paths_area, 4, 0, 1, 3)
        layout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum), 2, 2)

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
            self.update_button_style()
            self.update_title_label_style()
            self.update_instructions_label_style()
        elif event.type() == QEvent.Type.Enter and source == self.button:
            self.button_animation.start()
        return super().eventFilter(source, event)

    def update_label_style(self):
        window_width = self.width()
        font_size = max(10, window_width // 30)
        padding_left = window_width * 0.1
        self.label.setStyleSheet(f"""
            padding-left: {padding_left}px;
            font-size: {font_size}px;
            color: white;
        """)

    def update_button_style(self):
        window_width = self.width()
        font_size = max(10, window_width // 30)# Adjust font size based on window width
        padding = max(5, window_width // 100)    # Adjust padding based on window width
        button_width = max(150, window_width // 5)  # Adjust button width based on window width
        button_height = max(40, window_width // 20)  # Adjust button height based on window width
        self.button.setFixedSize(button_width, button_height)
        self.button.setStyleSheet(f"""
            QPushButton {{
                background-color: #0078f2;
                color: white;
                font-size: {font_size}px;
                border-radius: 5px;
                padding: {padding}px;
            }}
            QPushButton:hover {{
                background-color: #005bb5;
            }}
        """)

    def update_title_label_style(self):
        window_width = self.width()
        font_size = max(16, window_width // 25)
        self.title_label.setStyleSheet(f"""
            font-size: {font_size}px;
            font-weight: bold;
            color: white;
            background-color: red;
        """)

    def update_instructions_label_style(self):
        window_width = self.width()
        font_size = max(12, window_width // 40)
        self.instructions_label.setStyleSheet(f"""
            font-size: {font_size}px;
            color: white;
             background-color: red;
        """)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if directory:
            success, failed, failed_paths = remove_json_files(directory)
            if failed == 0:
                self.result_label.setText(f'All JSON files removed successfully!\nFiles removed: {success}')
            else:
                self.result_label.setText(f'Some deletions were not successful\nFiles removed: {success}, Failed: {failed}')
                self.show_failed_paths(failed_paths)

    def show_failed_paths(self, failed_paths):
        for i in reversed(range(self.failed_paths_layout.count())): 
            self.failed_paths_layout.itemAt(i).widget().deleteLater()
        for path in failed_paths:
            path_label = QLabel(f'<a href="file:///{path}">{path}</a>', self)
            path_label.setOpenExternalLinks(True)
            path_label.setStyleSheet("color: white;")
            self.failed_paths_layout.addWidget(path_label)