import requests
import pandas as pd
import os


class StockDataAPI:
    """Class with methods to get and process stock data from Alpha Vantage"""

    def __init__(self, api_key, data_function: str = "TIME_SERIES_DAILY") -> None:
        """
        Args:
            api_key: a unique API key from here: https://www.alphavantage.co/support/#api-key
            data_function: Alpha Vantage function for obtaining different types of time series data. See documentation: https://www.alphavantage.co/documentation/
        """
        self._data_function = data_function
        self._api_key = api_key

    def get_stock(self, symbol: str) -> pd.DataFrame:
        """Performs a GET request on Alpha Vantage to get stock data

        Args:
            symbol: stock symbol

        Returns:
            a Pandas DataFrame with index dates, columns [1. open, 2. high, 3. low, 4. close, 5. volume]
        """

        url = f"https://www.alphavantage.co/query?function={self._data_function}&symbol={symbol}&apikey={self._api_key}&outputsize=full"
        try:
            data = requests.get(url).json()  # GET request
        except KeyError as err:
            print(err)
            print("You can't access the stock too fast, wait a little bit")

        df = pd.DataFrame(data["Time Series (Daily)"]).transpose().astype(float)
        df.index = pd.to_datetime(df.index)
        df.columns = ["Open", "High", "Low", "Close", "Volume"]

        return df


class StockDataLocal:
    """Class method to get and process local stock data"""

    def __init__(self, data_folder_path: str = "data") -> None:
        """
        Args:
            data_folder_path: path to folder where the data is
        """
        self._data_folder_path = data_folder_path

    def stock_dataframe(self, stockname: str) -> list:
        """Cleans a dataframe of specified filename

        Returns:
            list of two dataframes, one for daily time series and one for intradaily time series
        """

        stock_df_list = []
        for path_ending in [
            "_TIME_SERIES_DAILY_ADJUSTED.csv",
            "_TIME_SERIES_INTRADAY_EXTENDED.csv",
        ]:
            path = os.path.join(self._data_folder_path, stockname+path_ending)

            stock = pd.read_csv(path, index_col=0, parse_dates=True)
            stock.index.rename("Date", inplace=True)

            stock_df_list.append(stock)

        return stock_df_list
