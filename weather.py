import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("weather.csv")

data = pd.DataFrame(df)

df.dropna(inplace = True)
an = df.describe().T

profile = ProfileReport(df)
profile.to_file(output_file="weather.html")