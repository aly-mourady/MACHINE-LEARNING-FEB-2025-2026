import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() -> None:
    file_name = "Public Datasets\\covid_19_clean_complete.csv.zip"
    df = pd.read_csv(file_name, compression='zip')
    plt.figure(figsize=(14,6))
    sns.scatterplot(x='Active', y='Recovered', hue='WHO Region', size='WHO Region', data=df)
    plt.title("Active vs Recovered Cases by WHO Region")
    plt.ticklabel_format(style='plain', axis='both')
    plt.xlabel("Number of Active Cases")
    plt.ylabel("Number of Recovered Cases")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()