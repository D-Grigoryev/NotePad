import classes.filehandler as file


class Note:
    def __init__(self):
        """Модель заметки
        name_note переменная в которой хранится название заметки
        content переменная в которой содержится содержание заметки
        self.note_list список в котором хранятся все созданные заметки
        """
        self.name_note = None
        self.content = None
        self.note = {}
        self.note_list = []

    def create_a_note(self):
        """Создает новую заметку"""
        self.name_note = input("Введите название заметки: ")
        self.content = input("Введите содержание заметки: ")
        self.note = {self.name_note: self.content}
        self.note_list.append(self.note)

    def show_list_of_notes(self):
        """Выводит список всех заметок"""
        for i in range(len(self.note_list)):
            print(f"Заметка №{i + 1}: название заметки: ", end=" ")
            print(*dict(self.note_list[i]).keys())

    def show_of_note(self, num):
        """Показывает содержание заметки"""
        try:
            print(*dict(self.note_list[num - 1]).values(), end=" ")
        except IndexError:
            print("Вы ввели неверное значение")

    def edit_note(self):
        """Редактирует содержание заметки"""

        try:
            num = int(input("Введите номер заметки: "))
            new_value = dict(self.note_list[num - 1])
            content = input("Введите новое содержание: ")
            new_value[str(*dict(self.note_list[num - 1]).keys())] = content
            self.note_list[num - 1] = new_value
            print("Заметка изменена")
        except IndexError:
            print("Вы ввели неверный номер заметки")

    def del_note(self, num):
        """Удаляет заметку"""
        del self.note_list[num - 1]

    def del_all_notes(self):
        """Удаляет все заметки"""
        self.note_list.clear()

    def save_changes(self):
        """Сохраняет изменения в файл"""
        file.save_info(self.note_list)

    def load_changes(self):
        """Загружает изменения из файла"""
        content = file.read_info()
        for el in content:
            if el in self.note_list:
                print("Эта заметка уже загружена")
            else:
                self.note_list.append(el)
        print(self.note_list)

    def load_changes_date(self, file_name):
        """Загружает данные по дате поиска"""
        content = file.read_info_date(file_name)
        for el in content:
            if el in self.note_list:
                print("Эта заметка уже загружена")
            else:
                self.note_list.append(el)
        print(self.note_list)
