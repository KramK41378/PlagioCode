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


def read_file_as_list(full_path):
    try:
        with open(full_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Ошибка: файл не найден по пути '{full_path}'.")
        return []
    except PermissionError:
        print(f"Ошибка: нет прав на чтение файла '{full_path}'.")
        return []
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось декодировать файл '{full_path}' как UTF-8.")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при чтении файла: {e}")
        return []


if __name__ == "__main__":
    print(read_py_file_to_list("algorithms.py"))
    print(read_file_as_list("tz.txt"))
