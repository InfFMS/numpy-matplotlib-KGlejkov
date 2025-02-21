# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x = np.array([[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0] ])
plt.imshow(x, cmap="Blues")
bukovi = ["A", "B", "C", "D", "E", "F", "G", "H"]
plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0, -1)])
plt.xticks(range(8), labels=[f"{bukovi[i]}" for i in range(8)])
x1 = int(input("Королева по x: ")) - 1
y1 = 8 - int(input("Королева y: "))
for i in range(0, 8):
    point = plt.Circle((i, y1), 0.25, edgecolor="black", facecolor="green")
    ax.add_patch(point)
    point = plt.Circle((x1, i), 0.25, edgecolor="black", facecolor="green")
    ax.add_patch(point)
x = x1
y = y1
while y < 8 and x < 8:
    point = plt.Circle((x, y), 0.25, edgecolor="black", facecolor="green")
    ax.add_patch(point)
    x += 1
    y += 1
x = x1
y = y1
while y < 8 and x > -1:
    print(x, y)
    point = plt.Circle((x, y), 0.25, edgecolor="black", facecolor="green")
    ax.add_patch(point)
    x -= 1
    y += 1
x = x1
y = y1
while y > -1 and x < 8:
    print(x, y)
    point = plt.Circle((x, y), 0.25, edgecolor="black", facecolor="green")
    ax.add_patch(point)
    x += 1
    y -= 1
x = x1
y = y1
while y > -1 and x > -1:
    print(x, y)
    point = plt.Circle((x, y), 0.25, edgecolor="black", facecolor="green")
    ax.add_patch(point)
    x -= 1
    y -= 1
ferz = plt.Circle((x1, y1), 0.35, edgecolor="black", facecolor="yellow")
ax.add_patch(ferz)
plt.show()
L
