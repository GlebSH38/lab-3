from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def sound(self):
        return 'Гав!'

    def move(self):
        return 'Бежит на четырёх лапах'


class Bird(Animal):
    def sound(self):
        return 'Чик-чирик!'

    def move(self):
        return 'Летит'
