import pandas as pd

def test():
    file = pd.read_feather('data/dataset_participant6.feather')
    # dataframe_temperature = file[file['Sensor'] == 'velbus.4F.WeatherStation']
    # dataframe_temperature_2 = file[file['Metric'] == 'org.dyamand.types.health.SpO2']
    # # if (dataframe_temperature['Metric'] == 'environment.temperature'):
    # # dataframe_3  = file[file['Metric'] == 'people.presence.detected']
    # dataframe_temperature_metric = dataframe_temperature['Metric']
    # print(dataframe_temperature_metric)
    # # print(dataframe_temperature_metric[''] == 'environment.temperature')
    # print(dataframe_temperature_2['Value'])
    # print(dataframe_temperature_2['Timestamp'])
    print(file['Metric'].unique())
    df = file[file['Metric'] == 'wearable.skt']
#     # print(dataframe['Value'], dataframe['Timestamp'])

# # Convert 'Timestamp' column to datetime format
#     # df['Timestamp'] = pd.to_datetime(df['Timestamp'])

#     df['Sampling-Timestamp'] = pd.to_datetime(df['Timestamp'].astype(str))
# # Set 'Timestamp' as the index
#     df.set_index('Sampling-Timestamp', inplace=True)
#     # df['Timestamp'] = df.index

# # Resample the DataFrame to one observation per second and take the first observation in each second
#     df_resampled = df.resample('2S').first().reset_index()

# # Print the resulting DataFrame
#     print(df_resampled)


test()