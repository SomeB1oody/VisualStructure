import os
import ctypes

def is_hidden(filepath):
    if os.name == 'nt':  # 针对 Windows 的实现
        # 通过API看
        attribute = ctypes.windll.kernel32.GetFileAttributesW(str(filepath))
        # 检查 FILE_ATTRIBUTE_HIDDEN 属性
        return attribute != -1 and (attribute & 2)  # 文件属性为 -1 时可能出错
    else:
        # 对于非Windows系统，以.开头的文件和文件夹为隐藏
        return os.path.basename(filepath).startswith('.')

def process_path(path):
    if path[-1] == "/" or path[-1] == "\\":
        return path
    else:
        return path + "/"

def generate_folder_structure(folder_path, output_path, include_hidden=False, ignored_paths=None):
    def draw_tree(folder_path, prefix=""):
        entries = sorted(os.listdir(folder_path))
        tree_lines = []
        for i, entry in enumerate(entries):
            entry_path = os.path.join(folder_path, entry)
            if entry_path in ignored_paths:
                continue
            if not include_hidden and is_hidden(entry_path):
                continue  # 跳过隐藏文件和文件夹
            if i == len(entries) - 1:
                tree_lines.append(f"{prefix}└── {entry}/" if os.path.isdir(entry_path) else f"{prefix}└── {entry}")
                new_prefix = f"{prefix}    "
            else:
                tree_lines.append(f"{prefix}├── {entry}/" if os.path.isdir(entry_path) else f"{prefix}├── {entry}")
                new_prefix = f"{prefix}│   "
            if os.path.isdir(entry_path):
                tree_lines.extend(draw_tree(entry_path, new_prefix))
        return tree_lines

    if not os.path.isdir(folder_path):
        raise ValueError(f"path '{folder_path}' is not a valid directory")

    folder_structure = draw_tree(folder_path)
    path = process_path(output_path) + "folder_structure.txt"
    with open(path, "", encoding="utf-8") as f:
        f.write("\n".join(folder_structure))

    print(f"Structure saved as {path}")


def main():
    folder_path = input("Enter path: ").strip()
    output_path = input("Enter path for output: ").strip()
    include_hidden = input("Include hidden files and folders? (yes/no): ").strip().lower() == 'yes'
    print("Enter paths to ignore, one per line. Enter two newlines to finish: ")
    ignored_paths = []
    while True:
        path = input().strip()
        if path == "":
            break
        ignored_paths.append(path)

    try:
        generate_folder_structure(folder_path, output_path, include_hidden, ignored_paths)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
