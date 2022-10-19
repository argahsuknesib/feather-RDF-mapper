import pandas as pandas

file = pandas.read_feather('../data/dataset_participant1.feather')
metric = 'people.presence.detected'

dataframe = file[file['Metric'] == 'people.presence.detected']
print(dataframe.head())

# for index in dataframe.index:
#     event = {
#         "metricId": dataframe['Metric'][index],
#         "sourceId": dataframe['Sensor'][index],
#         "timestamp": dataframe['Timestamp'][index],
#         "value": dataframe['Value'][index]
#     }
#     result = annotate_event(event)
#     print(result)
