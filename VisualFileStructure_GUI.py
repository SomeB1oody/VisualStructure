import wx
import os
import ctypes
from subprocess import Popen

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

def generate_folder_structure(folder_path, output_path, include_hidden=False):
    def draw_tree(folder_path, prefix=""):
        entries = sorted(os.listdir(folder_path))
        tree_lines = []
        for i, entry in enumerate(entries):
            entry_path = os.path.join(folder_path, entry)
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

    # 检查目录路径是否有效
    if not os.path.isdir(folder_path):
        raise ValueError(f"path '{folder_path}' is not a valid directory")

    # 生成目录结构
    folder_structure = draw_tree(folder_path)

    path = process_path(output_path) + "folder_structure.txt"

    # 将目录结构写入输出文件
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(folder_structure))

    # 添加打开文件的代码
    try:
        Popen(['notepad.exe', path])
    except Exception as e:
        raise ValueError(f"Error opening file: {e}")

class VisualFileStructureWX(wx.Frame):
    def __init__(self, *args, **kw):
        super(VisualFileStructureWX, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        # 选择文件夹
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.folder_button = wx.Button(panel, label="Select input folder")
        self.Bind(wx.EVT_BUTTON, self.on_select_folder, self.folder_button)
        self.hbox.Add(self.folder_button, flag=wx.ALL, border=5)
        self.input_path_text = wx.StaticText(panel, label="Click \"Select input folder\" first")
        self.hbox.Add(self.input_path_text, flag=wx.ALL, border=5)
        self.vbox.Add(self.hbox, flag=wx.EXPAND)

        # 输出路径
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.folder_button_ = wx.Button(panel, label="Select output folder")
        self.Bind(wx.EVT_BUTTON, self.on_select_folder_, self.folder_button_)
        self.hbox2.Add(self.folder_button_, flag=wx.ALL, border=5)
        self.output_path_text = wx.StaticText(panel, label="Click \"Select output folder\" first")
        self.hbox2.Add(self.output_path_text, flag=wx.ALL, border=5)
        self.vbox.Add(self.hbox2, flag=wx.EXPAND)

        # 是否把目录下隐藏的文件和文件夹写进结构图中
        self.include_hidden_checkbox = wx.CheckBox(panel, label="Include hidden files and folders")
        self.vbox.Add(self.include_hidden_checkbox, flag=wx.ALL, border=5)

        # 生成按钮
        self.generate_button = wx.Button(panel, label="Generate")
        self.vbox.Add(self.generate_button, flag=wx.ALL, border=5)
        self.generate_button.Bind(wx.EVT_BUTTON, self.on_generate_button)

        # 设置面板的布局管理器
        panel.SetSizer(self.vbox)
        panel.Layout()

    def on_select_folder(self, event):
        with wx.DirDialog(None, "Select a folder", "",
                          style=wx.DD_DEFAULT_STYLE) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.input_path_text.SetLabel(f"{dialog.GetPath()}")
                self.selected_folder = dialog.GetPath()

    def on_select_folder_(self, event):
        with wx.DirDialog(None, "Select a folder for output", "",
                          style=wx.DD_DEFAULT_STYLE) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.output_path_text.SetLabel(f"{dialog.GetPath()}")
                self.selected_output_folder = dialog.GetPath()

    def on_generate_button(self, event):
        input_path = self.selected_folder
        output_path = self.selected_output_folder
        include_hidden = self.include_hidden_checkbox.GetValue()

        if not input_path:
            wx.MessageBox("Please select input folder first", "Error", wx.OK | wx.ICON_ERROR)
            return
        if not output_path:
            wx.MessageBox("Please select output folder first", "Error", wx.OK | wx.ICON_ERROR)
            return

        try:
            generate_folder_structure(input_path, output_path, include_hidden)
            wx.MessageBox(
                "Folder structure generated successfully", "Success", wx.OK | wx.ICON_INFORMATION
            )
        except Exception as e:
            wx.MessageBox(f"Error: {e}", "Error", wx.OK | wx.ICON_ERROR)
            return

if __name__ == "__main__":
    app = wx.App()
    frame = VisualFileStructureWX(None)
    frame.SetTitle('Visual File Structure with GUI')
    frame.SetSize((400, 200))
    frame.Show()
    app.MainLoop()
