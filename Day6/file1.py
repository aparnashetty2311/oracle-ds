import pandas as pd
import numpy as np

data=pd.df = pd.read_json("emp.json")
print(data.head(5))

print("=====================")
s = pd.Series([10, 20, 30, 40], name="Numbers")
print("Series:\n", s)

# Convert Series to DataFrame
df = s.to_frame()
print("\nDataFrame:\n", df)
print("===========================")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}
df = pd.DataFrame(data)

print("DataFrame:\n", df)

# Convert one column into Series
age_series = df["Age"]
print("\nSeries (Age column):\n", age_series)
