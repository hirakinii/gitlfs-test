"""main.py
"""

import numpy as np
import os


def main():
    shape = (1024, 1024)
    data = np.random.randint(0, 10, shape, dtype=int)
    dstpath = os.path.join(os.path.dirname(__file__), "../output/test.dat")
    np.savetxt(dstpath, data, delimiter=",", fmt="%d")


if __name__ == "__main__":
    main()
