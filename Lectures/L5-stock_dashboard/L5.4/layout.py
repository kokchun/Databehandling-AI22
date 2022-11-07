import dash_bootstrap_components as dbc
from dash import html, dcc


class Layout:
    def __init__(self, symbol_dict) -> None:
        self._symbol_dict = symbol_dict

        self.stock_options_dropdown = [
            {"label": name, "value": symbol}
            for symbol, name in self._symbol_dict.items()
        ]

        # ohlc - Open, High, Low, Close
        self.ohlc_options = [
            {"label": option.capitalize(), "value": option}
            for option in ["open", "high", "low", "close"]
        ]

        self.slider_marks = {
            i: mark
            for i, mark in enumerate(
                ["1 day", "1 week", "1 month", "3 months", "1 year", "5 year", "Max"]
            )
        }

        print(self.stock_options_dropdown)

    def layout(self):
        return dbc.Container(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H1(
                                    "Stocks viewer",
                                    className="card-title text-dark mx-3",
                                )
                            ]
                        )
                    ],
                    className="mt-4",
                ),
                dbc.Row(
                    className="mt-4",
                    children=[
                        dbc.Col(
                            # responsivity
                            html.P("Choose a stock"),
                            xs="12",
                            sm="12",
                            md="6",
                            lg="4",
                            xl={"size": 1, "offset": 2},
                            className="mt-1",
                        ),
                        dbc.Col(
                            dcc.Dropdown(
                                id="stock-picker-dropdown",
                                className="",
                                options=self.stock_options_dropdown,
                                value="AAPL",
                                placeholder="Apple",
                            ),
                            xs="12",
                            sm="12",
                            md="12",
                            lg="4",
                            xl="3",
                        ),
                        dbc.Col(
                            [
                                dbc.Card(
                                    [
                                        dcc.RadioItems(
                                            id="ohlc-radio",
                                            className="m-1",
                                            options=self.ohlc_options,
                                            value="close",
                                        ),
                                    ]
                                )
                            ],
                            xs="12",
                            sm="12",
                            md="12",
                            lg="4",
                            xl="3",
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id="stock-graph"),
                                dcc.Slider(
                                    id="time-slider",
                                    min=0,
                                    max=6,
                                    step=None,
                                    value=2,
                                    marks=self.slider_marks,
                                ),
                            ],
                            lg={"size": "6", "offset": 1},
                            xl={"size": "6", "offset": 1},
                        ),
                        dbc.Col(
                            [
                                dbc.Row(
                                    dbc.Card(
                                        [
                                            html.H2(
                                                "Highest value",
                                                className="h5 mt-3 mx-3",
                                            ),
                                            html.P(
                                                id="highest-value",
                                                className="text-success h1 mx-2",
                                            ),
                                        ]
                                    ),
                                    className="mt-5 h-25",
                                ),
                                dbc.Row(
                                    dbc.Card(
                                        [
                                            html.H2(
                                                "Lowest value", className="h5 mt-3 mx-3"
                                            ),
                                            html.P(
                                                id="lowest-value",
                                                className="text-danger h1 mx-2",
                                            ),
                                        ]
                                    ),
                                    className="mt-5 h-25",
                                ),
                            ],
                            sm="5",
                            md="3",
                            lg="3",
                            xl="2",
                            className="mt-5 mx-5",
                        ),
                        html.Footer(
                            [
                                html.H3("Stock viewer 2021", className="h6"),
                                html.P("Dashboard av Kokchun Giang"),
                            ],
                            className="navbar fixed-bottom",
                        ),
                    ]
                ),
                # stores an intermediate value on the clients browser for sharing between callbacks
                dcc.Store(id="filtered-df"),
            ],
            fluid=True,
        )
