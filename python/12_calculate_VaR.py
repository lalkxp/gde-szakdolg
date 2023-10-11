#!/usr/bin/env python3

import montecarlo as mc
import scipy.stats as stats
import pandas as pd


def calculate_VaR(
        header : str,
        index_close_return : pd.Series,
        confidence_level : float
):
    '''
    Calculate VaR, CVaR and print the result
    '''
    # Calculate VaR and CVaR
    VaR, CVaR_plus, CVaR_minus, CVaR = mc.logic.risk.VaR(
        index_close_return,
        confidence_level
    )

    # Print summary
    print("-----------")
    print(header)
    print("VaR: %.4f" % VaR)
    print("CVaR plus: %.4f" % CVaR_plus)
    print("CVaR minus: %.4f" % CVaR_minus)
    print("CVaR: %.4f" % CVaR)
    print("")



def main():
    # Get input parameters
    print("")

    ticker = mc.helper.input_str("Index", "SPY")

    start_year = mc.helper.input_int("Start year", 2022)
    start_month = mc.helper.input_int("Start month", 1)
    start_day = mc.helper.input_int("Start day", 1)

    end_year = mc.helper.input_int("End year", 2023)
    end_month = mc.helper.input_int("End month", 1)
    end_day = mc.helper.input_int("End day", 1)

    confidence_level = mc.helper.input_float("Confidence level", 95.0)

    number_of_steps = mc.helper.input_int("Number of steps", 1000)

    print("")


    # Download ticker data
    index = mc.data.ticker.download_ticker(
        ticker = ticker,
        startdate = (start_year, start_month, start_day),
        enddate = (end_year, end_month, end_day)
    )
    index_close_return = mc.data.ticker.get_ticker_close_return(index)


    # Calculate VaR with historic method
    calculate_VaR("Historic method", index_close_return, confidence_level)


    # Calculate VaR with MC method and GBM
    mu, sigma = stats.norm.fit(index_close_return)
    random_daily_return = mc.logic.simulation.geometric_browian_motion(
        number_of_steps, mu, sigma)

    calculate_VaR("MC method and geometric Brownian motion",
                  random_daily_return, confidence_level)


    # Calculate VaR with MC method and Bootstrap
    mu, sigma = stats.norm.fit(index_close_return)
    random_daily_return = mc.logic.simulation.bootstrap_vector(
        index_close_return, number_of_steps)

    calculate_VaR("MC method and Bootstrap",
                  random_daily_return, confidence_level)


if __name__ == '__main__':
    main()
