import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main() -> None:
    file_name = "Public Datasets\\covid_19_clean_complete.csv.zip"
    df = pd.read_csv(file_name, compression='zip')
    df['Country/Region'] = df['Country/Region'].replace('Mainland China', 'China')
    df['Country/Region'] = df['Country/Region'].replace('US', 'United States')
    df['Country/Region'] = df['Country/Region'].replace('United Kingdom', 'UK')
    #we faced an issue with the different country names leading to duplicates in the chart
    deaths_country = df.groupby('Country/Region')['Deaths'].sum().sort_values(ascending=False).head(50)
    plt.figure(figsize=(20,6))
    sns.barplot(x=deaths_country.index, y=deaths_country.values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.xticks(rotation=45, ha='right')
    plt.title("Top 50 Countries by COVID Deaths")
    #we limited the number of countries to 50 to get rid of the issue of overcrowding 
    #Furthermore, we only focused on the top 50 countries to get the most affected countries by deaths
    plt.xlabel("Country/Region")
    plt.ylabel("Total Deaths")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()