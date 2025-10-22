"""
Plotting helpers (matplotlib):

- plot_forward_vs_maturity(df):
    line plot of F_mkt and F_th against T (or expiry dates)

- plot_deviation_hist(df):
    histogram of (F_mkt - F_th) or percent deviation

- plot_implied_rate_term_structure(df):
    scatter/line of implied r* versus T

All figures saved into docs/img/ with sensible filenames.
"""
