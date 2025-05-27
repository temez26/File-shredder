# File Shredder

A Python application for safely removing specific file types from directories and subdirectories.

## Features

- Recursive file deletion by extension
- Graphical user interface built with PyQt6
- Real-time deletion progress tracking
- Error handling and reporting for failed deletions

## Requirements

- Python 3.6+
- PyQt6

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd File-shredder
   ```

2. Install dependencies:
   ```bash
   pip install PyQt6
   ```

## Usage

Run the application:

```bash
python main.py
```

1. Enter the file extension to target (e.g., `.json`, `.txt`)
2. Select the target directory
3. Confirm deletion

## Building Executable

To create a standalone executable:

```bash
pyinstaller --onefile --noconsole --icon=assets/shredder.ico --add-data "assets/shredder.ico;assets" main.py
```
