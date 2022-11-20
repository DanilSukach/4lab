import pandas as pd


def data_frame(file):
    df = pd.read_csv(file, sep=";",names=["absolute path","relative path","class name"])
    print(df)
    df = df.drop(["relative path"], axis=1)
    print(df)
  


def main():
    data_frame("data.csv")


if __name__ == "__main__":
    main()
