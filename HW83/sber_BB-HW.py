import pandas as pd
import numpy as np
import plotly.graph_objects as go

# load data
file_path = 'SBER.csv'
data = pd.read_csv(file_path, sep=';')

# format data on correct
data['DATE'] = np.array(pd.to_datetime(data['DATE']))

# setup settings
ma_size = 20  # age SMA
bol_size = 2  # width screen 'hall'

# calculate BB
data['SMA'] = data['CLOSE'].rolling(ma_size).mean()
data['BB_UP'] = data['SMA'] + data['CLOSE'].rolling(ma_size).std() * bol_size
data['BB_DOWN'] = data['SMA'] - data['CLOSE'].rolling(ma_size).std() * bol_size

# create chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['DATE'], y=data['CLOSE'], mode='lines', name='Цена закрытия', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=data['DATE'], y=data['SMA'], mode='lines', name='SMA (20)', line=dict(color='orange')))
fig.add_trace(go.Scatter(x=data['DATE'], y=data['BB_UP'], mode='lines', name='Верхняя полоса', line=dict(color='red')))
fig.add_trace(go.Scatter(x=data['DATE'], y=data['BB_DOWN'], mode='lines', name='Нижняя полоса', line=dict(color='green')))

# setup chart
fig.update_layout(title='Полосы Боллинджера для акций Сбербанка', xaxis_title='Дата', yaxis_title='Цена', template='plotly_dark')

fig.show()
