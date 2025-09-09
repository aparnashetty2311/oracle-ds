import pandas as pd
import numpy as np
import pandas as pd
import numpy as np

data = {
    "A": [1, 2, np.nan, 4],
    "B": [10, np.nan, 30, 40],
    "C": [np.nan, 20, 30, 40]
}

df = pd.DataFrame(data)
print(df)
#print(df.fillna(0))

df["A"] = df["A"].fillna("abc")

print(df)
#print(df.fillna(method="ffill"))

df.drop

'''
print("Original DataFrame:\n", df)
print(df.dropna())

print("==============")
print(df.dropna(axis=1))

print(df.dropna(thresh=2))

'''
