import polars as pl

df_3a = pl.read_csv('../data-raw/data3a.csv', infer_schema_length=100_000) 
df_3b = pl.read_csv('../data-raw/data3b.csv', infer_schema_length=100_000) 

# Rename the first column to time_measurement_weeks, second to site_id, third to plot_id
# keep the last two headers
df_3a = df_3a.rename({"time_measurement":"time_measurement_weeks","site":"site_id","plot":"plot_id"})
df_3b = df_3b.rename({"time_measurement":"time_measurement_weeks","site":"site_id","plot":"plot_id"})

df_3a.write_csv('../data-raw/data3a.csv')
df_3b.write_csv('../data-raw/data3b.csv')

# Create a concatenated csv with the values from 3a and 3b
df_both = pl.concat([df_3a, df_3b], how="align")

df_both.write_csv('../data-raw/data-concat.csv')

df_both.glimpse()
