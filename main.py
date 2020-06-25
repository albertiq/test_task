from approx.approx_func import approx_function
import numpy as np


def main():
    x = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 66])
    y = np.array([4.88, 4.73, 4.66, 4.61, 4.52, 4.35, 4.10, 3.74, 3.28, 2.73, 2.11, 1.45, 0.77, 0])
    approx_function(x, y)


if __name__ == "__main__":
    main()
