import dash
import dash_bootstrap_components as dbc
import os 
from load_data import StockData

directory_path = os.path.dirname(__file__)
path = os.path.join(directory_path, "stocksdata")

print(path)

stockdata_object = StockData(path)

print(stockdata_object.stock_dataframe("AAPL"))
