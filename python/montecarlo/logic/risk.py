#!/usr/bin/env python3

import pandas as pd


def VaR(
        close_return : pd.Series,
        confidence_level : float
):
    # Sort daily return
    close_return.sort_values(ascending=False, inplace=True)

    # Calculate VaR
    number_of_days = close_return.size
    possibility_of_one_day = 1/number_of_days
    index_of_VaR = (confidence_level/100) // (possibility_of_one_day) - 1
    index_of_VaR = int(index_of_VaR)

    VaR = close_return.iloc[index_of_VaR] * (-100)

    # Calculate CVar plus
    sum1 = 0.0
    sum2 = 0.0
    for i in range(index_of_VaR+1, number_of_days):
        sum1 += (close_return.iloc[i] * possibility_of_one_day)
        sum2 += possibility_of_one_day
    CVaR_plus = (sum1 / sum2) * (-100)

    # Calculate CVar minus
    sum1 += (close_return.iloc[index_of_VaR] * possibility_of_one_day)
    sum2 += possibility_of_one_day
    CVaR_minus = (sum1 / sum2) * (-100)

    # Calculate lambda
    x = (index_of_VaR + 2) * possibility_of_one_day
    lambdaa = (x - confidence_level/100.0) / (1 - confidence_level/100.0)

    # Calculate CVar
    CVaR =  lambdaa * VaR + (1-lambdaa) * CVaR_plus
    return (VaR, CVaR_plus, CVaR_minus, CVaR)
