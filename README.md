# Python lab 1
____
## Условие задачи:
### Задание 1.
Известно, что в CPython для `x = 5` и `y = 5` выполняется `id(x) == id(y)`. Найти максимальный диапазон целых чисел [-M, N], для которого это утверждение верно.
____
## Установка виртуального окружения и запуск
____
### 1. Клонируйте репозиторий
```bash
git clone https://github.com/Syntax-Error-Squad/int-optimization.git
cd int-optimization
```
### 2. Создайте виртуальное окружение
```bash
python -m venv venv
```
### 3. Активируйте виртуальное окружение
- **Windows CMD**
```bash
.\venv\Scripts\activate
```
- **Windows PowerShell**
```powershell
.\venv\Scripts\Activate.ps1
```
- **macOS/Linux**
```bash
source venv/bin/activate
```
После активации виртуального окружения в командной строке появится префикс venv.
### 4. Запустите программу
```bash
python task_1_int_optimization.py
```
Ожидаемый вывод:
```
[-5, 256]
```
____
### Зависимости проекта
Внешних зависимостей нет — используется только стандартная библиотека Python.
