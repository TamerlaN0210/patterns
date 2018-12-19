import abc


class MyApp:
    def __init__(self, open_file_class, keep_data_class, filter_class, print_data_class):
        self.file = open_file_class
        self.data = keep_data_class
        self.filter = filter_class
        self.printer = print_data_class

    def run(self):
        self.data.keep_data(self.file.get_file_stream())
        self.printer.show(self.filter.filtrate(self.data.get_data()))
        self.file.close_file_stream()


class File(abc.ABC):

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def get_file_stream(self):
        pass

    @abc.abstractmethod
    def close_file_stream(self):
        pass


class OpenTextFile(File):

    def __init__(self):
        super().__init__()
        print('Введите путь до файла: ')
        self.path = input()
        self.file_stream = open(self.path)

    def get_file_stream(self):
        return self.file_stream

    def close_file_stream(self):
        self.file_stream.close()


class Keeper(abc.ABC):
    @abc.abstractmethod
    def keep_data(self, file_stream):
        pass

    @abc.abstractmethod
    def get_data(self):
        pass


class Keep100(Keeper):
    def __init__(self):
        super().__init__()
        self.data_array = list()

    def keep_data(self, file_stream):
        self.data_array.clear()
        for i in range(0, 100):
            try:
                self.data_array.append(int(file_stream.readline()))
            except Exception:
                print('Строку №', i, ' нельзя преобразовать к int')

    def get_data(self):
        return self.data_array


class Keep50(Keeper):
    def __init__(self):
        super().__init__()
        self.data_array = list()

    def keep_data(self, file_stream):
        self.data_array.clear()
        for i in range(0, 50):
            try:
                self.data_array.append(int(file_stream.readline()))
            except Exception:
                print('Строку №', i, ' нельзя преобразовать к int')

    def get_data(self):
        return self.data_array



class Filter(abc.ABC):
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def filtrate(self, numbers):
        pass


class FilterGreaterThan10(Filter):
    def __init__(self):
        super().__init__()

    def filtrate(self, numbers: list) -> list:
        filt_list = list()
        for i in range(0, len(numbers)):
            if numbers[i] > 10: filt_list.append(numbers[i])
        return filt_list


class FilterGreaterThan50(Filter):
    def __init__(self):
        super().__init__()

    def filtrate(self, numbers: list) -> list:
        filt_list = list()
        for i in range(0, len(numbers)):
            if numbers[i] > 50: filt_list.append(numbers[i])
        return filt_list


class DataOutput(abc.ABC):
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def show(self, numbers):
        pass


class ConsoleOutput(DataOutput):
    def __init__(self):
        super().__init__()

    def show(self, numbers: list):
        for i in range(0, len(numbers)):
            print(numbers[i])


class FileOutput(DataOutput):
    def __init__(self):
        super().__init__()

    def show(self, numbers: list):
        file = open('output.txt', 'w')
        for i in range(0, len(numbers)):
            temp = ''.join((str(numbers[i]), '\n'))
            file.write(temp)
        file.close()


if __name__ == '__main__':

    MyApp(OpenTextFile(), Keep50(), FilterGreaterThan10(), FileOutput()).run()



