import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() -> None:
    file_name = "Public Datasets\\covid_19_clean_complete.csv.zip"
    df = pd.read_csv(file_name, compression='zip')
    df['Date'] = pd.to_datetime(df['Date'])
    plt.figure(figsize=(12,6))
    plt.title("Recovered vs Dates")
    plt.xlabel("Date")
    plt.ylabel("Number of Recovered Cases")
    plt.ticklabel_format(style='plain', axis='y')
    grouped_recovered = df.groupby(df['Date'].dt.to_period('M'))['Recovered'].sum()
    grouped_recovered.index = grouped_recovered.index.strftime('%Y-%m')
    plt.plot(range(len(grouped_recovered)), grouped_recovered.values)
    plt.xticks(range(0, len(grouped_recovered), 1), grouped_recovered.index[::1], fontsize=7, rotation=90, fontname="Times New Roman")
    plt.yticks(fontsize=10, fontname="Times New Roman")
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()