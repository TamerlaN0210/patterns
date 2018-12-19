import abc


class EventManager:
    def __init__(self):
        self.listeners = list()

    def subscribe(self, listener):
        if isinstance(listener, list) or isinstance(listener, tuple):
            for elem in listener:
                self.listeners.append(elem)
        if isinstance(listener, Listeners):
            self.listeners.append(listener)

    def unsubscribe(self, listener):
        self.listeners.remove(listener)

    def notify(self, number):
        for elem in self.listeners:
            elem.update(number)


class MyNumber:
    def __init__(self):
        self.events = EventManager()
        self.number = 0

    def input(self):
        print('Введите число')
        self.number = int(input())
        self.events.notify(number=self.number)


class Listeners(abc.ABC):
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def update(self, number):
        pass


class NumMod2(Listeners):
    def update(self, number):
        if number % 2 == 0:
            print('Число четное')
        else:
            print('Число нечетное')


class NumMod3(Listeners):
    def update(self, number):
        if number % 3 == 0:
            print('Число делится на 3 без остатка')


class NumCompareTo0(Listeners):
    def update(self, number):
        if number > 0:
            print('Число больше нуля')
        elif number < 0:
            print('Число меньше нуля')
        else:
            pass


class SimpleNum(Listeners):

    def __init__(self):
        super().__init__()
        self.is_simple = True

    def update(self, number):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    self.is_simple = False
                    break
            if self.is_simple:
                print('Простое число')
        else:
            self.is_simple = False


if __name__ == '__main__':
    my_number = MyNumber()
    my_number.events.subscribe([NumMod2(), NumMod3(), NumCompareTo0(), SimpleNum()])
    my_number.input()
