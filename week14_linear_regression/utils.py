import pandas as pd
from sklearn.model_selection import train_test_split


def load_house_dataset():
    df = pd.read_csv("./data/house.csv")
    X = df.drop(["price"], axis=1)
    y = df["price"]
    return train_test_split(X, y, train_size=0.8, random_state=1234) 


def load_diamonds_dataset():
    df = pd.read_csv("./data/diamonds.csv")
    X = df.drop(["price"], axis=1)
    y = df["price"]
    return train_test_split(X, y, train_size=0.8, random_state=1234) 


def load_titanic_dataset():
    df = pd.read_csv("./data/titanic.csv")
    X = df.drop(["Survived"], axis=1)
    y = df["Survived"]
    return train_test_split(X, y, train_size=0.8, random_state=1234) 


def load_penguin_dataset():
    df = pd.read_csv("./data/penguins.csv")
    df = df.dropna(subset="body_mass_g")
    X = df.drop(["body_mass_g"], axis=1)
    y = df["body_mass_g"]
    return train_test_split(X, y, train_size=0.8, random_state=1234) 


def load_weather_dataset():
    df = pd.read_csv("./data/weather.csv")
    X = df.drop(["RainTomorrow"], axis=1)
    y = df["RainTomorrow"]
    return train_test_split(X, y, train_size=0.8, random_state=1234) 
