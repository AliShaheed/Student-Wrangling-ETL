import pandas as pd

def extract(file):
    data = pd.read_csv(file)
    return data
    

file = "al_results_2020.csv"
df = extract(file)

print(df.head())