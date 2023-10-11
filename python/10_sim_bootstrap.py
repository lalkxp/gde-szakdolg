#!/usr/bin/env python3

import montecarlo as mc


def main():
    # Get input parameters
    ticker = mc.helper.input_str("Index", "SPY")

    start_year = mc.helper.input_int("Start year", 2022)
    start_month = mc.helper.input_int("Start month", 1)
    start_day = mc.helper.input_int("Start day", 1)

    end_year = mc.helper.input_int("End year", 2023)
    end_month = mc.helper.input_int("End month", 1)
    end_day = mc.helper.input_int("End day", 1)

    number_of_steps = mc.helper.input_int("Number of steps", 250)


    # Download ticker data
    index = mc.data.ticker.download_ticker(
        ticker = ticker,
        startdate = (start_year, start_month, start_day),
        enddate = (end_year, end_month, end_day)
    )
    index_close_return = mc.data.ticker.get_ticker_close_return(index)


    # Generate random vector with bootstrap method
    random_daily_return = mc.logic.simulation.bootstrap_vector(
        index_close_return, number_of_steps)


    # Plot the chart
    last_value = index["Close"].iloc[-1]
    random_daily = mc.data.ticker.daily_from_daily_return(random_daily_return, last_value)
    random_df = mc.data.ticker.add_time_to_ts(random_daily)

    mc.view.chart.plot_chart(
        random_df,
        "Bootstrap"
    )


if __name__ == '__main__':
    main()
