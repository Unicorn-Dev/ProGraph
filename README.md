# review
## 1st review
Идея проекта - сайт для построения графов с возможностью интерактивного запуска алгоритмов на них.  
Пока реализованно:
1. Датабаза SQLite с графами (Пока возможность добавлять графы только через терминал)
1. Страницы, доступные по ссылкам // , /graph/, /graph/1/, /graph/2/ ... при числе болшем чем колличество грфов в датабазе (пока их 3) выводится ошибка 404. 
1. На стрницах /graph/numer/  видны кнопки добавления новых вершин (они пока не работают) и картинка (пока это просто картинка, но в будущем это будет картинка графа)

# About ProGraph
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
