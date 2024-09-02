import pandas as pd

def load_iris_dataset():
    train_df = pd.read_csv("./data/iris_train.csv")
    val_df = pd.read_csv("./data/iris_val.csv")
    x_train = train_df.drop(["label"], axis=1)
    y_train = train_df["label"]
    
    