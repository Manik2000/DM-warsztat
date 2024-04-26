import os

import numpy as np


if __name__ == "__main__":
    N = 2000

    np.random.seed(30_08_2000)
    values = np.random.multivariate_normal(
        mean=[0, 2, 4, -1, 5], 
        cov=[[1, 0, 0.5, 0.9, 0.2],
             [0, 1.5, -0.7, 0.45, 0],
             [0.5, -0.7, 2.1, 0.3, 0.1],
             [0.9, 0.45, 0.3, 1.5, 0.6],
             [0.2, 0, 0.1, 0.6, 1]],
        size=N
    )
    
    # get Y = X1 + 2*X2 + 3*X3 - X4 + 4*X5
    Y = values[:, 0] + 2 * values[:, 1] + 3 * values[:, 2] - values[:, 3] + \
        4 * values[:, 4] + np.random.normal(0, 0.5, N)
    np.savez_compressed(os.path.join('data', 'linear.npz'), X=values, Y=Y)


    # get Y1 as nonlinear function of X1, X2, X3, X4, X5
    Y1 = values[:, 0] * values[:, 1] + values[:, 2]**2 * 3 * np.sin(values[:, 3]) + \
         np.log(np.exp(values[:, 4]) + 2) + np.random.normal(0, 0.5, N)
    np.savez_compressed(os.path.join('data', 'nonlinear.npz'), X=values, Y=Y1)
