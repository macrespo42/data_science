import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    df = pd.read_csv("Test_knight.csv")

    num_columns = df.shape[1]

    plt.figure(figsize=(30, 25))

    for i, column in enumerate(df.columns):
        plt.subplot((num_columns // 5) + 1, 5, i + 5)
        plt.hist(df[column], color="green", alpha=0.3)
        plt.title(column)

    plt.tight_layout(pad=2.0)
    plt.show()


if __name__ == "__main__":
    main()
