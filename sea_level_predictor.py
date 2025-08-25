import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data")

    # First line of best fit (1880–2050)
    slope1, intercept1, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred1 = range(1880, 2051)
    y_pred1 = intercept1 + slope1 * pd.Series(x_pred1)
    plt.plot(x_pred1, y_pred1, 'r', label="Best fit (1880-2014)")

    # Second line of best fit (2000–2050)
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred2 = range(2000, 2051)
    y_pred2 = intercept2 + slope2 * pd.Series(x_pred2)
    plt.plot(x_pred2, y_pred2, 'g', label="Best fit (2000-2014)")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()
