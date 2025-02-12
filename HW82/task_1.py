import pandas as pd
import matplotlib.pyplot as plt

# load data
data = pd.read_csv("vgsale_1.csv")

# observes first rows for understand logics and architecture
print(data.head())

# check all info on data
print(data.info())

# divide data on two age
data_before_2000 = data[data['Year'] <= 2000]
data_after_2000 = data[data['Year'] > 2000]

# group by genres and sum sales
genre_sales_before_2000 = data_before_2000.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
genre_sales_after_2000 = data_after_2000.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

# build columns charts
plt.figure(figsize=(14, 6))

# chart for before 2000 age
plt.subplot(1, 2, 1)
genre_sales_before_2000.plot(kind='bar', color='skyblue')
plt.title('Популярные жанры до 2000 года (по продажам)')
plt.ylabel('Мировые продажи (млн)')
plt.xlabel('Жанры')

# chart for after 2000 age
plt.subplot(1, 2, 2)
genre_sales_after_2000.plot(kind='bar', color='salmon')
plt.title('Популярные жанры после 2000 года (по продажам)')
plt.ylabel('Мировые продажи (млн)')
plt.xlabel('Жанры')

plt.tight_layout()
plt.show()