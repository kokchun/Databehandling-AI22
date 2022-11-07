from dateutil.relativedelta import relativedelta
from datetime import datetime

def filter_time(df, days = 0):
    last_day = df.index[0].date()
    start_day = last_day-relativedelta(days = days)
    df = df.sort_index().loc[start_day:last_day]
    return df 
