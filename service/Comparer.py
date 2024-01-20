import difflib

class Comparer:
    def __init__(self):
        # Дополнительные инициализации, если необходимо
        pass

    def compare_text_files(self, file1, file2):
        try:
            # Считываем содержимое файлов
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            # Используем difflib для сравнения строк
            differ = difflib.Differ()
            diff = list(differ.compare(lines1, lines2))

            # Возвращаем результат сравнения в виде строки
            return '\n'.join(diff)
        except Exception as e:
            # Обработка ошибок, например, если файлы не существуют или чтение не удалось
            return f'Ошибка при сравнении файлов: {str(e)}'