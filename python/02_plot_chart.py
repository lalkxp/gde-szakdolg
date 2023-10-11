#!/usr/bin/env python3

import montecarlo as mc


def main():
    # Get input parameters
    ticker = mc.helper.input_str("Index", "SPY")

    start_year = mc.helper.input_int("Start year", 2000)
    start_month = mc.helper.input_int("Start month", 1)
    start_day = mc.helper.input_int("Start day", 1)

    end_year = mc.helper.input_int("End year", 2023)
    end_month = mc.helper.input_int("End month", 1)
    end_day = mc.helper.input_int("End day", 1)


    # Download ticker data
    spy = mc.data.ticker.download_ticker(
        ticker = ticker,
        startdate = (start_year, start_month, start_day),
        enddate = (end_year, end_month, end_day)
    )


    # Plot chart
    mc.view.chart.plot_chart(
        ticker = spy,
        ticker_label = ticker,
        logscale=True
    )


if __name__ == '__main__':
    main()
