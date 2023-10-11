#!/bin/usr/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def mc_simulation(
        sim_size : int
) -> float:
    v1 = np.random.rand(sim_size)
    v2 = np.random.rand(sim_size)

    s1 = pd.Series(v1)
    s2 = pd.Series(v2)
    s3 = np.sqrt(s1 ** 2 + s2 ** 2) < 1

    return s3.sum()*4/sim_size


def mc_simulation2(
        sim_size : int
) -> float:
    v1 = np.random.rand(sim_size)
    v2 = np.random.rand(sim_size)
    v11 = np.concatenate((v1, 1-v1))
    v22 = np.concatenate((v2, 1-v2))

    s1 = pd.Series(v11)
    s2 = pd.Series(v22)
    s3 = np.sqrt(s1 ** 2 + s2 ** 2) < 1

    return s3.sum()*4/(sim_size*2)


def main():
    number_of_simulations = 10000

    mindata = 3.1
    maxdata = 3.2
    binwidth = 0.002

    sim_size = 10000


    result = []
    for i in range(number_of_simulations):
        res = mc_simulation(sim_size)
        result.append(res)
    res2 = pd.Series(result)
    var2 = res2.var()
    print( "Variance without reduction: ", var2 )

    plt.subplot(2, 1, 1)
    plt.title(str(sim_size) + " steps")
    plt.hist(res2, bins=np.arange(mindata, maxdata + binwidth, binwidth))


    result = []
    for i in range(number_of_simulations):
        res = mc_simulation2(sim_size // 2)
        result.append(res)
    res3 = pd.Series(result)
    var3 = res3.var()
    print( "Variance with reduction: ", var3 )

    print( "Reduction in percent : ", (var2 - var3) / var2 * 100, "%" )


    plt.subplot(2, 1, 2)
    plt.title(str(sim_size) + " steps")
    plt.hist(res3, bins=np.arange(mindata, maxdata + binwidth, binwidth))


    plt.show()


if __name__ == "__main__":
    main()
