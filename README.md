# RSV22_yaroslavl_serdce

### Прогнозирование риска развития сердечно-сосудистого заболевания пациента


Препроцессинг данных и генерация необходимых фичей происходит в `preprocessing.py`

В папке `models` обученные модели Catboost

В конфиге `config.py` задаётся список используемых каждой моделью переменных, а также пути к нужным директориям.

Для выбора оптимальных параметров максимизируем целевую метрику с помощью optuna (`optimization.py`)

**Для воспроизведения обучения и получения предсказания последовательно запустить ноутбук `LD22_yaroslavl_final_sol.ipynb`, предварительно прроверив наличие файлов с данными в директории `DATA_PATH` в конфиге**



