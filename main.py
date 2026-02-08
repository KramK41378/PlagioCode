import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt6 import uic
from get_list_from_py import read_py_file_to_list, read_file_as_list
from algorithms import compare_simple_alg, compare_strings, compare_binary, compare_without_spaces
from lm import generate_code


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("design.ui", self)

        self.setWindowTitle("PlagioCode")

        self.setWindowIcon(QIcon("img.png"))

        self.pushButton.clicked.connect(self.select_file)
        self.comboBox.currentTextChanged.connect(self.on_combo_changed)
        self.pushButton_2.clicked.connect(self.select_file1)
        self.pushButton_3.clicked.connect(self.compare_codes)

        self.combo_box_text = self.comboBox.currentText()
        self.selected_file_path_1 = None
        self.selected_file_path_2 = None

    def on_combo_changed(self):
        self.combo_box_text = self.comboBox.currentText()

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите Python-файл",
            "",
            "Python файлы (*.py)"
        )

        if file_path:
            self.selected_file_path_1 = file_path
            self.label_1.setText(f"Выбран файл:\n{file_path}")
        else:
            self.label_1.setText("Файл не выбран")

    def select_file1(self):
        if self.combo_box_text == "Выбрать файл .py для сверки":
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Выберите Python-файл",
                "",
                "Python файлы (*.py)"
            )
        else:
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Выберите Python-файл",
                "",
                "Python файлы (*.txt)")

        if file_path:
            self.selected_file_path_2 = file_path
            self.label_2.setText(f"Выбран файл:\n{file_path}")
        else:
            self.label_2.setText("Файл не выбран")

    def compare_codes(self):
        if self.selected_file_path_1 and self.selected_file_path_2:
            if self.combo_box_text == "Выбрать файл .py для сверки":
                lst1 = []
                lst2 = []
                try:
                    lst1 = read_py_file_to_list(self.selected_file_path_1)
                    lst2 = read_py_file_to_list(self.selected_file_path_2)
                except Exception:
                    self.label_3.setText(f"Ошибка чтения файлов(проверьте существование файлов)")
                percent = max(compare_strings(lst1, lst2), compare_binary(lst1, lst2), compare_simple_alg(lst1, lst2),
                              compare_without_spaces(lst1, lst2))
                if lst1:
                    self.label_3.setText(f"Файлы прочитаны, они схожи на {percent} %")
            else:
                lst1 = []
                prompt = []
                try:
                    lst1 = read_py_file_to_list(self.selected_file_path_1)
                    prompt = read_file_as_list(self.selected_file_path_2)
                except Exception:
                    self.label_3.setText(f"Ошибка чтения файлов(проверьте существование файлов)")
                code = generate_code(prompt)
                percent = max(compare_strings(lst1, code), compare_binary(lst1, code), compare_simple_alg(lst1, code),
                              compare_without_spaces(lst1, code))
                if lst1:
                    self.label_3.setText(f"Коды схожи на {percent} %")
        else:
            self.label_3.setText("Файлы не выбраны")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
