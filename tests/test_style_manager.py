import unittest
from PyQt6.QtWidgets import QLabel
from ui.style_manager import StyleManager

class TestStyleManager(unittest.TestCase):
    def test_apply_style(self):
        label = QLabel()
        style_manager = StyleManager(None)
        style_manager.apply_style(label, 'title')
        self.assertIn('font-size: 24px;', label.styleSheet())

if __name__ == '__main__':
    unittest.main()