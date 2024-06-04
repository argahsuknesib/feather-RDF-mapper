import os
import pandas as pd

# Initialize an empty DataFrame to store the final results
final_dataframe = pd.DataFrame()

# Define the folder path
folder_path = '/home/kush/Dataset/protego_day/Protego_anom/'

# Iterate through each folder
for foldername in os.listdir(folder_path):
    folder = os.path.join(folder_path, foldername)
    
    # Check if it's a directory
    if os.path.isdir(folder):
        file_path = os.path.join(folder, 'data.feather')
        
        # Check if the data.feather file exists
        if os.path.exists(file_path):
            # Read the feather file into a DataFrame
            df = pd.read_feather(file_path)
            print(df)
            
            # Filter for 'org.dyamand.types.health.SpO2' in the 'Metric' column
            filtered_data = df[df['Metric'] == 'org.dyamand.types.health.SpO2']
            
            # Append the filtered data to the final DataFrame
            final_dataframe = final_dataframe.concat(filtered_data)

# Display the final DataFrame
print(final_dataframe)
