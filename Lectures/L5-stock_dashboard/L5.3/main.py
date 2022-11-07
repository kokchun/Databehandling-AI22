from dash import dcc, html
from dash.dependencies import Output, Input
import dash
from load_data import StockDataLocal
import plotly_express as px
from time_filtering import filter_time
import pandas as pd
import os 

# module variables

path = os.path.join(os.path.dirname(__file__), "stocksdata")

# create an object of type StockDataLocal so that we can load data
stock_data_object = StockDataLocal(path)


symbol_dict = {"AAPL": "Apple", "NVDA": "Nvidia",
               "TSLA": "Tesla", "IBM": "IBM"}

# stock_symbol: [daily_df, intradaily_df]
df_dict = {symbol: stock_data_object.stock_dataframe(
    symbol) for symbol in symbol_dict}


stock_options_dropdown = [{"label": name, "value": symbol}
                          for symbol, name in symbol_dict.items()]

# ohlc - Open, High, Low, Close
ohlc_options = [{"label": option.capitalize(), "value": option}
                for option in ["open", "high", "low", "close"]]

slider_marks = {i: mark for i, mark in enumerate(
    ["1 day", "1 week", "1 month", "3 months", "1 year", "5 year", "Max"])}

# creates a Dash App
app = dash.Dash(__name__)

# TODO: bootstrap styling

app.layout = html.Div([
    html.H1("Stocks viewer"),
    html.P("Choose a stock"),
    dcc.Dropdown(id='stock-picker-dropdown', className='',
                 options=stock_options_dropdown,
                 value='AAPL',
                 placeholder='Apple'
                 ),
    html.P(id = "highest-value"),
    html.P(id = "lowest-value"),
    dcc.RadioItems(id='ohlc-radio', className='',
                   options=ohlc_options,
                   value='close'
                   ),
    dcc.Graph(id="stock-graph"),
    dcc.Slider(id='time-slider',
               min=0,
               max=6,
               step=None,
               value=2,
               marks=slider_marks
               ),

    # stores an intermediate value on the clients browser for sharing between callbacks
    dcc.Store(id="filtered-df"),
])




@app.callback(Output("filtered-df", "data"), Input("stock-picker-dropdown", "value"),
              Input("time-slider", "value"))
def filter_df(stock, time_index):
    """Filters the dataframe and stores it intermediary for usage in callbacks
    Returns:
        json object of filtered dataframe
    """
    dff_daily, dff_intraday = df_dict[stock]

    dff = dff_intraday if time_index <= 2 else dff_daily

    days = {i: day for i, day in enumerate([1, 7, 30, 90, 365, 365*5])}

    dff = dff if time_index == 6 else filter_time(dff, days=days[time_index])

    return dff.to_json()

# when something changes in the input component, the code in function below will run and update the output component
# the components are connected through their id
@app.callback(
    Output("stock-graph", "figure"),
    Input("filtered-df", "data"),
    Input("ohlc-radio", "value"),
    Input("stock-picker-dropdown", "value")
)
def update_graph(json_df, ohlc, stock):
    """Updates graph based on different unputs"""

    dff = pd.read_json(json_df)

    fig = px.line(dff, x=dff.index,
                  y=ohlc, title=symbol_dict[stock])

    # TODO: Add figure settings to make graph look nice

    return fig

@app.callback(
    Output("highest-value", "children"),
    Output("lowest-value", "children"),
    Input("filtered-df", "data"),
    Input("ohlc-radio", "value")
)
def highest_lowest_value(json_df, ohlc):
    dff = pd.read_json(json_df)
    highest_value = f"Highest value {dff[ohlc].max()}"
    lowest_value = f"Lowest value {dff[ohlc].min()}"
    return highest_value, lowest_value


if __name__ == "__main__":
    app.run_server(debug=True)
