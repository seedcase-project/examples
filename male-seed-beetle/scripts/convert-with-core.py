import polars as pl

df = pl.read_csv('../data-raw/data.csv')

#Test that it works - remove later!
first_row = df.head(1)
print(first_row)
