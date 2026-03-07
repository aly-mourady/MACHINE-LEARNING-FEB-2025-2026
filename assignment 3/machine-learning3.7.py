import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() -> None:
    file_name = "Public Datasets\\covid_19_clean_complete.csv.zip"
    df = pd.read_csv(file_name, compression='zip')
    plt.figure(figsize=(8,6))
    plt.scatter(df['Active'], df['Deaths'], marker='o', alpha = 0.7, edgecolor = 'w')
    plt.xlabel('Number of Active', fontsize=14, fontweight = 'bold')
    plt.ylabel('Number of Death',fontsize=14, fontweight = 'bold')
    plt.xticks(fontsize=12, fontweight = 'bold')
    plt.yticks(fontsize=12, fontweight = 'bold')
    plt.title('Active v.s Deaths', fontsize=16, fontweight = 'bold')
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()