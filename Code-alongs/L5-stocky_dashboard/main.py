import dash
import dash_bootstrap_components as dbc
import os
from load_data import StockData
from dash import html, dcc  # dcc - dash core components

directory_path = os.path.dirname(__file__)
path = os.path.join(directory_path, "stocksdata")

print(path)

stockdata_object = StockData(path)

# pick one stock
# print(stockdata_object.stock_dataframe("AAPL"))

symbol_dict = {"AAPL": "Apple", "NVDA": "Nvidia", "TSLA": "Tesla", "IBM": "IBM"}

df_dict = {symbol: stockdata_object.stock_dataframe(symbol) for symbol in symbol_dict}

stock_options_dropdown = [
    {"label": name, "value": symbol} for symbol, name in symbol_dict.items()
]

print(df_dict.keys())
# print(df_dict["TSLA"][0])

# create a Dash App
app = dash.Dash(__name__)

app.layout = html.Main(
    [
        html.H1("Techy stocks viewer"),
        html.P("Choose a stock"),
        dcc.Dropdown(
            id="stockpicker-dropdown",
            options=stock_options_dropdown,
            value="AAPL",
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
