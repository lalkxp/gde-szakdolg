#!/bin/usr/env python3

import math
import time
import numpy as np
import pandas as pd
import montecarlo as mc


def mc_simulation(
        sim_size : int
):
    v1 = np.random.rand(sim_size)
    v2 = np.random.rand(sim_size)

    s1 = pd.Series(v1)
    s2 = pd.Series(v2)
    s3 = np.sqrt(s1 ** 2 + s2 ** 2) < 1

    return s3.sum()*4/sim_size
    

def main():
    sim_size = mc.helper.input_int("Number of steps", 1000)

    start_time = time.time()

    res1 = mc_simulation(sim_size)
    res2 = mc_simulation(sim_size)
    res3 = mc_simulation(sim_size)
    res = (res1+res2+res3) / 3.0
    err = 100 * abs(res - math.pi) / math.pi

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("#   : %d" % sim_size)
    print("1.  : %.4f" % res1)
    print("2.  : %.4f" % res2)
    print("3.  : %.4f" % res3)
    print("avg.: %.4f" % res)
    print("err.: %.4f %%" % err)
    print("time: %.4f ms" % elapsed_time)


if __name__ == "__main__":
    main()
