import os

def remove_files(directory, file_extension):
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

                except Exception as e:
                    failed += 1
                    failed_paths.append(file_path)
                    print(f"Error removing {file_path}: {e}")

    success = count - failed
    print(f"Success: {success}, Failed: {failed}")
    return success, failed, failed_paths