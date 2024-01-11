from django.shortcuts import render
import plotly.graph_objects as go
import pandas as pd

def plot_graph(request):
    # Replace this URL with the path to your CSV file
    csv_url = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
    df = pd.read_csv(csv_url)

    fig = go.Figure(data=go.Ohlc(x=df['Date'],
                    open=df['AAPL.Open'],
                    high=df['AAPL.High'],
                    low=df['AAPL.Low'],
                    close=df['AAPL.Close']))

    fig.update_layout(
        title='The Great Recession',
        yaxis_title='AAPL Stock',
        shapes=[dict(
            x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
            line_width=2)],
        annotations=[dict(
            x='2016-12-09', y=0.05, xref='x', yref='paper',
            showarrow=False, xanchor='left', text='Increase Period Begins')]
    )

    # Convert the Plotly figure to JSON for embedding in the template
    graph_json = fig.to_json()

    return render(request, 'plot_template.html', {'graph_json': graph_json})
