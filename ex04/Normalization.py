import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def main() -> None:
    df = pd.read_csv("Train_knight.csv")

    df["knight"] = [1 if x == "Jedi" else 0 for x in df["knight"]]

    scaler = MinMaxScaler()
    df[["Survival", "Deflection"]] = scaler.fit_transform(
        df[["Survival", "Deflection"]]
    )

    jedi = df.loc[df["knight"] == 1]
    sith = df.loc[df["knight"] == 0]

    plt.scatter(
        sith["Survival"],
        sith["Deflection"],
        label="Sith",
        color="lightcoral",
        alpha=0.3,
    )

    plt.scatter(
        jedi["Survival"], jedi["Deflection"], label="Jedi", color="blue", alpha=0.3
    )

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
