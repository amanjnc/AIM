import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = pd.read_csv('data/benin-malanville.csv')

data['Timestamp'] = pd.to_datetime(data['Timestamp'])

def TimeSeries(column_name):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['Timestamp'], data[column_name], label=column_name)
    ax.set_xlabel('Timestamp')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    ax.set_ylabel('Value')
    ax.set_title('Time Series Analysis')
    ax.legend()
    plt.xticks(rotation=45, ha='right')
    plt.show()

column_name = 'GHI'
TimeSeries(column_name)