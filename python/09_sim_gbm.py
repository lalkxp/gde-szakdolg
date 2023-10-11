#!/usr/bin/env python3

import montecarlo as mc


def main():
    # Generate random geometric brownian motion
    random_daily_return = mc.logic.simulation.geometric_browian_motion(
        number_of_steps=1000, mu=0.0001, sigma=0.015)

    # Plot the chart
    random_daily = mc.data.ticker.daily_from_daily_return(random_daily_return, 100)
    random_df = mc.data.ticker.add_time_to_ts(random_daily)

    mc.view.chart.plot_chart(
        random_df,
        "Geometric brownian motion"
    )


if __name__ == '__main__':
    main()
