import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Загружаем данные
data = pd.read_csv("vgsale_1.csv")

# 2️⃣ Очистка данных: убираем дубликаты по играм (агрегируем продажи)
def clean_game_sales(data):
    """
    Объединяет данные по одной и той же игре, вышедшей на разных платформах.
    Складывает продажи, оставляя уникальные записи.
    """
    clean_data = data.groupby(['Name', 'Year', 'Publisher'], as_index=False).agg({
        'NA_Sales': 'sum',
        'EU_Sales': 'sum',
        'JP_Sales': 'sum',
        'Other_Sales': 'sum',
        'Global_Sales': 'sum',
        'Genre': 'first',  # Берём жанр первой записи
        'Platform': lambda x: ', '.join(set(x))  # Записываем все платформы в одну строку
    })
    return clean_data

cleaned_data = clean_game_sales(data)

# Сохраняем очищенные данные
cleaned_data.to_csv("vgsale_cleaned.csv", index=False)

data["Year"] = data["Year"].fillna(0).astype(int)

# 3️⃣ График: Количество видеоигр по годам (без дубликатов по Name)
games_per_year = data.drop_duplicates(subset=["Name"]).groupby("Year")["Name"].count()

plt.figure(figsize=(12, 5))
games_per_year.plot(kind="bar", color="lightblue")
plt.title("Количество выпущенных видеоигр по годам")
plt.ylabel("Количество игр")
plt.xlabel("Год")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# 4️⃣ Топ-3 издателя по количеству выпущенных игр
top_publishers = data["Publisher"].value_counts().nlargest(3)  # Берём топ-3
print("Топ-3 издателя:\n", top_publishers)

# Визуализация топ-3 издателей
plt.figure(figsize=(10, 5))
top_publishers.plot(kind="bar", color=["red", "green", "blue"])
plt.title("Топ-3 издателя по количеству выпущенных игр")
plt.ylabel("Количество игр")
plt.xlabel("Издатель")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# 5️⃣ График: Количество игр топ-3 издателей по платформам
top_publisher_names = top_publishers.index
top_publisher_data = data[data["Publisher"].isin(top_publisher_names)]

plt.figure(figsize=(12, 6))
top_publisher_data.groupby(["Publisher", "Platform"])["Name"].count().unstack().plot(kind="bar", stacked=True, figsize=(12, 6))
plt.title("Игры по платформам у топ-3 издателей")
plt.ylabel("Количество игр")
plt.xlabel("Издатель")
plt.xticks(rotation=0)
plt.legend(title="Платформа")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# 6️⃣ Круговые диаграммы долей продаж по регионам (1980-2000 и 2000-2020)
data_before_2000 = data[data['Year'] <= 2000]
data_after_2000 = data[data['Year'] > 2000]

sales_before_2000 = data_before_2000[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
sales_after_2000 = data_after_2000[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].pie(sales_before_2000, labels=sales_before_2000.index, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'purple'])
axes[0].set_title("Доли продаж 1980-2000")

axes[1].pie(sales_after_2000, labels=sales_after_2000.index, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'purple'])
axes[1].set_title("Доли продаж 2000-2020")

plt.tight_layout()
plt.show()
