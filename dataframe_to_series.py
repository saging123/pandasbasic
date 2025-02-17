#collection to dataframe
import pandas as pd
data = {
    'Name': ['John','Robert','Alf','Erica','Roque','Pantaras'],
    'Grades':[90,87,92,90,91,95]
}
df = pd.DataFrame(data)

# extract names
extracted_names = df['Name']

print(type(extracted_names))
print(extracted_names)