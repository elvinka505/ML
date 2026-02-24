import pandas as pd
import matplotlib.pyplot as plt

def main():
    dataset = pd.read_csv("titanic.csv")
    print(dataset.describe())
    Jack = dataset[(dataset["Age"] < 20) & (dataset["Age"] > 16) & (dataset["Pclass"] == 3) & (dataset["Sex"] == "male")]["Survived"].mean()
    print(Jack)
    dataset.Age.hist()
    plt.show()

if __name__ == '__main__':
    main()
