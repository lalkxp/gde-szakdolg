#!/bin/usr/env python3

import numpy as np
import pandas as pd
import montecarlo as mc


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
    sim_size = mc.helper.input_int("Number of steps", 1000)
    res = mc_simulation(sim_size)
    print(res)


if __name__ == "__main__":
    main()
