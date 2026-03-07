# /// machine-learning1
# requires-python = ">=X.XX" TODO: Update this to the minimum Python version you want to support
# dependencies = [
#   TODO: Add any dependencies your script requires
# ]
# ///

# TODO: Update the main function to your needs or remove it.

import pandas as pd
import numpy as np
def main() -> None:
    file_name = "Public Datasets\\covid_19_clean_complete.csv.zip"
    df = pd.read_csv(file_name, compression='zip')
    #our objective is to predict the number of deaths in the coming days,Y(output), based on the number of confirmed cases,X(input)
    print("The number of null values in the dataset is: ", df.isnull().sum())
    #as we can see in the previous print, there are 34404 null values in the Province/State column.
    #the first issue we face is the amount of null values in the dataset which may affect our estimate number of deaths
    #for that reason, we will remove Province/State as it includes half the null values of the dataset
    df.drop("Province/State", inplace=True, axis=1)
    #the second issue is the date column, as it is a string (the wrong data type for dates)
    df["Date"] = pd.to_datetime(df["Date"])
    df.info()
    
if __name__ == "__main__":
    main()
