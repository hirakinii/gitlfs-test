"""main.py
"""

import numpy as np
import os
import pandas as pd


def main():
    # test1: random int with .dat
    shape = (1024, 1024)
    data = np.random.randint(0, 10, shape, dtype=int)
    dstpath = os.path.join(os.path.dirname(__file__), f"../output/test.dat")
    np.savetxt(dstpath, data, delimiter=",", fmt="%d")

    # test2: random int with .csv and header
    shape = (1024*256, 3)
    data = np.random.randint(0, 10, shape, dtype=int)
    columns = ["x", "y", "z"]
    df = pd.DataFrame(data, columns=columns)
    dstpath = os.path.join(os.path.dirname(__file__), f"../output/test.csv")
    df.to_csv(dstpath, index=None)


if __name__ == "__main__":
    main()
