import numpy as np
import matplotlib.pyplot as plt

points = np.array(
    [17.01139450,
    224.32106018,
     37.87823486,
    217.28157043,
     57.88871384,
    212.70600891,
     75.98481750,
    210.45985413,
     90.31930542,
    211.22506714,
    102.57107544,
    213.35574341,
    112.32439423,
    216.28579712,
    117.35403442,
    217.94039917,
    118.36590576,
    218.13363647,
    115.74873352,
    216.84901428,
    109.20302582,
    216.06253052,
     99.68204498,
    215.55908203,
     86.41867065,
    216.43103027,
     71.71394348,
    218.14942932,
     54.68348312,
    220.48808289,
     37.25648499,
    223.12141418,
     17.42551041,
    225.37916565],
    dtype=np.float32
).reshape((17, 2))

plt.plot(points[:, 0], points[:, 1])
plt.show()