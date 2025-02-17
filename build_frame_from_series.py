import pandas as pd

series_a = pd.Series([90,80,70,60,75,77])
series_b = pd.Series(['A','B','C','D','E','F'])
big_frame = pd.DataFrame({
    'Student':series_b,
    'Grades': series_a
})

print(big_frame)