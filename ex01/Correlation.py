import numpy as np
import pandas as pd


def main() -> None:
    df = pd.read_csv("Train_knight.csv")

    df["knight"] = [1 if jedi == "Jedi" else 0 for jedi in df["knight"]]
    knight = df["knight"]

    for column in df.columns:
        coef = np.corrcoef(df[column], knight)[0, 1]
        print(f"{column}    {coef:.6f}")


if __name__ == "__main__":
    main()
