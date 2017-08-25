Демо версия: http://54.93.235.17/

### Эксперименты
Первоночальная идея была использовать w2v embeddings на корпусе. Обучить свою w2v модель на имеющихся данных<br>

метрика: F1 на 30000 примеров<br>

|Модель|counter|w2v_big|w2v_own|all w2v|tf-idf|
| --- | --- | --- | --- | --- | --- |
| RF | 0.55 | 0.39 | 0.39 | 0.41 | 0.52 |
| Log-reg | 0.46 | 0.40 | 0.07 | 0.40 | 0.46 |
| Bayes | 0.63 | 0.47 | 0.48 | 0.50 | 0.62 |
| BF neural net | 0 | 0 | 0 | 0 | 0 |

Интересно было бы посмотреть на результаты на полной конкатенации. Не тестировалось в виду сложности вычислений и необходимости применения более сложного стека.<br>

Также можно было бы попробовать применить LSTM (https://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/)<br>
CNN (https://arxiv.org/abs/1408.5882)<br>

и character level

также заменить w2v на char2vec или doc2vec.

|FastText|30000|1000000|
| --- | --- | --- |
|correct	|5999 (3235)|	122582 (199999)|
|acuuracy	|0.54|0.61|
|precision	|0.59|0.58|
|recall	|0.07|0.77|
|f1|0.12|0.66|

Скорее всего из-за особенностей датасета и русского языка, а также того, что fasttext char based, лемминг, стемминг и предобработка строк ухудшали метрики, поэтому от предобработки было решено отказаться.

[fasttext](https://github.com/facebookresearch/fastText)
1. [формирование эмбеддингов](https://arxiv.org/abs/1607.04606)<br>
2. [классификатор](https://arxiv.org/abs/1607.01759)<br>

### Логика работы:
Веб часть реализована с использованием Flask. Клиентская чась на Angular 1.<br>

В качестве ML части используется биндинг [python fasttexts](https://pypi.python.org/pypi/fasttext) на python.<br>

Общая вероятность считается как среднее межжду всеми предсказаниями для каждого из классов.<br>

### Установка:
#### LOCAL
```
git clone https://github.com/nsmalimov/gender_detector
cd gender_detector
pip3 install requirements.txt
python3 run.py
```
#### REMOTE
https://habrahabr.ru/post/267097/
