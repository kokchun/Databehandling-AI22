from graphs import Graphs


GB_dropdown_option = [
    {"label": "medals", "value": "medals"},
    {"label": "statistics", "value": "sport_statistics"},
]


@app.callback(Output("graph-left", "figure"), Input("GB-dropdown", "value"))
def update_left_graph(option):
    if option == "medals":
        return Graphs().medals()
    elif option == "sport_statistics":
        return Graphs().sport_statistics()
