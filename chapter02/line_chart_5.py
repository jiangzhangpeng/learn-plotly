# encoding:utf-8
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

title = 'Main Source for News'
labels = ['Television', 'Newspaper', 'Internet', 'Radio']
colors = ['rgba(67,67,67,1)', 'rgba(115,115,115,1)', 'rgba(49,130,89,1)', 'rgba(189,189,189,1)']
mode_size = [8, 8, 12, 8]
line_size = [2, 2, 4, 2]
x_data = [
    [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
    [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
    [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
    [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
]

y_data = [
    [74, 82, 80, 74, 73, 72, 74, 70, 70, 66, 66, 69],
    [45, 42, 50, 46, 36, 36, 34, 35, 32, 31, 31, 28],
    [13, 14, 20, 24, 20, 24, 24, 40, 35, 41, 43, 50],
    [18, 21, 18, 21, 16, 14, 13, 18, 17, 16, 19, 23],
]
traces = []
for i in range(0, 4):
    traces.append(go.Scatter(
        x=x_data[i],
        y=y_data[i],
        mode='lines',
        line=dict(color=colors[i], width=line_size[i]),
        connectgaps=True
    ))

    traces.append(go.Scatter(
        x=[x_data[i][0], x_data[i][11]],
        y=[y_data[i][0], y_data[i][11]],
        mode='markers',
        marker=dict(color=colors[i], size=mode_size[i])
    ))

layout = go.Layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,  # 显示坐标信息
        linecolor='rgb(204,204,204)',  # x轴颜色
        linewidth=2,
        autotick=False,  # True为自动删除部分日期，False为保持原状
        ticks='outside',  # x轴上的刻度线，在图内或图外
        tickcolor='rgb(204,204,204)',  # x轴刻度线颜色
        tickwidth=2,  # 刻度线宽度
        ticklen=10,  # 刻度线长度
        tickfont=dict(  # x轴上坐标标记的字体样式、大小、颜色
            family='Arial',
            size=12,
            color='rgb(82,82,82)'
        )
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        zeroline=False,
        showticklabels=False
    ),
    autosize=False,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110
    ),
    showlegend=False
)

annotations = []
# Adding labels
for y_trace, label, color in zip(y_data, labels, colors):
    # labeling the left_side of the plot
    annotations.append(dict(
        xref='paper',
        x=0.05,
        y=y_trace[0],
        xanchor='right',
        yanchor='middle',
        text=label + ' {}%'.format(y_trace[0]),
        font=dict(
            family='Arial',
            size=16,
            color=color
        ),
        showarrow=False
    ))
    # labeling the right_side of the plot
    annotations.append(dict(
        xref='paper',
        x=0.95,
        y=y_trace[11],
        xanchor='left',
        yanchor='middle',
        text=label + ' {}%'.format(y_trace[11]),
        font=dict(
            family='Arial',
            size=16,
            color=color
        ),
        showarrow=False
    ))

# Title
annotations.append(dict(
    xref='paper',
    yref='paper',
    x=0.0,
    y=1.05,
    xanchor='left',
    yanchor='bottom',
    text='Main Source for News',
    font=dict(
        family='Arial',
        size=30,
        color='rgb(37,37,37)'
    ),
    showarrow=False
))

# Source
annotations.append(dict(
    xref='paper',
    yref='paper',
    x=0.5,
    y=-0.1,
    xanchor='center',
    yanchor='top',
    text='Source: PewResearch Center & Storytelling with data',
    font=dict(
        family='Arial',
        size=12,
        color='rgb(150,150,150)'
    ),
    showarrow=False
))

layout['annotations'] = annotations

fig = go.Figure(data=traces, layout=layout)
pyplt(fig, filename='tmp/news-source.html')
