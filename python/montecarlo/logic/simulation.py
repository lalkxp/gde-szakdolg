#!/usr/bin/env python3

import numpy as np
import pandas as pd

import math


def geometric_browian_motion(
        number_of_steps : int,
        mu : float,
        sigma : float,
        dt=1
) -> pd.Series:
    # Generate epsilon as standard normal distribution random number (mu=0, sigma=1)
    epsilon = np.random.normal(0, 1, number_of_steps)

    # Calculate the stock price changes
    ret = mu * dt + sigma * epsilon * math.sqrt(dt)

    return pd.Series(ret)


def geometric_browian_motion_cholesky(
        number_of_steps : int,
        mu1 : float,
        sigma1 : float,
        mu2 : float,
        sigma2 : float,
        covariance : float,
        dt=1
) -> pd.DataFrame:
    # Generate epsilon as standard normal distribution random number (mu=0, sigma=1)
    epsilon1 = np.random.normal(0, 1, number_of_steps)
    epsilon2 = np.random.normal(0, 1, number_of_steps)

    Z1 = epsilon1
    Z2 = covariance * epsilon1 + math.sqrt(1 - covariance ** 2) * epsilon2

    # Calculate the stock price changes
    ret1 = mu1 * dt + sigma1 * Z1 * math.sqrt(dt)
    ret2 = mu2 * dt + sigma2 * Z2 * math.sqrt(dt)

    return (pd.Series(ret1), pd.Series(ret2))


def bootstrap_vector(
        sample_vector : pd.Series,
        number_of_sample : int
) -> pd.Series:
    bootstrap_values = sample_vector.sample(n=number_of_sample, replace=True)
    return pd.Series(bootstrap_values)
