import pandas as pd
import matplotlib.pyplot as plt

# Dummy data
data_with_aggregator = {
    'seconds_to_monitor': [10, 20, 30],
    'stream_reader': [15, 25, 35],
    'stream_processor': [20, 30, 40]
}

data_without_aggregator = {
    'seconds_to_monitor': [10, 20, 30],
    'stream_reader': [10, 20, 30],
    'stream_processor': [18, 28, 38]
}

# Create DataFrames from dummy data
df_with_aggregator = pd.DataFrame(data_with_aggregator)
df_without_aggregator = pd.DataFrame(data_without_aggregator)

# Set the index to 'seconds_to_monitor' for plotting
df_with_aggregator.set_index('seconds_to_monitor', inplace=True)
df_without_aggregator.set_index('seconds_to_monitor', inplace=True)

# Plotting a stacked bar plot
fig, ax = plt.subplots()

# Stacked bar plot for 'stream_reader' and 'stream_processor' for each seconds_to_monitor
df_with_aggregator.plot(kind='bar', stacked=True, ax=ax, color=['blue', 'orange'], width=0.4, position=1.5)
df_without_aggregator.plot(kind='bar', stacked=True, ax=ax, color=['green', 'red'], width=0.4, position=-0.5)

plt.xlabel('Seconds to Monitor')
plt.ylabel('Latency')
plt.title('Comparison of Latency with and without Aggregator')
plt.legend(['Reader with Aggregator', 'Processor with Aggregator', 'Reader without Aggregator', 'Processor without Aggregator'])
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
