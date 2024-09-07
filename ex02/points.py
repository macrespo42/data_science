import matplotlib.pyplot as plt
import pandas as pd


def test_plot() -> None:
    df = pd.read_csv("Test_knight.csv")

    plt.scatter(df["Empowered"], df["Stims"], label="Knight", color="green", alpha=0.3)
    plt.legend()
    plt.show()

    plt.scatter(
        df["Survival"], df["Deflection"], label="Knight", color="green", alpha=0.3
    )
    plt.legend()
    plt.show()


def train_plot() -> None:
    df = pd.read_csv("Train_knight.csv")

    jedi = df.loc[df["knight"] == "Jedi"]
    sith = df.loc[df["knight"] == "Sith"]

    plt.scatter(
        sith["Survival"],
        sith["Deflection"],
        label="sith",
        color="lightcoral",
        alpha=0.3,
    )

    plt.scatter(
        jedi["Survival"], jedi["Deflection"], label="jedi", color="blue", alpha=0.3
    )

    plt.legend()
    plt.show()

    plt.scatter(
        sith["Empowered"],
        sith["Stims"],
        label="sith",
        color="lightcoral",
        alpha=0.3,
    )

    plt.scatter(jedi["Empowered"], jedi["Stims"], label="jedi", color="blue", alpha=0.3)

    plt.legend()
    plt.show()


def main() -> None:
    test_plot()
    train_plot()


if __name__ == "__main__":
    main()
