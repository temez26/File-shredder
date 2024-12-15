import unittest
from PyQt6.QtWidgets import QLabel, QApplication, QWidget
from ui.style_manager import StyleManager
import sys

class TestStyleManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
        cls.mock_window = QWidget()
        cls.mock_window.resize(800, 600)  

    def test_apply_style(self):
        label = QLabel()
        style_manager = StyleManager(self.mock_window)
        style_manager.apply_style(label, 'title')
        self.assertIn('font-size:', label.styleSheet())

if __name__ == '__main__':
    unittest.main()