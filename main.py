import pandas as pd

CSV_PATH = "data/data.csv"


def main():
    df = pd.read_csv(CSV_PATH)
    print(df.head())


if __name__ == "__main__":
    main()
