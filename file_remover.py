import os

def remove_json_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                Count = 0
                Failed = 0

                try:
                    os.remove(file_path)
                    Count + 1
                    print(f"Removed: {file_path}")


                except Exception as e:
                    Failed + 1
                    print(f"Error removing {file_path}: {e}")
            Success = Count - Failed 
            print(f"Success: {Success}")       