import math
import sys

from pandas import read_csv


def separate(path: str, name="data", train_percentage=80) -> None:
    if train_percentage >= 99:
        raise ValueError("The train percentage is to high")
    df = read_csv(path)
    train_stop_idx = math.floor((train_percentage / 100) * df.shape[0])

    data_train = df.iloc[0:train_stop_idx]
    data_test = df.iloc[train_stop_idx::]

    train_path = f"Training_{name}"
    test_path = f"Validation_{name}"

    try:
        data_train.to_csv(train_path)
        data_test.to_csv(test_path)
    except Exception:
        print("Cannot save split data. Try running script from the root directory")
        sys.exit(1)

    print(f"training data saved at: {train_path}")
    print(f"test data saved at: {test_path}")


def main() -> None:
    if not len(sys.argv) == 2:
        raise ValueError(
            "Please provide the dataset to separate as argument of this script"
        )
    separate(sys.argv[1])


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
