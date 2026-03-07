import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() -> None:
    file_name = "Public Datasets\\covid_19_clean_complete.csv.zip"
    df = pd.read_csv(file_name, compression='zip')
    active = df['Active'].sum()
    recovered = df['Recovered'].sum()
    deaths = df['Deaths'].sum()
    confirmed = df['Confirmed'].sum()
    labels = ['Active', 'Recovered', 'Deaths', 'Confirmed']
    values = [active, recovered, deaths, confirmed]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title("Covid-19 Cases")
    plt.ticklabel_format(style='plain', axis='y')
    plt.xlabel("Status")
    plt.ylabel("Number of Cases")
    plt.show()

if __name__ == "__main__":
    main()