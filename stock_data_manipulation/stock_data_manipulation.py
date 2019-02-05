import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style


# Start and end dates
# start = dt.datetime(2010, 1, 1)
# end = dt.datetime(2018, 12, 31)

# Create dataframe for TSLA stock from Yahoo Finance API, save as CSV
# df = web.DataReader('TSLA', 'yahoo', start, end)
# Save dataframe as a CSV
# df.to_csv('tsla.csv')


# Read in created CSV from above code
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# Create 100 day moving avg col
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

# Each matplotlib plot has a figure and the figure contains all your subplots (axes)
# 'subplot2grid' function --> grid size, starting point, how many rows, how many cols
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

# Plot the axes by passing in x and y values, x is the date (index of df) and y is a col in the df
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()
