# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import numpy as np
import matplotlib.pyplot as plt
from random import randint
temperatures = [randint(-10, 35) for _ in range(365)]
average_temp = np.mean(temperatures)
days_above_25 = sum(temp > 25 for temp in temperatures)
longest_cold_streak = 0
current_streak = 0
end_of_streak = 0
for i, temp in enumerate(temperatures):
    if temp < 0:
        current_streak += 1
    else:
        if current_streak > longest_cold_streak:
            longest_cold_streak = current_streak
            end_of_streak = i
        current_streak = 0
if current_streak > longest_cold_streak:
    longest_cold_streak = current_streak
    end_of_streak = 365
start_of_streak = end_of_streak - longest_cold_streak + 1
print("Средняя температура за год:", average_temp)
print("Количество дней с температурой выше 25:", days_above_25)
print("Самая длинная последовательность дней, когда температура была ниже 0:")
print("\tДлина этой последовательности:", longest_cold_streak)
print("\tНомера крайних дней:", start_of_streak, end_of_streak)
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
axs[0].plot(temperatures, color="blue", label="Температура")
axs[0].set_title("Температура по дням")
axs[0].set_xlabel("День года")
axs[0].set_ylabel("Температура (°C)")
axs[0].axhline(0, color="gray", linewidth=0.8, linestyle='--')
axs[0].legend()
axs[1].hist(temperatures, bins=np.arange(-10, 36, 1), color="#5da38f", edgecolor="black")
axs[1].set_title("Распределение температуры")
axs[1].set_xlabel("Температура (°C)")
axs[1].set_ylabel("Количество дней")
cold_days = [temp if temp < 0 else np.nan for temp in temperatures]
hot_days = [temp if temp > 25 else np.nan for temp in temperatures]
axs[2].plot(cold_days, color="blue", label="Холодные дни (< 0°C)", linestyle="None", marker="o")
axs[2].plot(hot_days, color="red", label="Жаркие дни (> 25°C)", linestyle="None", marker="o")
axs[2].plot(temperatures, color="gray", alpha=0.5, label="Температура")
axs[2].set_title("Температура с подсветкой холодных и жарких дней")
axs[2].set_xlabel("День года")
axs[2].set_ylabel("Температура (°C)")
axs[2].axhline(0, color="gray", linewidth=0.8, linestyle='--')
axs[2].legend()
plt.tight_layout()
plt.show()
