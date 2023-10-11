#!/usr/bin/env python3

import montecarlo as mc


def main():
    # Get input parameters
    stock_ticker = mc.helper.input_str("Stock", "SPY")

    start_year = mc.helper.input_int("Start year", 2020)
    start_month = mc.helper.input_int("Start month", 1)
    start_day = mc.helper.input_int("Start day", 1)

    end_year = mc.helper.input_int("End year", 2023)
    end_month = mc.helper.input_int("End month", 1)
    end_day = mc.helper.input_int("End day", 1)


    # Download ticker data
    spy = mc.data.ticker.download_ticker(
        ticker = stock_ticker,
        startdate = (start_year, start_month, start_day),
        enddate = (end_year, end_month, end_day)
    )
    spy_close_return = mc.data.ticker.get_ticker_close_return(spy)


    # Run the normality test
    mc.logic.normality.test(spy_close_return)


if __name__ == '__main__':
    main()
