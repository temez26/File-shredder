from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QFileDialog, QLabel, QSpacerItem, QSizePolicy, QScrollArea, QVBoxLayout, QLineEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QEvent, QPropertyAnimation, QEasingCurve
from file_remover import remove_files
from style_manager import StyleManager

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.style_manager = StyleManager(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Shredder')
        self.setGeometry(100, 100, 400, 300)

        layout = QGridLayout()
        self.setWindowIcon(QIcon('shredder.png'))

        self.title_label = QLabel('File Shredder', self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.style_manager.apply_style(self.title_label, 'title')

        self.instructions_label = QLabel('Select a directory and enter the file extension to remove.', self)
        self.instructions_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.style_manager.apply_style(self.instructions_label, 'instructions')

        self.label = QLabel('Write filetype', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.style_manager.apply_style(self.label, 'label')

        self.extension_input = QLineEdit(self)
        self.extension_input.setPlaceholderText('Enter file extension (e.g., .json)')
        self.style_manager.apply_style(self.extension_input, 'input')

        self.button = QPushButton('Browse', self)
        self.style_manager.apply_style(self.button, 'button')
        self.button.clicked.connect(self.select_directory)

        self.result_label = QLabel('', self)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.style_manager.apply_style(self.result_label, 'result')

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
        layout.addWidget(self.extension_input, 2, 1)
        layout.addWidget(self.button, 2, 2)
        layout.addWidget(self.result_label, 3, 0, 1, 3)
        layout.addWidget(self.failed_paths_area, 4, 0, 1, 3)
       

        self.setLayout(layout)
        self.setStyleSheet("""
            background-color: #121212;
            color: white;
            font-family: 'Segoe UI', sans-serif;           
        """)
        self.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.Resize:
            self.style_manager.update_styles()
        elif event.type() == QEvent.Type.Enter and source == self.button:
            self.button_animation.start()
        return super().eventFilter(source, event)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        file_extension = self.extension_input.text().strip()
        if directory and file_extension:
            success, failed, failed_paths = remove_files(directory, file_extension)
            if failed == 0:
                self.result_label.setText(f'All {file_extension} files removed successfully!\nFiles removed: {success}')
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