import os

def process_path(path):
    if path[-1] == "/" or path[-1] == "\\":
        return path
    else:
        return path + "/"

def generate_folder_structure(folder_path, output_path):
    def draw_tree(folder_path, prefix=""):
        entries = sorted(os.listdir(folder_path))  # 获取并排序目录下的所有条目
        tree_lines = []
        for i, entry in enumerate(entries):
            entry_path = os.path.join(folder_path, entry)  # 连接路径
            if i == len(entries) - 1:  # 当前目录中的最后一个条目
                tree_lines.append(f"{prefix}└── {entry}/" if os.path.isdir(entry_path) else f"{prefix}└── {entry}")
                new_prefix = f"{prefix}    "
            else:
                tree_lines.append(f"{prefix}├── {entry}/" if os.path.isdir(entry_path) else f"{prefix}├── {entry}")
                new_prefix = f"{prefix}│   "
            if os.path.isdir(entry_path):  # 如果条目是目录，递归调用
                tree_lines.extend(draw_tree(entry_path, new_prefix))
        return tree_lines

    # 检查目录路径是否有效
    if not os.path.isdir(folder_path):
        raise ValueError(f"path '{folder_path}' is not a valid directory")

    # 生成目录结构
    folder_structure = draw_tree(folder_path)

    path = process_path(output_path) + "folder_structure.txt"

    # 将目录结构写入输出文件
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(folder_structure))

    print(f"structure saved as {path}")


def main():
    # 获取用户输入的目录路径和输出文件路径
    folder_path = input("Enter path: ").strip()
    output_path = input("Enter path for output: ").strip()

    # 调用 generate_folder_structure 函数，并处理潜在的错误
    try:
        generate_folder_structure(folder_path, output_path)
    except Exception as e:
        print(f"Error: {e}")


# 脚本的入口
if __name__ == "__main__":
    main()