from transliterate import translit


class MyStr:
    def __init__(self, val):
        self.value = val

    def get_str(self):
        return self.value

class BaseDecorator:
    def __init__(self, Source):
        self.wrappee = Source

    def get_str(self):
        return self.wrappee.get_str()

class LowerStr(BaseDecorator):
    def get_str(self):
        return super().get_str().lower()


class ReplaceSpaceStr(BaseDecorator):
    def get_str(self):
        return '_'.join(super().get_str().split())


class TranslitStr(BaseDecorator):
    def get_str(self):
        return translit(super().get_str(), 'ru')


if __name__ == '__main__':
    string = input('Введите строку')
    my_str = MyStr(string)
    print(LowerStr(my_str).get_str())
    print(ReplaceSpaceStr(my_str).get_str())
    print(TranslitStr(my_str).get_str())