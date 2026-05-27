# pip install pandas

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    csv_path = Path(r"/home/aa/kuBig2026/python_example/data")
    df = pd.read_csv(csv_path / 'ta_20260527093811.csv')
    df.info()
    # plt.figure(figsize=(12,6))
    plt.plot(df['timestamp'], df['average'])
    plt.show()


if __name__ == "__main__":
    main()
