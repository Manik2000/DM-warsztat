import os

import numpy as np
from scipy.stats import t as t_dist, poisson



def get_number_of_anomalies(anomaly_rate: float=3):
    """
    Get the number of anomalies in the time series by sampling Poisson distribution.
    """
    number_of_anomalies = poisson(anomaly_rate).rvs(size=1)[0]
    while number_of_anomalies == 0:
        number_of_anomalies = poisson(anomaly_rate).rvs(size=1)[0]
    return number_of_anomalies


def autoregressive_trajectory(N: int, anomaly: bool=False):
    """
    Generate a time series with autoregressive dynamics.
    """
    noise = np.random.standard_normal(N)
    values = np.zeros(N)
    values[0] = noise[0]
    values[1] = 0.5 * values[0] + noise[1]
    for i in range(2, N):
        values[i] = 0.5 * values[i - 1] - 0.7 * values[i-2] + noise[i]
    if anomaly:
        number_of_anomalies = get_number_of_anomalies()
        random_indices = np.random.choice(np.arange(N), number_of_anomalies, replace=False)
        values[random_indices] = values[random_indices] + t_dist(0.1).rvs(size=number_of_anomalies)
    return values


if __name__ == "__main__":
    normal_sample_size = 2000

    np.random.seed(30_08_2000)
    values = np.random.multivariate_normal(
        mean=[0, 2, 4, -1, 5], 
        cov=[[1, 0, 0.5, 0.9, 0.2],
             [0, 1.5, -0.7, 0.45, 0],
             [0.5, -0.7, 2.1, 0.3, 0.1],
             [0.9, 0.45, 0.3, 1.5, 0.6],
             [0.2, 0, 0.1, 0.6, 1]],
        size=normal_sample_size
    )
    
    # get Y = X1 + 2*X2 + 3*X3 - X4 + 4*X5
    Y = values[:, 0] + 2 * values[:, 1] + 3 * values[:, 2] - values[:, 3] + \
        4 * values[:, 4] + np.random.normal(0, 0.5, normal_sample_size)
    np.savez_compressed(os.path.join('data', 'linear.npz'), X=values, Y=Y)  

    # get Y1 as nonlinear function of X1, X2, X3, X4, X5
    Y1 = values[:, 0] * values[:, 1] + values[:, 2]**2 * 3 * np.sin(values[:, 3]) + \
         np.log(np.exp(values[:, 4]) + 2) + np.random.normal(0, 0.5, normal_sample_size)
    np.savez_compressed(os.path.join('data', 'nonlinear.npz'), X=values, Y=Y1)

    # autoregressive time series
    N = 200
    M = 500 

    X = np.zeros((N, 2 * M))
    for i in range(M):
        X[:, i] = autoregressive_trajectory(N)
    for i in range(M, 2 * M):
        X[:, i] = autoregressive_trajectory(N, anomaly=True)
    labels = np.concatenate([np.zeros(M), np.ones(M)])
    np.savez_compressed(os.path.join('data', 'time_series.npz'), X=X, labels=labels)
