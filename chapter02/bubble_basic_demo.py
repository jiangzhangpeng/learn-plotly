# encoding:utf-8

import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 4, 9, 16],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100])
)

data = [trace0]
pyplt(data, filename='tmp/bubble_basic_demo.html')
