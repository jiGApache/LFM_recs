# Общее описание

Целью реализации данного консольного приложения служит поиск похожих музыкальных исполнителей.
Информация об исполнителях взята с открытого датасета last.fm: https://www.kaggle.com/datasets/pcbreviglieri/lastfm-music-artist-scrobbles

В основе работы приложения лежит алгоритм item-item коллаборативной фильтрации, которая основана на сходстве между объектами рекомендаций. Сходство между объектами рассчитывается при помощи косинусного расстояния.

# Инструкция по запуску

Перед запуском программы необходимо иметь установленное средство контейнеризации приложений Docker.
Доступно здесь: https://docs.docker.com/get-docker/

### Шаги по запуску приложения:
- Загрузить исходные файлы с репозитория
- Перейти в корневую папку проекта
- Командой `docker build -t {название_образа} .` создать образ контейнера
- Командой `docker run -ti {название_образа}` запустить контейнер

# Пример работы приложения

На вход приложения следует подать название музыкальной группы, для которой необходимо найти похожие музыкальные группы.

Результатом работы приложения будет являться отсортированный список групп, согласно их коэффициенту схожести с поданной на вход группой.

```
Введите название группы (q - для выхода): Би-2 
Возможные результаты:
- Агата Кристи | (0.9300314370787105)
- Emf | (0.9282462583471244)
- Holdcut | (0.9282462583471244)
- Neneh Cherry | (0.9282462583471244)
- Hadise | (0.9242156884973113)
- Girls Can't Catch | (0.9158822142460258)
- Kalomoira | (0.9056130584994051)
- Gravity Kills | (0.8955741831996594)
- Erreway | (0.890698003106487)
- Endraum | (0.8883024240886948)
- Alizee | (0.8746208468704588)
```