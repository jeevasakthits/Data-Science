import chart_studio.plotly as py
from plotly.graph_objs import *
import pandas as pd
import chart_studio.plotly
import plotly.graph_objs as go
df=pd.read_csv("F:/jeeva/Salary_prediction_web_app/files/500092.csv")


trace1 = {
  "name": "GS", 
  "type": "candlestick", 
  "x":df["Date"][::-1],
  "yaxis": "y2", 
  "low":df["Low Price"][::-1],
  "high": df["High Price"][::-1],
  "open": df["Open Price"][::-1],
  "close": df["Close Price"][::-1],
  "decreasing": {"line": {"color": "#7F7F7F"}}, 
  "increasing": {"line": {"color": "#17BECF"}}
}
mid=[]
for i in range(len(df)):
    pred_mid=(float(df["High Price"][i])+float(df["Low Price"][i]))/2.0
    mid.append(pred_mid)
trace2 = {
  "line": {"width": 1}, 
  "mode": "lines", 
  "name": "Moving Average", 
  "type": "scatter", 
  "x": df["Date"][::-1],
  "y":mid[::-1],
  "yaxis": "y2", 
  "marker": {"color": "#E377C2"}
}
trace3 = {
  "name": "Volume", 
  "type": "bar", 
  "x": df["Date"][::-1],
  "y": df["No.of Shares"][::-1],
  "yaxis": "y", 
  "marker": {"color": ["#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF", "#17BECF", "#7F7F7F", "#7F7F7F", "#17BECF", "#7F7F7F", "#17BECF", "#17BECF", "#17BECF"]}
}
high=[]
low=[]
for i in range(20):
    high.append(None)
    low.append(None)
import statistics
high2=df["High Price"][::-1]
low2=df["Low Price"][::-1]

for i in range(20,len(df)):
    high1=high2[i-20:i]
    low1=low2[i-20:i]
    highavg=sum(high1)/20.0
    lowavg=sum(low1)/20.0
    highstd=statistics.stdev(high1)*2
    lowstd=statistics.stdev(low1)*2
    high_vl=highavg+highstd
    low_vl=lowavg+lowstd
    high.append(high_vl)
    low.append(low_vl)

    
trace4 = {
  "line": {"width": 1}, 
  "name": "Bollinger Bands", 
  "type": "scatter", 
  "x": df["Date"][::-1],
  "y": high,
  "yaxis": "y2", 
  "marker": {"color": "#ccc"}, 
  "hoverinfo": "none", 
  "legendgroup": "Bollinger Bands"
}
trace5 = {
  "line": {"width": 1}, 
  "type": "scatter", 
  "x": df["Date"][::-1],
  "y": low,
  "yaxis": "y2", 
  "marker": {"color": "#ccc"}, 
  "hoverinfo": "none", 
  "showlegend": False, 
  "legendgroup": "Bollinger Bands"
}
data = Data([trace1, trace2, trace3, trace4, trace5])
layout = {
  "xaxis": {"rangeselector": {
      "x": 0, 
      "y": 0.9, 
      "font": {"size": 13},  
      "bgcolor": "rgba(150, 200, 250, 0.4)", 
      "buttons": [
        {
          "step": "all", 
          "count": 1, 
          "label": "reset"
        }, 
        {
          "step": "year", 
          "count": 1, 
          "label": "1yr", 
          "stepmode": "backward"
        }, 
        {
          "step": "month", 
          "count": 3, 
          "label": "3 mo", 
          "stepmode": "backward"
        }, 
        {
          "step": "month", 
          "count": 1, 
          "label": "1 mo", 
          "stepmode": "backward"
        }, 
        {"step": "all"}
      ]
    }}, 
  "yaxis": {
    "domain": [0, 0.2], 
    "showticklabels": False
  }, 
  "legend": {
    "x": 0.3, 
    "y": 0.9, 
    "yanchor": "bottom", 
    "orientation": "h"
  }, 
  "margin": {
    "b": 40, 
    "l": 40, 
    "r": 40, 
    "t": 40
  }, 
  "yaxis2": {"domain": [0.2, 0.8]}, 
  "plot_bgcolor": "rgb(250, 250, 250)"
}

fig = Figure(data=data, layout=layout)
print("plot_bgcolor")
plot_url = py.plot(fig)
