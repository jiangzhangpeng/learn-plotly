# encoding:utf-8
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

# trace
trace_basic = [go.Bar(x=['v1', 'v2', 'v3', 'v4', 'v5'], y=[1, 2, 3, 2, 4])]
# layout
layout_basic = go.Layout(
    title='The Graph Title',
    xaxis=go.XAxis(
        range=[-0.5, 4.5],
        domain=[0, 1]
    )
)

# figure
figure_basic = go.Figure(data=trace_basic, layout=layout_basic)

# plot
pyplt(figure_basic, filename='tmp/basic_barchart.html')
