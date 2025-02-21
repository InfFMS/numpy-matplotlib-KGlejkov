# Описание задачи:
# Робот начинает своё движение из точки (0,0) на координатной плоскости. Его маршрут задаётся массивом из 100 случайных значений, где:1 — движение вверх.2 — движение вниз.3 — движение вправо.4 — движение влево.
# Ваша задача:
# Сымитировать маршрут робота, используя случайные числа.
# Найти конечное положение робота.
# Построить путь робота на графике (соединяя все пройденные точки).
# Подсчитать, сколько шагов робот сделал в каждую сторону.
# Определить расстояние от начальной точки до конечной.
from random import randint
import matplotlib.pyplot as plt
import numpy as np
x, y = 0, 0
v1, v2, v3, v4 = 0, 0, 0, 0
fig = plt.figure(figsize=(6, 6))
ax = plt.subplot(1, 1, 1)
path_x = [x]
path_y = [y]
for i in range(100):
    v = randint(1, 4)
    if v == 1:
        y += 1
        v1 += 1
    elif v == 2:
        y -= 1
        v2 += 1
    elif v == 3:
        x += 1
        v3 += 1
    else:
        x -= 1
        v4 += 1
    path_x.append(x)
    path_y.append(y)
ax.plot(path_x, path_y, color="blue")
plt.text(0, 0, "H", fontsize=12, ha='right')
plt.text(x, y, "К", fontsize=12, ha='right')
print("Конечное положение робота:")
print("\tПо х:", x)
print("\tПо у:", y)
print("Робот сделал следующее количество шагов:")
print("\tВверх:", v1)
print("\tВниз:", v2)
print("\tВправо:", v3)
print("\tВлево:", v4)
print("Расстояние от начальной точки до конечной:", (x ** 2 + y ** 2) ** 0.5)
ax.set_title("Движение робота")
ax.set_xlabel("Ось X")
ax.set_ylabel("Ось Y")
ax.axhline(0, color='black',linewidth=0.5, ls='--')
ax.axvline(0, color='black',linewidth=0.5, ls='--')
ax.grid(color='gray', linestyle='--', linewidth=0.5)
plt.axis('equal')
plt.show()
