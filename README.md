# Reviews
## 1st review
Идея проекта - сайт для построения графов с возможностью интерактивного запуска алгоритмов (вроде поиска в ширину) на них.  
Пока реализованно:
1. Датабаза SQLite с графами (Пока возможность добавлять графы только через терминал)
1. Страницы, доступные по ссылкам // , /graph/, /graph/1/, /graph/2/ ... при числе болшем чем колличество грфов в датабазе (пока их 3) выводится ошибка 404. 
1. На стрницах /graph/numer/  видны кнопки добавления новых вершин (они пока не работают) и изображение графа.
"Нестндартные" модули -- django, matplotlib, networkx, pillow (Интструкция по установке ниже и запуску).  
Пример того что вы должны увидеть:
![](https://github.com/Falier77777/test_lfs2/blob/master/Снимок%20экрана%202020-05-10%20в%2013.08.48.png)
# About ProGraph
Website created to make interaction with graphs easier.
ProGraph helps visualize graph and applies a lot of algorithms.

## 2nd review
1. Теперь можно добавлять новые вершины к графу
1. Добавленны некоторые тесты

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
