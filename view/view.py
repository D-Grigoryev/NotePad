

import classes.note as note
import filters.date as date_filter


class View:
    """Реализует интерфейс работы с заметками"""

    def __init__(self):
        self.menu = {
            1: "-Cоздать заметку",
            2: "-Посмотреть список заметок",
            3: "-Посмотреть содержание заметки",
            4: "-Изменить заметку",
            5: "-Удалить заметку",
            6: "-Удалить все заметки",
            7: "-Показать меню",
            8: "-Сохранить изменения",
            9: "-Загрузить последнее сохранение",
            10: "-Поиск заметок по дате создания",
            0: "-Завершить работу"
        }
        self.flag = True
        self.note = note.Note()
        self.date_filter = date_filter.DateFiler()

    def show_menu(self):
        """Показывает меню для работы с заметками"""
        print("Добро пожаловать в приложение 'Заметки'\n")
        for k, v in self.menu.items():
            print(k, v)

    def work_menu(self):
        """Реализует работу с меню"""
        while self.flag:
            while True:
                try:
                    choice = int(input("\nВыберите пункт меню: "))
                    break
                except ValueError:
                    print("Вы ввели не число. Попробуйте снова: ")
            if choice in self.menu.keys():
                print(f"Вы выбрали пункт -  {choice}")
                if choice == 1:
                    self.note.create_a_note()
                elif choice == 2:
                    print("Список имеющихся заметок:")
                    self.note.show_list_of_notes()
                elif choice == 3:
                    print("Просмотр содержания интересующей заметки:")
                    self.note.show_of_note(int(input("Введите номер заметки: ")))
                elif choice == 4:
                    print("Редактирование заметки")
                    self.note.edit_note()
                elif choice == 5:
                    print("Удаление заметки")
                    self.note.del_note(int(input("Введите номер заметки: ")))
                    print("Заметка удалена")
                elif choice == 6:
                    print("Удаление всех заметок")
                    self.note.del_all_notes()
                    print("Заметки удалены")
                elif choice == 7:
                    self.show_menu()
                elif choice == 8:
                    print("Сохранение изменений")
                    self.note.save_changes()
                    print("Изменения сохранены")
                elif choice == 9:
                    print("Загрузка из файла")
                    self.note.load_changes()
                    print("Заметки загружены")
                elif choice == 10:
                    print("Поиск заметок по дате создания")
                    file_name = self.date_filter.serch_date()
                    self.note.load_changes_date(file_name)
                elif choice == 0:
                    self.flag = False
                    print("Завершение работы программы")
                    print("Работа программы завершена")
            else:
                print("Вы выбрали нвереный пункт")

