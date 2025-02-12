import pandas as pd
# import matplotlib as plt

# load data
# data = pd.read_csv("IQ_countries.csv")
file_path = "IQ_countries.csv"

# observes first rows for understand logics and arhitecture
# print(data.head())

# check all info on data
# print(data.info())

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
df['Population'] = df['Population'].str.replace(r'\D', '', regex=True)  # удаляем все цифры
df['Population'] = df['Population'].astype(int)  # приводим к int

print('Проверяю тип данных "Population", после форматирования.', end='\n\n')
print(df['Population'].apply(type).value_counts())


# save result
df.to_csv("IQ_countries_clean.csv", index=False)

# df[['Average IQ', 'Literacy Rate', 'Human Development Index', 'Mean years of schooling', 'Gross National Income']]