Демо версия: http://54.93.235.17/

### Эксперименты
Первоночальная идея была использовать w2v embeddings на корпусе. Обучить свою w2v модель на имеющихся данных

### Логика работы:
Веб часть реализована с использованием Flask. Клиентская чась на Angular 1.<br>

В качестве ML части используется биндинг fasttext [python fasttexts](https://pypi.python.org/pypi/fasttext) на python.<br>

Общая вероятность считается как среднее межжду всеми предсказаниями для каждого из классов.<br>

### Установка:
project adapted for Python 3<br>

need ubuntu/linux/mac os

### LOCAL
```
git clone https://github.com/nsmalimov/gender_detector
cd gender_detector
pip3 install requirements.txt
python3 run.py
```
### REMOTE
https://habrahabr.ru/post/267097/
