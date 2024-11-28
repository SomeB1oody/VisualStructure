import wx
import os
from subprocess import Popen

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

        if not input_path:
            wx.MessageBox("Please select input folder first", "Error", wx.OK | wx.ICON_ERROR)
            return
        if not output_path:
            wx.MessageBox("Please select output folder first", "Error", wx.OK | wx.ICON_ERROR)
            return

        try:
            generate_folder_structure(input_path, output_path)
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
    frame.SetSize((400, 150))
    frame.Show()
    app.MainLoop()