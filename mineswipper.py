# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
#
import matplotlib.pyplot as plt
from random import randint
m=[[1 if (i%2==j%2) else 1 for j in range(10)] for i in range(10)]
z=[[0 for _ in range(10)] for _ in range(10)]
fig = plt.figure(figsize=(10,6))
ax = plt.subplot(1,2,1)
plt.imshow(m, cmap="hot")
for _ in range(15):
    while True:
        x=randint(0, 9)
        y=randint(0, 9)
        if m[x][y]==1:
            m[x][y]=-1
            z[y][x]=10
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0<=x+dx<10 and 0<=y+dy<10 and (dx!=0 or dy!=0) and z[y+dy][x+dx]!=10:
                        z[y+dy][x+dx]+=1
                        cil=plt.Circle((x,y),0.35,color="#c41414")
            ax.add_patch(cil)
            break
for row in z:
    print(row)
plt.xticks(range(10),labels=[f"{i}" for i in range(1,11)])
plt.yticks(range(10),labels=[f"{i}" for i in range(10,0,-1)])
plt.xticks([i+0.5 for i in range(10)])
plt.yticks([i+0.5 for i in range(10)])
plt.grid(color="white")
ax = plt.subplot(1, 2, 2)
plt.imshow(z, cmap="OrRd")
for i in range(10):
    for j in range(10):
        plt.text(j, i, "M" if z[i][j] == 10 else z[i][j], ha="center", va="center")

plt.xticks(range(10), labels=[f"{i}" for i in range(1,11)])
plt.yticks(range(10), labels=[f"{i}" for i in range(10,0,-1)])
plt.xticks([i+0.5 for i in range(10)])
plt.yticks([i+0.5 for i in range(10)])
plt.grid(color="black", linestyle="--", linewidth=1.5)
plt.show()
