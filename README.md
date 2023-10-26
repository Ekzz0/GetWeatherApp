## Description
Задачи, которые можно решить:
1. Определить погоду (по координатам)
2. Определить погоду (по городу)
3. Определить погоду (по текущему местоположению)
4. Посмотреть историю запросов (последние n штук)
5. Очистить историю запросов
6. Завершить работу приложения

## План реализации
1) Информация о погоде по конкретному городу будет получаться по запросу библиотеки [requests](https://requests.readthedocs.io/en/latest/user/quickstart/), используя [OpenWeatherMap API](https://openweathermap.org/current). Погода по кординатам будет получена с помощью запроса из [requests](https://requests.readthedocs.io/en/latest/user/quickstart/) в [Geocoding API](https://openweathermap.org/api/geocoding-api)
2) Текущее месторасположение будет определяться по запросу библиотеки [requests](https://requests.readthedocs.io/en/latest/user/quickstart/) на сайт [ipinfo](https://ipinfo.io/).
3) История результатов запросов будет храниться в json-файле. 
4) Реализована простая консольная программа с выбором действий по пунктам.

## Установка приложения:
1. Установить интерпретатор python версии 3.11 (или выше)
2. Установить используемые модули в ваше окружение командой `pip install -r requirements.txt`
3. Для запуска приложения ввести команду `python main.py` в консоли из папки, в которой находится файл main.py

## Пример работы программы:
Главное меню с возможностью выбора следующего действия:
```
ГЛАВНОЕ МЕНЮ:

1: Определить погоду (по координатам)
2: Определить погоду (по городу)
3: Определить погоду (по текущему местоположению)
4: Посмотреть историю запросов (последние n штук)
5: Очистить историю запросов
6: Завершить работу приложения

Выберите действие (введите цифру):
```
Определим погоду по названию города (выберем пункт 2):
```
ОПРЕДЕЛИТЬ ТЕКУЩУЮ ПОГОДУ (ПО ГОРОДУ):

1: Ввести название города             
2: Назад                              
3: Завершить работу приложения        
   
Выберите действие (введите цифру):
```
Введём название города (выберем пункт 1).
```
Введите название города: Спб
```
Получим отчет по текущей погоде для города "Спб" (Санкт-Петербург):
```
Текущее время: 2023-10-20 19:40:45  
Название города: Спб                         
Погодные условия: пасмурно                   
Текущая температура: 2.84 градусов по цельсию
Ощущается как: -0.09 градусов по цельсию     
Скорость ветра: 3 м/с                        
         
1: Назад в главное меню                      
2: Завершить работу приложения               
 
Выберите действие (введите цифру):
```
Видим, что в последнем меню имеется возможность вернуться назад в главное меню и завершить работу программы.