# Утилита для работы с конфигурационными файлами 

## Описание
Этот скрипт предназначен для работы с файлом конфигурации. Он позволяет читать, записывать и изменять настройки в файле конфигурации.

## Как запустить
Для запуска скрипта необходимо выполнить следующую команду в командной строке:
python main.py <action> <filepath> --param <param>
Где:
- action - действие, которое необходимо выполнить (read или write).
- filepath - путь к файлу конфигурации.
- param - параметр и значение для этого параметра в формате: key.subkey=value (только для действия Write).
## Содержание
- main.py - основной скрипт 
- config.json - файл над котором проводяться манипуляции 
- README.md - документация
### Функции main.py
- read_config(filepath): Функция для чтения файла конфигурации. Принимает путь к файлу и возвращает данные из него.
- write_config(filepath, config): Функция для записи конфигурации в файл. Принимает путь к файлу и данные для записи.
- update_config(config, param, value): Функция для изменения параметра в конфигурации. Принимает данные конфигурации, параметр и значение для установки.
## Примеры использования
- Откройте терминал или командную строку.
1. Чтение файла конфигурации:
```python
python main.py read config.json
```
вывод:
```python
{
   "server": {
      "host": "0.0.0.0",
      "port": "3000",
      "debug": "false",
      "": {
         "port": "3000"
      }
   },
   "database": {
      "type": "postgresql",
      "host": "localhost",
      "port": 5432,
      "username": "db_user",
      "password": "db_password",
      "database_name": "my_database"
   },
   "logging": {
      "level": "INFO",
      "file": "/var/log/myapp.log"
   },
   "api": {
      "key": "my_api_key",
      "endpoint": "https://api.example.com/v1/"
   },
   "email": {
      "smtp_server": "smtp.example.com",
      "smtp_port": 587,
      "username": "email_user",
      "password": "email_password",
      "from_email": "no-reply@example.com",
      "to_email": "admin@example.com"
   },
   "features": {
      "enable_feature_x": true,
      "enable_feature_y": false
   },
   "server.port": "3000"
}
```
2. Запись нового параметра в файл конфигурации:
```python
python main.py write config.json --param server.port=3000
```

## Используемые модули
```python
import argparse
import json
```
Модуль argparse в Python предназначен для обработки аргументов командной строки. Он позволяет создавать интуитивно понятные интерфейсы для работы с командами и опциями, что является важным аспектом при создании полноценных приложений.

JSON (JavaScript Object Notation) — это легковесный формат обмена данными, основанный на синтаксисе объектов JavaScript. Он используется для передачи данных между сервером и клиентом и обладает простой и читаемой структурой. JSON является языконезависимым, что позволяет его использовать в различных языках программирования, включая Python.
## Автор
[GitHub](https://github.com/Abakar0 'Абдулаев Абакар')
