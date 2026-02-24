import pandas as pd
import matplotlib.pyplot as plt

def main():
    dataset = pd.read_csv("../../titanic.csv")
    print(dataset.describe())
    Rose = dataset[(dataset["Age"] < 20) & (dataset["Age"] > 16) & (dataset["Pclass"] == 1) & (dataset["Sex"] == "female")]["Survived"].mean()
    print(Rose)
    dataset.Age.hist()
    plt.show()

if __name__ == '__main__':
    main()
