import pandas as pd
from dash import dcc, html
from dash.dependencies import Output, Input
import dash
from dotenv import load_dotenv
import os
from load_data import StockDataAPI
import plotly_express as px

# module variables
api_key = os.getenv("ALPHA_API_KEY")
stock_data = StockDataAPI(api_key)

stock_dict = {"AAPL": "Apple", "NVDA": "Nvidia",
                 "TSLA": "Tesla", "IBM": "IBM"}

stock_options = [{"label": name, "value": symbol}
                 for symbol, name in stock_dict.items()]
ohlc_options = [{"label": option, "value": option}
                for option in ["Open", "High", "Low", "Close", "Volume"]]

# creates a Dash App
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stocks viewer"),
    html.P("Choose a stock"),
    dcc.Dropdown(id='stock-picker-dropdown', className='',
                 options=stock_options,
                 value='AAPL',
                 placeholder='Apple'
                 ),
    dcc.Graph(id="stock-graph"),
])

# when something changes in the input component, the code in function below will run and update the output component
# the components are connected through their id 
@app.callback(
    Output("stock-graph", "figure"),
    Input("stock-picker-dropdown", "value"),
)
def update_graph(stock):
    # slow due to limited amount of API calls on free subscription
    df = stock_data.get_stock(stock)
    fig = px.line(df, x=df.index, y="Close",
                  labels={"index": "Date"}, title=stock)

    return fig

# TODO: download local csv-files to work with in order to not overload the free API


if __name__ == "__main__":
    app.run_server(debug=True)
