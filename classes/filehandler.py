
import json
import datetime

date = datetime.date.today().isoformat()
path = "data/"
filename = path+date+".json"

def save_info(content):
    """Сохраняет в файл информацию"""
    try:
        with open(filename, 'w') as file:
            json.dump(content, file)
    except FileNotFoundError:
        print("Файл не найден")

def read_info():
    """Читает информацию из файла"""
    try:
        with open(filename) as file:
            lines = json.load(file)
        return lines
    except FileNotFoundError:
        print("Файл не найден")

def read_info_date(name):
    """Читает информацию из файла"""
    try:
        with open(path+name) as file:
            lines = json.load(file)
            print("Данные загружены")
        return lines
    except FileNotFoundError:
        print("Файл не найден")
