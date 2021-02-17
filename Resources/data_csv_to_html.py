import os 
import pandas as pd 

file_path= os.path.join('Resources', 'cities.csv')

cities_csv = pd.read_csv(file_path)

cities_csv.to_html('cities_data_table.html', index=False, classes=['table', 'table-striped', 'table-hover'])
