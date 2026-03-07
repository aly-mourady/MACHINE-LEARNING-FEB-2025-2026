import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main() -> None:
    file_name = "Public Datasets\\covid_19_clean_complete.csv.zip"
    df = pd.read_csv(file_name, compression='zip')
    df['Date'] = pd.to_datetime(df['Date'])
    groupeddeaths = df.groupby(df['Date'].dt.to_period('M'))['Deaths'].sum()
    groupeddeaths.index = groupeddeaths.index.strftime('%Y-%m')
    plt.figure(figsize=(20,6))
    plt.title("Number of deaths vs date")
    plt.xlabel("Date")
    plt.ylabel("Number of Deaths")
    plt.ticklabel_format(style='plain', axis='y')
    plt.plot(range(len(groupeddeaths)), groupeddeaths.values)
    plt.xticks(range(0, len(groupeddeaths), 1), groupeddeaths.index[::1], fontsize=7, rotation=90, fontname="Times New Roman")
    plt.yticks(fontsize=10, fontname="Times New Roman")
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()