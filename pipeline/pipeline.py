import sys
import pandas as pd

print('arguments', sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "shodaqoh": [3000, 4000]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet")

print(f'month={month}')