#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


def test(
        stock_close_return : pd.Series
):
    mu, sigma = stats.norm.fit(stock_close_return)
    print("mu: ", mu)
    print("sigma: ", sigma)

    skewness = stats.skew(
        stock_close_return
    )
    print("skewness: ", skewness)

    kurtosis = stats.kurtosis(
        stock_close_return
    )
    print("kurtosis: ", kurtosis)


    stock_close_return.plot.hist(
        bins = 100,
        density=True
    )

    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    
    plt.plot(x, p, 'k')
    plt.show()


    # Plot the Q-Q chart
    stats.probplot(stock_close_return,
                   dist = stats.norm,
                   sparams = (mu, sigma),
                   plot = plt)
    plt.show()


    # Shapiro-Wilk test
    shapiro_wilk_test = stats.shapiro(
        x = stock_close_return
    )
    print( shapiro_wilk_test )


    # Anderson-Darling test
    anderson_darling_test = stats.anderson(
        x = stock_close_return,
        dist = 'norm'
    )
    print( anderson_darling_test )


    # Kolmogorov-Smirnov test
    kolmogorov_smirnov_test = stats.kstest(
           stock_close_return,
           'norm'
    )
    print( kolmogorov_smirnov_test )
