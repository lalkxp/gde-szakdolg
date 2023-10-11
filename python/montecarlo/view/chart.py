#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def plot_chart(
        ticker : pd.DataFrame,
        ticker_label : str,
        logscale=False
):
    '''
    Plots a chart. X is Date, y is Close.
    '''
    ticker.plot(
        x = 'Date',
        y = 'Close',
        label = ticker_label,
        figsize = (14, 6)
    )
    if (logscale):
        plt.yscale("log")
    plt.xlabel('Time')
    plt.ylabel('Price [$]')
    plt.title(ticker_label + ' chart')
    plt.grid()
    plt.show()


def plot_chart_with_volume(
        ticker : pd.DataFrame,
        ticker_label : str
):
    ticker.plot(
        x = 'Date',
        title = ticker_label + ' chart',
        y = ['Close', 'Volume'],
        subplots = True,
        grid = True,
        figsize = (14, 6)
    )
    plt.show()


def plot_chart2(
        ticker1 : pd.DataFrame,
        ticker1_label : str,
        ticker2 : pd.DataFrame,
        ticker2_label : str
):
    '''
    Plots a chart. X is Date, y is Close.
    '''
    plt.subplot(2, 1, 1)
    plt.plot(ticker1['Date'], ticker1['Close'])
    plt.xlabel('Time')
    plt.ylabel('Price [$]')
    plt.title(ticker1_label + ' chart')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(ticker2['Date'], ticker2['Close'])
    plt.xlabel('Time')
    plt.ylabel('Price [$]')
    plt.title(ticker2_label + ' chart')
    plt.grid()

    plt.show()
