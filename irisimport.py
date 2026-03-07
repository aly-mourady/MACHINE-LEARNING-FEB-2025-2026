import pandas as pd
import numpy as np
def main() -> None:
    from urllib.request import urlretrieve
    iris = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    urlretrieve(iris)
    df = pd.read_csv(iris, sep=',')
    attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
    df.columns = attributes
    print(df.head())
if __name__ == "__main__":
    main()
