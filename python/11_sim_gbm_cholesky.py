#!/usr/bin/env python3

import montecarlo as mc
import matplotlib.pyplot as plt


def main():
    # Generate two correlated random geometric brownian motion
    random_sample1, random_sample2 = mc.logic.simulation.geometric_browian_motion_cholesky(
        number_of_steps=1000,
        mu1=0.0001, sigma1=0.015,
        mu2=0.0001, sigma2=0.015,
        covariance=0.8)


    # Plot the chart
    random_daily1 = mc.data.ticker.daily_from_daily_return(random_sample1, 100)
    random_df1 = mc.data.ticker.add_time_to_ts(random_daily1)

    random_daily2 = mc.data.ticker.daily_from_daily_return(random_sample2, 100)
    random_df2 = mc.data.ticker.add_time_to_ts(random_daily2)

    mc.view.chart.plot_chart2(
        random_df1,
        "first",
        random_df2,
        "secod"
    )


if __name__ == '__main__':
    main()
