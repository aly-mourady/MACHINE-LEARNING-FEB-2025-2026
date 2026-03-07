import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() -> None:
    file_name = "Public Datasets\\covid_19_clean_complete.csv.zip"
    df = pd.read_csv(file_name, compression='zip')
    grid = sns.pairplot(df, x_vars='Recovered', y_vars='Deaths', hue = "Country/Region",height=5)
    plt.show()

if __name__ == "__main__":
        main()