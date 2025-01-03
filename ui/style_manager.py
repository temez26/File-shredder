class StyleManager:
    def __init__(self, window):
        self.window = window

    def apply_style(self, widget, widget_type):
        window_width = self.window.width()
        if widget_type == 'title':
            font_size = max(16, window_width // 25)
            widget.setStyleSheet(f"""
                font-size: {font_size}px;
                font-weight: bold;
                color: white;
                
            """)
        elif widget_type == 'instructions':
            font_size = max(12, window_width // 40)
            widget.setStyleSheet(f"""
                font-size: {font_size}px;
                color: white;
                
            """)
        elif widget_type == 'label':
            font_size = max(10, window_width // 30)
            widget.setStyleSheet(f"""
                font-size: {font_size}px;
                color: white;
            """)
        elif widget_type == 'button':
            font_size = max(10, window_width // 30)
            padding = max(5, window_width // 150)
        
            widget.setStyleSheet(f"""
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
        elif widget_type == 'result':
            widget.setStyleSheet("""
              
                font-size: 16px;
                color: white;
            """)
        elif widget_type == 'input':
            font_size = max(10, window_width // 30)
            widget.setStyleSheet(f"""
                QLineEdit {{
                    font-size: {font_size}px;
                    color: white;
                    background-color: #333;
                    border: 1px solid #555;
                    padding: 5px;
                }}
                QLineEdit::placeholder {{
                    color: #888;
                }}
            """)

    def update_styles(self):
        self.apply_style(self.window.title_label, 'title')
        self.apply_style(self.window.instructions_label, 'instructions')
        self.apply_style(self.window.label, 'label')
        self.apply_style(self.window.button, 'button')
        self.apply_style(self.window.extension_input, 'input')