import os
import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            print(f"Successfully loaded JSON data from {file_path}")
            return data
        except json.JSONDecodeError as e:
            print(f"Error loading JSON from {file_path}: {e}")
            raise

def rename_files_in_directory(directory, a_json_path, b_json_path):
    # Load JSON data
    a_data = load_json(a_json_path)
    b_data = load_json(b_json_path)

    # Ensure a_data and b_data have the same length
    if len(a_data) != len(b_data):
        raise ValueError("a.json and b.json must have the same number of lines")

    # Create a mapping from a_data to b_data
    rename_map = dict(zip(a_data, b_data))

    # List all .png files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            file_without_ext = os.path.splitext(filename)[0]
            if file_without_ext in rename_map:
                new_name = rename_map[file_without_ext] + '.png'
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' to '{new_name}'")

# Example usage
directory = 'path/to/file'  # 指定目录路径
a_json_path = 'path/to/file/a.json'   # a.json 文件路径
b_json_path = 'path/to/file/b.json'   # b.json 文件路径

rename_files_in_directory(directory, a_json_path, b_json_path)
