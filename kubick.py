# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import matplotlib.pyplot as plt
import random
ones=0
twos=0
threes=0
fours=0
fives=0
sixs=0
counter=1
a=0
counters=[]
for i in range(1000):
    prev_a=a
    a=random.randint(1, 6)
    if a==1:
        ones+=1
    elif a==2:
        twos+=1
    elif a==3:
        threes+=1
    elif a==4:
        fours+=1
    elif a==5:
        fives+=1
    else:
        sixs+=1
    if prev_a==a:
        counter+=1
    else:
        counters.append(counter)
        counter=0
max_sim=0
for i in range(len(counters)):
    if counters[i]>max_sim:
        max_sim=counters[i]
values=[ones, twos, threes, fours, fives, sixs, max_sim]
categories=["единицы", "двойки", "тройки", "четвёрки", "пятёрки", "шестёрки", "подряд идущие"]
plt.bar(categories, values, color="green")
plt.title("1000 бросков")
plt.show()
