# VisualStructure
*Easy way to generate structure diagram of your files*
*轻松生成文件结构图的工具*

---
## 1. Intro 简介
**VisualStructure** is a lightweight program for generating structural diagrams, using `├──`, `│`, and `└──` to represent branch relationships. It exports the diagram as a text document, making file management and searching more convenient.
**VisualStructure** 是一个用于生成结构图的轻量级程序，使用 `├──`、`│` 和 `└──` 来表示分支关系。它将结构图导出为文本文档，从而使文件管理和搜索更加方便。

Each program comes with both a non-GUI and a GUI version. The non-GUI version offers the simplest operations and code, making it easier to understand. The GUI version supports more complex operations, providing a more advanced and user-friendly experience.
每个程序都提供了 GUI 和非 GUI 版本。非 GUI 版本提供最简单的操作和代码，更易于理解；而 GUI 版本支持更复杂的操作，提供更高级且用户友好的体验。

Due to my limited capabilities, the code may have some imperfections. I warmly welcome everyone to share their suggestions and contribute to the project. For more details, please see the Contribution. Thank you for your understanding!
由于个人能力有限，代码可能存在一些不足，热烈欢迎大家分享建议并为项目做出贡献。详细信息请参考贡献。感谢您的理解！

---
## 2. Function 功能

**VisualStructure** uses Python's `os` library to retrieve directory and file information, employing `├──`, `│`, and `└──` to represent branch relationships. The front-end is built with the `wxPython` library, ensuring an exceptionally lightweight experience. Users only need to input the path of the folder for which they want to generate the structure diagram and the output file path.
**VisualStructure** 使用 Python 的 `os` 库来检索目录和文件信息，并使用 `├──`、`│` 和 `└──` 表示分支关系。前端基于 `wxPython` 库开发，确保了极为轻量的使用体验。用户只需输入希望生成结构图的文件夹路径和输出文件路径即可。

All folders end with a `/`, and all files are labeled with their extensions, ensuring clear differentiation between directories and files.
所有文件夹以 `/` 结尾，所有文件以其扩展名标注，确保目录和文件之间有清晰的区分。

---
# 3. Required environment 要求环境

Python should be at least 3.8.
Python 版本需至少为 3.8。

All GUI-version files require `wxPython`:
所有 GUI 版本的文件都需要 `wxPython`：
```bash
pip install wxPython
```

---
## 4. Example 实例

Using [BarcodeMaster](https://github.com/SomeB1oody/BarcodeMaster) as an example:
以 [BarcodeMaster](https://github.com/SomeB1oody/BarcodeMaster)为例：
![VS_example](https://github.com/user-attachments/assets/9db1d30a-e20e-4463-b0c8-386fffcac01b)

---

## 5. Contribution 贡献

Contributions are welcome! Follow these steps:
欢迎贡献！请按照以下步骤操作：
 - 1. Fork project.
      Fork 项目。
 - 2. Create branch:
      创建分支：
 ```bash
 git checkout -b feature-name
```
- 3. Submit changes:
     提交更改：
```bash
git commit -m "Explain changes"
```
- 4. Push branch:
     推送分支：
```bash
git push orgin feature-name
```
- 5. Submit Pull Request.
     提交拉取请求。

---
## 6. License 证书

This project uses [MIT LICENSE](https://github.com/SomeB1oody/VisualStructure/blob/main/LICENSE).
本项目使用 [MIT LICENSE](https://github.com/SomeB1oody/VisualStructure/blob/main/LICENSE)。

---
## 7. Contact information 联系方式

- Email: stanyin64@gmail.com
- GitHub: [@SomeB1ooody](https://github.com/SomeB1oody)
