# VisualStructure
*Easy way to generate structure diagram of your files*

---
## 1. Intro
**VisualStructure** is a lightweight program for generating structural diagrams, using `├──`, `│`, and `└──` to represent branch relationships. It exports the diagram as a text document, making file management and searching more convenient.


Each program comes with both a non-GUI and a GUI version. The non-GUI version offers the simplest operations and code, making it easier to understand. The GUI version supports more complex operations, providing a more advanced and user-friendly experience.

Due to my limited capabilities, the code may have some imperfections. I warmly welcome everyone to share their suggestions and contribute to the project. For more details, please see the Contribution. Thank you for your understanding!

---
## 2. Function

**VisualStructure** uses Python's `os` library to retrieve directory and file information, employing `├──`, `│`, and `└──` to represent branch relationships. The front-end is built with the `wxPython` library, ensuring an exceptionally lightweight experience. Users only need to input the path of the folder for which they want to generate the structure diagram and the output file path.

All folders end with a `/`, and all files are labeled with their extensions, ensuring clear differentiation between directories and files.

---
# 3. Required environment

Python should be at least 3.8.

All GUI-version files require `wxPython`:
```bash
pip install wxPython
```

---
## 4. Example

Using [BarcodeMaster](https://github.com/SomeB1oody/BarcodeMaster) as an example:
![VS_example](https://github.com/user-attachments/assets/9db1d30a-e20e-4463-b0c8-386fffcac01b)

---

## 5. Contribution

Contributions are welcome! Follow these steps:
 - 1. Fork project.
 - 2. Create branch:
 ```bash
 git checkout -b feature-name
```
- 3. Submit changes:
```bash
git commit -m "Explain changes"
```
- 4. Push branch:
```bash
git push orgin feature-name
```
- 5. Submit Pull Request.

---
## 6. License

This project uses [MIT LICENSE](https://github.com/SomeB1oody/VisualStructure/blob/main/LICENSE).

---
## 7. Contact information

- Email: stanyin64@gmail.com
- GitHub: [@SomeB1ooody](https://github.com/SomeB1oody)
