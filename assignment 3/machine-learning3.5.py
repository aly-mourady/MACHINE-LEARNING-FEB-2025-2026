import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() -> None:
    file_name = "Public Datasets\\Covid_19_clean_complete.csv.zip"
    df = pd.read_csv(file_name, compression='zip')
    active_by_country = df.groupby('Country/Region')['Active'].sum().sort_values(ascending=False).head(25)
    plt.figure(figsize=(12,6))
    sns.barplot(x=active_by_country.index, y=active_by_country.values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.ylabel("Number of Active Cases")
    plt.xlabel("Country/Region")
    plt.title("Top 25 Countries by Active Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()