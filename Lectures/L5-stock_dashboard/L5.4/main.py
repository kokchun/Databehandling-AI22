
from dash.dependencies import Output, Input
import dash
from load_data import StockDataLocal
import plotly_express as px
from time_filtering import filter_time
import pandas as pd
import dash_bootstrap_components as dbc
import sys, os

# module variables

directory_path = os.path.dirname(__file__)

sys.path.append(directory_path)

from layout import Layout

path = os.path.join(directory_path, "stocksdata")

# create an object of type StockDataLocal so that we can load data
stock_data_object = StockDataLocal(path)


symbol_dict = {"AAPL": "Apple", "NVDA": "Nvidia", "TSLA": "Tesla", "IBM": "IBM"}

# stock_symbol: [daily_df, intradaily_df]
df_dict = {symbol: stock_data_object.stock_dataframe(symbol) for symbol in symbol_dict}

stylesheets = [dbc.themes.MATERIA]
# creates a Dash App
app = dash.Dash(
    __name__,
    external_stylesheets=stylesheets,
    meta_tags=[dict(name="viewport", content="width=device-width, initial-scale=1.0")],
)

server = app.server  # needed for Heroku to connect to

app.layout = Layout(symbol_dict).layout()


@app.callback(
    Output("filtered-df", "data"),
    Input("stock-picker-dropdown", "value"),
    Input("time-slider", "value"),
)
def filter_df(stock, time_index):
    """Filters the dataframe and stores it intermediary for usage in callbacks
    Returns:
        json object of filtered dataframe
    """
    dff_daily, dff_intraday = df_dict[stock]

    dff = dff_intraday if time_index <= 2 else dff_daily

    days = {i: day for i, day in enumerate([1, 7, 30, 90, 365, 365 * 5])}

    dff = dff if time_index == 6 else filter_time(dff, days=days[time_index])

    return dff.to_json()


# when something changes in the input component, the code in function below will run and update the output component
# the components are connected through their id


@app.callback(
    Output("stock-graph", "figure"),
    Input("filtered-df", "data"),
    Input("ohlc-radio", "value"),
    Input("stock-picker-dropdown", "value"),
)
def update_graph(json_df, ohlc, stock):
    """Updates graph based on different unputs"""

    dff = pd.read_json(json_df)

    # TODO: Add figure settings to make graph look nice

    return px.line(dff, x=dff.index, y=ohlc, title=symbol_dict[stock])


@app.callback(
    Output("highest-value", "children"),
    Output("lowest-value", "children"),
    Input("filtered-df", "data"),
    Input("ohlc-radio", "value"),
)
def highest_lowest_value(json_df, ohlc):
    dff = pd.read_json(json_df)
    highest_value = f"{dff[ohlc].max():.2f} USD"
    lowest_value = f"{dff[ohlc].min():.2f} USD"
    return highest_value, lowest_value


if __name__ == "__main__":
    app.run_server(debug=True)
