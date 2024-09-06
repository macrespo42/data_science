import matplotlib.pyplot as plt
import pandas as pd


def test_plot() -> None:
    df = pd.read_csv("Test_knight.csv")

    plt.figure(figsize=(20, 15))

    for i, column in enumerate(df.columns):
        plt.subplot((df.shape[1] // 5) + 1, 5, i + 5)
        plt.hist(df[column], color="green", alpha=0.3)
        plt.title(column)

    plt.tight_layout(pad=2.0)
    plt.show()


def train_plot() -> None:
    df = pd.read_csv("Train_knight.csv")

    plt.figure(figsize=(20, 20))

    jedi = df.loc[df["knight"] == "Jedi"]
    sith = df.loc[df["knight"] == "Sith"]

    df = df.drop(["knight"], axis=1)

    for i, column in enumerate(df.columns):
        plt.subplot((df.shape[1] // 5) + 1, 5, i + 5)
        plt.hist(jedi[column], label="jedi", color="blue", alpha=0.3)
        plt.hist(sith[column], label="sith", color="lightcoral", alpha=0.3)
        plt.title(column)
        plt.legend()

    plt.tight_layout(pad=4.0)
    plt.show()


def main() -> None:
    test_plot()
    train_plot()


if __name__ == "__main__":
    main()
