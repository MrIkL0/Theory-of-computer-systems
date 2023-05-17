import os
import time

while True:
    # Перелічуємо файли в каталозі "data"
    files = os.listdir("data")

    # Якщо в каталозі є файли, то виводимо їх назви та вміст
    if len(files) > 0:
        for file in files:
            with open(os.path.join("data", file), "r") as f:
                content = f.read()
            print(f"Назва файлу: {file}\nResult: {content}\n")

    # Затримка на 10 секунд перед наступною перевіркою
    time.sleep(10)