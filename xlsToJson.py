import pandas as pd
import json
from pandas.io.json import _normalize


inputpath = input('enter file path(/path/to/file.xlsx): ')

excel_file = inputpath
print(inputpath)

df = pd.read_excel(excel_file, engine='openpyxl')

combined_data = df
combined_data['id'] = range(1, len(combined_data) + 1)

# Convert the DataFrame to a JSON object
json_data = json.dumps(df.to_dict(orient='records'), ensure_ascii=False)

# Write the JSON data to a file
with open('output.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json_data)


