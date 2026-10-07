from pathlib import Path
import shutil


class FileManager:
    """Класс для удобной работы с файлами."""

    def __init__(self, path, encoding='utf-8'):
        """
        :param path: путь к файлу (str или Path)
        :param encoding: кодировка для текстовых операций
        """
        self.path = Path(path)
        self.encoding = encoding

    # Проверки

    def exists(self):
        """Существует ли файл."""
        return self.path.exists()

    def is_file(self):
        """Является ли путь файлом."""
        return self.path.is_file()

    def is_dir(self):
        """Является ли путь директорией."""
        return self.path.is_dir()

    # Метаданные

    def name(self):
        """Имя файла без пути."""
        return self.path.name

    def extension(self):
        """Расширение файла."""
        return self.path.suffix

    # Чтение

    def read(self):
        """Прочитать весь файл как строку."""
        self._ensure_exists()
        return self.path.read_text(encoding=self.encoding)

    def read_lines(self):
        """Прочитать файл как список строк (без \\n)."""
        self._ensure_exists()
        with open(self.path, 'r', encoding=self.encoding) as f:
            return [line.rstrip('\n') for line in f]

    # Запись

    def write(self, content, mode='w'):
        """
        Записать строку в файл.
        :param mode: 'w' — перезапись, 'a' — добавление
        """
        self._ensure_parent()
        with open(self.path, mode, encoding=self.encoding) as f:
            f.write(content)
        return self

    # Операции с файлом

    def clear(self):
        """Очистить файл (сделать пустым)."""
        return self.write('')

    def copy_to(self, destination):
        """Скопировать файл в новое место."""
        self._ensure_exists()
        destination = Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(self.path, destination)
        return FileManager(destination, self.encoding)

    def move_to(self, destination):
        """Переместить файл в новое место."""
        self._ensure_exists()
        destination = Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(self.path), str(destination))
        self.path = destination
        return self

    def delete(self, missing_ok=True):
        """Удалить файл."""
        self.path.unlink(missing_ok=missing_ok)
        return self

    def rename(self, new_name):
        """Переименовать файл (в той же директории)."""
        new_path = self.path.with_name(new_name)
        self.path.rename(new_path)
        self.path = new_path
        return self

    # Вспомогательные

    def _ensure_exists(self):
        """Выбросить исключение, если файла нет."""
        if not self.exists():
            raise FileNotFoundError(f'Файл не найден: {self.path}')

    def _ensure_parent(self):
        """Создать родительскую директорию, если её нет."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
