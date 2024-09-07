import matplotlib.pyplot as plt
import pandas as pd


def train_plot() -> None:
    df = pd.read_csv("standardized.csv")

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


def standardize(df, columns) -> pd.DataFrame:
    for column in columns:
        x = df[column]
        df.loc[:, column] = (x - x.mean()) / x.std()
    return df


def main() -> None:
    df = pd.read_csv("Train_knight.csv")

    column_to_scale = list(df.columns)
    if "knight" in column_to_scale:
        column_to_scale.remove("knight")

    scaled_data = standardize(df, column_to_scale)
    scaled_data.to_csv("standardized.csv")
    train_plot()


if __name__ == "__main__":
    main()
