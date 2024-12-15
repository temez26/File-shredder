import os

def remove_files(directory, file_extension, result_label):
    count = 0
    failed = 0
    failed_paths = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    count += 1
                    print(f"Removed: {file_path}")
                    result_label.setText(f"Deleting... {count} files removed")
                    result_label.repaint()  # Force update the label to show the progress
                except Exception as e:
                    failed += 1
                    failed_paths.append(file_path)
                    print(f"Error removing {file_path}: {e}")

    success = count - failed
    print(f"Success: {success}, Failed: {failed}")
    return success, failed, failed_paths