import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main() -> None:
    from urllib.request import urlretrieve
    iris = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    urlretrieve(iris)
    df = pd.read_csv(iris, sep=',')
    attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    df.columns = attributes
    #importing the dataset and assigning column names to it
    a1 = np.array([df.sepal_length.mean(), df.sepal_width.mean(), df.petal_length.mean(), df.petal_width.mean()])
    a2 = np.array([df.sepal_length.std(), df.sepal_width.std(), df.petal_length.std(), df.petal_width.std()])
    a3 = np.array([df.sepal_length.median(), df.sepal_width.median(), df.petal_length.median(), df.petal_width.median()])
    #calculating mean, standard deviation and median of the numerical data columns and storing them in arrays
    filtered_df = df[df["sepal_length"] == 5.0]
    #filtering the dataset to get the rows with sepal length of 5.0
    grouped_df = filtered_df.groupby("species")
    #grouping the filtered dataset by species
    sns.barplot(x="species", y="sepal_length", data=grouped_df.mean().reset_index())
    #plotting a bar graph to show the mean sepal length for each species with sepal length of 5.0
    plt.show()
    filtered_df.to_csv("filtered_iris.csv", index=False)
    #saving the filtered dataset to a csv file
    filtered2_df = df[df["sepal_width"] > 3.0]
    #filtering the dataset to get the rows with sepal width greater than 3.0
    a4  = filtered2_df["petal_length"].mean()
    #average petal length for all rows with sepal width greater than 3.0
    filtered2_df.sort_values("petal_length", ascending=False)
    #ordering the filtered dataset in descending order according to petal length
    filtered2_df.iloc[:, [0, 1, 2]]
    filtered2_df.loc[10:21, ["sepal_length", "species"]]
    #selecting the first three columns of the filtered dataset and then selecting rows from index 10 to 21 and columns sepal length and species
    a5 = np.array(filtered2_df["sepal_length"])
    a6 = a5.var()
    #calculating the variance of sepal length for all rows with sepal width greater than 3.0
    df["petal_size"] = np.where(df["petal_width"] > 3.0, "large", "small")
    #creating a new column petal size and assigning values large or small based on petal width
    df.to_csv("modified_iris.csv", index=False)
    #saving the modified dataset to a csv file
    print("Mean of numerical columns:", a1)
    print("Standard deviation of numerical columns:", a2)
    print("Median of numerical columns:", a3)
    print("Average petal length for sepal width > 3.0:", a4)
    print("Variance of sepal length for sepal width > 3.0:", a6)

if __name__ == "__main__":
    main()
