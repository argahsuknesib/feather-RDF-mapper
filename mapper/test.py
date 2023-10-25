import pandas as pandas

def test():
    file = pandas.read_feather('data/dataset_participant6.feather')
    print(file['Metric'].unique())
    # dataframe_temperature = file[file['Sensor'] == 'velbus.4F.WeatherStation']
    # # dataframe_temperature_2 = file[file['Metric'] == 'org.dyamand.types.health.SpO2']
    # # if (dataframe_temperature['Metric'] == 'environment.temperature'):
    # # dataframe_3  = file[file['Metric'] == 'people.presence.detected']
    # dataframe_temperature_metric = dataframe_temperature['Metric']
    # print(dataframe_temperature_metric)
    # # print(dataframe_temperature_metric[''] == 'environment.temperature')

test()