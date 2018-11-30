# encoding:utf-8

import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 4, 9, 16],
    mode='markers',
    text=['A</br>size:40</br>default', 'B</br>size:60</br>default', 'C</br>size:80</br>default',
          'D</br>size:100</br>default'],
    name='default',
    marker=dict(
        size=[400, 600, 800, 1000],
        sizemode='area'
    )
)

trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[5, 8, 13, 20],
    mode='markers',
    text=['A</br>size:40</br>sizeref0.2', 'B</br>size:60</br>sizeref0.2', 'C</br>size:80</br>sizeref0.2',
          'D</br>size:100</br>sizeref0.2'],
    name='ref0.2',
    marker=dict(
        size=[400, 600, 800, 1000],
        sizemode='area',
        sizeref=0.2
    )
)

trace2 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[9, 12, 17, 24],
    mode='markers',
    text=['A</br>size:40</br>sizeref2', 'B</br>size:60</br>sizeref2', 'C</br>size:80</br>sizeref2',
          'D</br>size:100</br>sizeref2'],
    name='ref2',
    marker=dict(
        size=[400, 600, 800, 1000],
        sizemode='area',
        sizeref=2
    )
)
data = [trace0, trace1, trace2]
pyplt(data, filename='tmp/bubble_scale.html')
