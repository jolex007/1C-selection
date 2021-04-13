# Задание для отбора на КИС

### **Описание**

Этот проект позволяет выбрать оптимальную стратегию выбора курсов на КИС.

Главный файл проекта - [main.py](main.py)

Файл для работы с таблицей - [table_help.py](table_help.py)

### Ввод

Пример:
```bash
Choose courses to take (indexes):
51 52 53

Choose priority courses (indexes):
36 43 20

Print minimal count of courses per term:
3

Bachelor or undergraduate (print 0 or 1):
1
That is courses you need to take:
[2, 3, 5, 6, 7, 11, 12, 20, 31, 39, 40, 44, 47, 51, 52, 53, 62]
```

Пример таблицы для обработки лежит в папке [data](data/1C_courses.csv)

### **Запуск**

Чтобы запустить проект, нужно ввести в консоли
```bash
python3 main.py --timetable_path <path_to_timetable>
```

Пример:
```bash
python3 main.py --timetable_path ./data/1C_courses.csv
```

--------

## Зерцалов Алексей

Telegram - [@jolex007](https://t.me/jolex007)