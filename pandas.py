""""

import pandas as pd

# 1. Загружаем данные (укажите правильный путь к вашему файлу)
# df = pd.read_csv('cars.csv')
# или для Excel: df = pd.read_excel('cars.xlsx')

# Для примера создадим искусственные данные, чтобы код работал:
data = {
    'марка': ['BMW', 'Mercedes', 'Lada', 'BMW', 'Ferrari', 'Lada', 'Mercedes', 'Ferrari'],
    'цена': [5000000, 6000000, 1000000, 8000000, 25000000, 1200000, 7500000, 30000000]
}
df = pd.DataFrame(data)

# 2. Топ-10 марок по СРЕДНЕЙ цене
top_avg = df.groupby('марка')['цена'].mean().sort_values(ascending=False).head(10)
print("Топ-10 по средней цене:\n", top_avg)

print("-" * 30)

# 3. Топ-10 марок по МАКСИМАЛЬНОЙ цене одной машины
top_max = df.groupby('марка')['цена'].max().sort_values(ascending=False).head(10)
print("Топ-10 по максимальной цене:\n", top_max)
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. Создаем тестовые данные (для примера)
# ==========================================
data = {
    'Make': ['Toyota', 'Toyota', 'Toyota', 'Toyota', 'BMW', 'Toyota', 'Toyota'],
    'Year': [2018, 2019, 2019, 2020, 2020, 2021, 2021],
    'Price': [1500000, 1600000, 1700000, 1800000, 2500000, 1900000, 2000000]
}
df = pd.DataFrame(data)

# ==========================================
# 2. Фильтруем только Toyota
# ==========================================
toyota_df = df[df['Make'] == 'Toyota']

# ==========================================
# 3. Считаем среднюю цену по годам
# ==========================================
# Результатом будет объект Series, где индекс - это Year, а значения - средняя цена
toyota_avg_price = toyota_df.groupby('Year')['Price'].mean()

# ==========================================
# 4. Линейный график
# ==========================================
# Создаем фигуру заданного размера
plt.figure(figsize=(10, 5))

# Строим график: marker='o' добавит точки на линию для наглядности
toyota_avg_price.plot(kind='line', marker='o', grid=True, color='blue')

# Добавляем заголовок и подписи осей
plt.title('Средняя цена автомобилей Toyota по годам', fontsize=14)
plt.xlabel('Год выпуска', fontsize=12)
plt.ylabel('Средняя цена (руб.)', fontsize=12)

# Заставляем ось X показывать все годы (а не через один)
plt.xticks(toyota_avg_price.index)

# Отображаем график
plt.show()

# ==========================================
# 5. Столбчатая диаграмма (Bar chart)
# ==========================================
# Используем figsize=(10, 3), как в задании
plt.figure(figsize=(10, 3))

toyota_avg_price.plot(kind='bar', color='orange', grid=True, alpha=0.8)

plt.title('Средняя цена автомобилей Toyota по годам (Столбчатая диаграмма)', fontsize=14)
plt.xlabel('Год выпуска', fontsize=12)
plt.ylabel('Средняя цена (руб.)', fontsize=12)

# rotation=0 делает подписи лет горизонтальными для удобства чтения
plt.xticks(rotation=0)

plt.show()