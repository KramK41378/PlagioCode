def read_py_file_to_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i][:-1]
        return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except PermissionError:
        raise PermissionError(f"Нет прав на чтение файла: {file_path}")
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла: {e}")


if __name__ == "__main__":
    print(read_py_file_to_list("algorithms.py"))