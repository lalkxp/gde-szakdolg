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
    

def main():
    number_of_simulations = 1000
    steps = [ 5000, 10000, 50000, 100000 ]

    mindata = 3.1
    maxdata = 3.2
    binwidth = 0.002

    for n in range(1, 5):
        sim_size = steps[n-1]

        result = []
        for i in range(number_of_simulations):
            res = mc_simulation(sim_size)
            result.append(res)
        res2 = pd.Series(result)

        rel_occ = []
        cumsum = 0
        for x in range(0, 11):
            res3 = res2 < (3.1 + x/100.0)
            rel_occ.append( res3.sum() - cumsum )
            cumsum = res3.sum()

        print(rel_occ)

        plt.subplot(2, 2, n)
        plt.title(str(sim_size) + " lépés")
        plt.hist(res2, bins=np.arange(mindata, maxdata + binwidth, binwidth))

    plt.show()


if __name__ == "__main__":
    main()
