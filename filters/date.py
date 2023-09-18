import os


class DateFiler:
    """Реализует поиск по дате"""

    def __self__(self):
        self.year = None
        self.month = None
        self.day = None

    def serch_date(self):
        """Принимает значение даты, формирует строку и осуществляет поиск на соотвествие имени файла"""
        try:
            self.year = int(input("Введите год: "))
            self.month = input("Введите месяц в виде двузначного значения (например январь - 01: ")
            self.day = int(input("Введите день в виде двузначного значения (например понедельник - 01: "))
        except TypeError:
            print("Вы ввели неверное значение")

        file_name = f"{self.year}-{self.month}-{self.day}.json"
        print(file_name)
        folder = "data/"

        for element in os.scandir(folder):
            if element.is_file():
                if element.name == file_name:
                    print("Файл найден")
                    return file_name
                else:
                    print("Файл не найден")
