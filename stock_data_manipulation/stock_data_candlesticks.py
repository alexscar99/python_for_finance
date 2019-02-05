import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
from matplotlib import style
from pandas.plotting import register_matplotlib_converters


# Set style
style.use('ggplot')

# Register matplotlib converters registered by pandas on import
register_matplotlib_converters()

# Read in CSV to create dataframe
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# Resample daily 'Adj Close' to 10 day using ohlc ('Open', 'High', 'Low', 'Close')
df_ohlc = df['Adj Close'].resample('10D').ohlc()
# Resample daily 'Volume' to 10 day using sum
df_volume = df['Volume'].resample('10D').sum()

# Reset the index for df_ohlc so that date is now a col
df_ohlc.reset_index(inplace=True)
# Convert date to mdates
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


# Create figure subplots
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
# Take mdates and display them in readable format
ax1.xaxis_date()

# Create candlesticks from ohlc values, size based on volume
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num),
                 df_volume.values, 0, color='b')

# Visualize data
plt.show()
