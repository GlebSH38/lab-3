import os


class TextFile:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            return f.read()


class BinaryFile:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'rb') as f:
            return f.read()


class FileFactory:
    TEXT_EXT = {'.txt', '.md', '.log', '.py'}
    BINARY_EXT = {'.jpg', '.png', '.pdf', '.bin'}

    @staticmethod
    def create(path):
        ext = os.path.splitext(path)[1].lower()
        if ext in FileFactory.TEXT_EXT:
            return TextFile(path)
        if ext in FileFactory.BINARY_EXT:
            return BinaryFile(path)
        raise ValueError(f'Неизвестный тип файла: {ext}')
