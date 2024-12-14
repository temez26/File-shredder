# File Shredder 🗑️

**File Shredder** is a simple Python script to delete specific types of files (e.g., `.json`) from a directory and its subdirectories. 🚀

## Features ✨

- Recursively searches and deletes files.
- Easy to customize for any file type.

## Requirements 🛠️

- Python 3.6 or higher installed on your system.

## Usage 🚀

1. Edit the script to set your target directory and file type.
   ```python
   base_directory = r'insert root filepath here'
   if file.endswith('.json'):  # Change ".json" to your desired file extension
   ```
2. Run the script:
   ```bash
   $ python file_shredder.py
   ```

## Example 🖥️

If you want to delete `.txt` files (or any other), replace `.json` with `.txt` in the script. The updated script will now remove `.txt` files instead.

---

Happy Cleaning! 🧹✨
