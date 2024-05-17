# Koshelek.ru-Test
Отборочное тестовое задание "Кошелёк.ру". Настоящий проект содержит автотесты на языке Python,исполняющие проверки формы регистрации сервиса по *негативным сценариям. Тестируемый сервис использует ShadowRoot корни и динамичные,сложноструктированные селекторы.

1. Объект тестирования - регистрационная форма веб-ресурса [https://koshelek.ru]
2. Фреймворк тестирования - Pytest на базе библиотеки веб-тестирования Selenium WebDriver (драйвер Firefox geckodriver V 0.34.0-win64)
3. Интерпретатор - VS code.
4. Файл elements.py содержит классы с локаторами веб-элементов. Тесты обращаются к ним по импорту
5. Файл values.py содержит классы с тестовыми данными для текстовых полей. Тесты обращаются к ним по импорту
6. Папка tests содержит файл с тестами - regpage_test.py (21 тест всего)
7. Некоторые строки тестов подкреплены пояснительными комментариями
8. Файл requirements.txt содержит список библиотек,необходимых для работы тестов. Установить - pip install {библиотека}
9. В настройках драйвера предусмотрена строка -headless. Раскомментируйте строку,что бы запускать тесты в фоновом режиме,без визуального отображения интерфейса браузера.
10. Среднее время прогона: 30 сек.

Запуск : 
1. python -m pytest tests\regpage_test.py {консоль} или кнопкой запуска файла # Если путь к драйверу задан заранее в переменных среды PATH
2. python -m pytest --driver Firefox --driver-path C:{driver path}\geckodriver.exe tests\regpage_test.py # Запуск через консоль с вручной передачей пути к драйверу. 
