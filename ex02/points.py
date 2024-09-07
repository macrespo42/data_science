import matplotlib.pyplot as plt
import pandas as pd


def test_plot() -> None:
    df = pd.read_csv("Test_knight.csv")

    plt.scatter(df["Empowered"], df["Stims"], label="Knight", color="green", alpha=0.3)
    plt.scatter(
        df["Survival"], df["Deflection"], label="Knight", color="green", alpha=0.3
    )
    plt.legend()
    plt.show()

    plt.scatter(
        df["Survival"], df["Deflection"], label="Knight", color="green", alpha=0.3
    )
    plt.legend()
    plt.show()


def main() -> None:
    test_plot()


if __name__ == "__main__":
    main()
