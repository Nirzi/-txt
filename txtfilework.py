class TxtFileHandler:
    """
    Класс для работы с TXT файлами.

    Методы:
        read_file(filepath: str) -> str:
            Считывает содержимое файла в строку.

        write_file(filepath: str, *data: str) -> None:
            Записывает данные в файл, перезаписывая его содержимое.

        append_file(filepath: str, *data: str) -> None:
            Добавляет данные в конец файла.
    """

    def read_file(self, filepath: str) -> str:
        """
        Читает содержимое файла и возвращает его в виде строки.
        Если файл не найден, метод возвращает пустую строку.
        При любой ошибке также возвращаем пустую строку, и выводим сообщение об ошибке.

        :param filepath: Путь к файлу, из которого читаем данные.
        :return: Содержимое файла в виде строки или "" в случае ошибки.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Ошибка при чтении файла {filepath}: {e}")
            return ""

    def write_file(self, filepath: str, *data: str) -> None:
        """
        Записывает переданные строки в файл, перезаписывая его.
        Если файл существует, он будет перезаписан.

        :param filepath: Путь к файлу, в который записываем данные.
        :param data: Произвольное количество строк для записи.
        :return: None
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                for item in data:
                    file.write(item)
        except Exception as e:
            print(f"Ошибка при записи в файл {filepath}: {e}")

    def append_file(self, filepath: str, *data: str) -> None:
        """
        Добавляет переданные строки в конец файла.
        Если файл не существует, он будет создан.

        :param filepath: Путь к файлу, в который добавляем данные.
        :param data: Произвольное количество строк для добавления.
        :return: None
        """
        try:
            with open(filepath, 'a', encoding='utf-8') as file:
                for item in data:
                    file.write(item)
        except Exception as e:
            print(f"Ошибка при добавлении в файл {filepath}: {e}")


if __name__ == "__main__":
    # Пример использования
    handler = TxtFileHandler()

    # 1. Запись в файл (перезапишет или создаст, если файла нет)
    handler.write_file("my_file.txt", "This is a test string.\n")

    # 2. Добавление в файл (добавит в конец)
    handler.append_file("my_file.txt", "This is another string.\n")

    # 3. Чтение из файла
    content = handler.read_file("my_file.txt")
    print("Содержимое файла:")
    print(content)
