import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() -> None:
    file_name = "Public Datasets\\covid_19_clean_complete.csv.zip"
    df = pd.read_csv(file_name, compression ='zip')
    sns.countplot(x='WHO Region', data=df)
    plt.show()

if __name__ == "__main__":
    main()