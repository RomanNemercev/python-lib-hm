import pandas as pd
import matplotlib.pyplot as plt

file_path = "IQ_countries.csv"

# reading file as normal text for correct research rows
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# table's header
headers = lines[0].strip().split(',')

# fnc for format row


def process_row(row):
    values = row.strip().split(',')  # split lines on commas
    values = [v.strip('"') for v in values]  # remove quotes at the beginning and at the end

    # if row is crashed, then return list of 10 elements include empty rows
    while len(values) < len(headers):
        values.append('0')

    return values


# reading all rows and check their
cleaned_data = [process_row(line) for line in lines[1:]]

# created DataFrame from format rows
df = pd.DataFrame(cleaned_data, columns=headers)

# replace empty rows and crashed data on "0"
df.replace([' ', ''], '0', inplace=True)

print('Первые 5 строк данных:', end='\n\n')
print(df.head())
print('Проверяю типы данных:', end='\n\n')
print(df.info())
print('Проверяю выборочные столбцы:', end='\n\n')
print(df[['Rank', 'Country', 'Average IQ']].head())

# I format the data columns into the appropriate data type
df['Rank'] = df['Rank'].astype(int)

# check format data
print('Проверяю форматированный тип данны с объекта в число:', end='\n\n')
print(df['Rank'].info())

# formatting was successful!
# I continue checking the data
df[['Country', 'Continent',]] = df[['Country', 'Continent',]].astype(str)
print(
    'Проверяю форматирование столбцов "Страна" и "Континент" '
    'из объекта в строку',
    end='\n\n'
)
print(df[['Country', 'Continent']].info())
print(df['Country'].apply(type).value_counts())

#  Заметил что столбец "Population" не валидный. Нужно убрать разделители и буквы
df['Population'] = df['Population'].astype(str)  # Приводим к строке на всякий случай
df['Population'] = df['Population'].str.replace(r'\D', '', regex=True)  # удаляем все кроме цифр
df['Population'] = df['Population'].astype(int)  # приводим к int

print('Проверяю тип данных "Population", после форматирования.', end='\n\n')
print(df['Population'].apply(type).value_counts())

print('Проверяю тип данных в Gross National Income:')
print(df['Gross National Income'].apply(type).value_counts())
df['Gross National Income'] = pd.to_numeric(df['Gross National Income'], errors='coerce')
df['Gross National Income'] = df['Gross National Income'].astype('Int64')


# save result
df.to_csv("IQ_countries_clean.csv", index=False)

# load data
data = pd.read_csv("IQ_countries_clean.csv")

# check all info on data
print('Проверка итоговых данных перед созданием графиков:')
print(data.info())
print(data.head())

# Данные корректны, начинаю построение графиков
# 1. Связь между нобелевскими премиями и интеллектом
plt.scatter(data['Average IQ'], data['Nobel Prices'], alpha=0.5)
plt.xlabel('Average IQ')
plt.ylabel('Nobel Prices')
plt.title('Связь между IQ и Нобелевскими премиями')
plt.show()

# 2. Средний IQ по Континентам
data.groupby('Continent')['Average IQ'].mean().plot(kind='bar')
plt.ylabel('Средний IQ')
plt.xlabel('Средний IQ на континентах')
plt.show()

# 3. Распределение численности населения
data['Population'].hist(bins=30)
plt.xlabel('Численность населения')
plt.ylabel('Количество стран')
plt.title('Распределение населения по странам')
plt.show()
