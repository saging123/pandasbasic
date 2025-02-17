import pandas as pd


series = pd.Series([55,51,54.5,56,55.5,57],
                   index=['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-05','2024-01-06'])
s_df = series.to_frame(name="USD PHP")

print(s_df)