# encoding:utf-8

import numpy as np
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

N = 500
x = np.random.randn(N)

trace0 = go.Scatter(x=np.random.randn(N), y=np.random.randn(N) + 2, name='Above', mode='lines+markers',
                    marker=dict(
                        size=10,  # 设置点的宽度
                        color='rgba(152,0,0,.8)',  # 设置点的颜色
                        line=dict(
                            width=2,  # 设置线条宽度
                            color='rgb(0,0,0)'  # 设置线条颜色
                        )
                    ))

trace1 = go.Scatter(x=np.random.randn(N), y=np.random.randn(N) - 2, name='Below', mode='markers',
                    marker=dict(
                        size=10,  # 设置点的宽度
                        color='rgba(255,182,193,.9)',  # 设置点的颜色
                        line=dict(
                            width=2  # 设置线条宽度
                        )
                    ))

data = [trace0, trace1]

layout = dict(title='Styled Scatter', yaxis=dict(zeroline=True), xaxis=dict(zeroline=True))
fig = dict(data=data, layout=layout)
pyplt(fig, filename='tmp/scatter_style.html')
