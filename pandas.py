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