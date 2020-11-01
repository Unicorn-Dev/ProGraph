# About ProGraph
![](https://github.com/Unicorn-Dev/ProGraph/blob/master/img/ProGraph.jpg)
Website created to make interaction with graphs easier.
ProGraph helps visualize graph and applies a lot of algorithms.

# License

MIT License.

# Requirements

Client side:
1. HTML5 support of client side.

Server side:
1. requirements  from requirements.txt

# How to run

1. Download repository to local website folder. 

1. Change dirrectory to reposytory's dirrectory and run command in terminal:  
  1. Create a venv for this project if you want
  ```
  $ python3 -m venv env_name
  $ source env_name/bin/activate
  ```
  1. Install requirements
  ```
  $ pip3 install -r requirements.txt  
  ```
  1. run your local server
  ```
  $ python3 manage.py runserver
  ```
  After that you will see local-host url.  
  
(for Windows you should use python instead of python3)
  


# Supports & feedback

You can write on telegram to @AlexFreik or @cosdar.


# Project development
Идея проекта - сайт для построения графов с возможностью интерактивного запуска алгоритмов (вроде поиска в ширину) на них.  
Пока реализованно:
1. Датабаза SQLite с графами (Пока возможность добавлять графы только через терминал)
1. Страницы, доступные по ссылкам // , /graph/, /graph/1/, /graph/2/ ... при числе болшем чем колличество грфов в датабазе (пока их 3) выводится ошибка 404. 
1. Теперь можно добавлять новые вершины и ребра к графу, а так же удалять их
  1. Добавлена обработка "ошибок" если добавляемое ребро существует / не существует
1. Можно запускать DFS или BFS алгоритмы на связаных графах
1. У графов можно скопировать ссылку или номер, чтобы расшарить его 
1. Теперь в главном меню есть кнопки перехода к существующему графу по его id и создания нового графа
1. Добавленны некоторые тесты
  1. тестировать можно командами:
  ```
  $ python3 manage.py test graph
  $ python3 manage.py test main
  $ python3 manage.py test app_backend
  ```
1. Добавлена графика
