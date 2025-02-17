#collection to dataframe

import pandas as pd

data = {
    'Name': ['John','Robert','Alf','Erica','Roque','Pantaras'],
    'Grades':[90,87,92,90,91,95]
}

df = pd.DataFrame(data)

print(type(df))
print(df)