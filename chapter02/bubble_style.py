# encoding:utf-8

import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 4, 9, 16],
    mode='markers',
    text=['A<br>size:40', 'B<br>size:60', 'C<br>size:80', 'D<br>size:100'],
    marker=dict(
        color=[20, 100, 180, 250],
        opacity=[1, 0.8, 0.6, 0.4],
        size=[40, 60, 80, 100],
        showscale=True
    )
)

data = [trace0]
pyplt(data, filename='tmp/bubble_style.html')
