import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("shopping_habits.csv")

# проверил данные перед обработкой
# print(df.head())
# print(df.info())
#
# unique_states = df['Location'].nunique()
# print(f"Уникальных значений в столбце Location: {unique_states}")

# group data for asc
data_sorted = df.groupby("Location")["Purchase Amount (USD)"].sum().sort_values(ascending=False)

# Суммы покупок по штатам
plt.figure(figsize=(10, 5))
data_sorted.plot(kind="bar", color="skyblue")
plt.title("Общая сумма покупок по локациям")
plt.xlabel("Локация")
plt.ylabel("Сумма покупок (USD)")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Средняя сумма покупок по возрастам
df["Age Group"] = pd.cut(df["Age"], bins=[18, 25, 35, 50, 65, 100], labels=["18-25", "26-35", "36-50", "51-65", "65+"])
age_purchase = df.groupby("Age Group", observed=False)["Purchase Amount (USD)"].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
age_purchase.plot(kind="bar", color="coral")
plt.title("Средняя сумма покупок по возрастным группам")
plt.xlabel("Возрастная группа")
plt.ylabel("Средний чек (USD)")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()


# Влияние скидок и промокодов на сумму покупок
discount_effect = df.groupby("Discount Applied")["Purchase Amount (USD)"].mean()
promo_effect = df.groupby("Promo Code Used")["Purchase Amount (USD)"].mean()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

discount_effect.plot(kind="bar", color=["red", "green"], ax=axes[0])
axes[0].set_title("Средний чек с/без скидки")
axes[0].set_xlabel("Скидка применена?")
axes[0].set_ylabel("Средний чек (USD)")

promo_effect.plot(kind="bar", color=["blue", "orange"], ax=axes[1])
axes[1].set_title("Средний чек с/без промокода")
axes[1].set_xlabel("Промокод применен?")
axes[1].set_ylabel("Средний чек (USD)")
plt.tight_layout()
plt.show()


# Популярность категорий товаров
category_counts = df["Category"].value_counts().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
category_counts.plot(kind="bar", color="purple")
plt.title("Популярность категорий товаров")
plt.xlabel("Категория")
plt.ylabel("Количество покупок")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
