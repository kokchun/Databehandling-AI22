# Lecture 5.3 - Dashboard

Created dashboard with main functionality in place: 

- choose stock 
- filter time 
- filter OHLC options - open, high, low, close

Note that we use local csv-files for this example and not API calls. 

## Intermediate storage

In this update we use the client-side storage, i.e. the user's browser for storing JSON data after filtering. After filtering this intermediate storage is then used for multiple callbacks such as updating the graph and updating highest and lowest values. We use the **dcc.Store** component for doing this.

