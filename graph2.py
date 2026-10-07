import plotly.express as px

def intHistogram(data):
    
    fig = px.histogram(data, x="Rating", nbins=20, title="Album Rating Distribution")
    
    fig.update_xaxes(tickmode="linear", tick0=0, dtick=1)
    
    fig.update_yaxes(title = "Number of Albums")
    
    fig.update_traces(hovertemplate="Rating: %{x}<br>Count: %{y}<extra></extra>")
    
    fig.show()