# encoding:utf-8
import pandas as pd
import plotly as py
import plotly.graph_objs as go

pd.set_option('display.width', 450)
pyplt = py.offline.plot

df = pd.read_csv('dat/tk01_m15.csv')
df9 = df[:10]
print(df9)

idx = df9['xtim']

xd0 = (df9['close'] - 27) * 50
df2 = df9

df2['xd1'] = xd0 - 10
df2['xd2'] = xd0
df2['xd3'] = xd0 + 10
print('df2\n', df2)

xtr1 = go.Scatter(
    x=idx,
    y=df2['xd1'],
    mode='markers',
    name='xtr1-markers'
)

xtr2 = go.Scatter(
    x=idx,
    y=df2['xd2'],
    mode='lines',
    name='xtr2-lines'
)

xtr3 = go.Scatter(
    x=idx,
    y=df2['xd3'],
    mode='markers+lines',
    name='xtr3-markers+lines'
)

xdat = go.Data([xtr1, xtr2, xtr3])
layout = go.Layout(title='收盘价---15分钟分时数据', xaxis=go.XAxis(tickangle=-15))
fig = go.Figure(data=xdat, layout=layout)
pyplt(fig, filename=r'tmp/scatter_apply.html')
print('ok')
