"""
Comparison pipeline:

- prepare(df):
    validate columns, add T (years)

- compute_theory(df):
    add column F_th using forward_theoretical_equity(S0, r, q, T)

- compute_implieds(df):
    add columns r_star and q_star from observed F_mkt and S0

- flag_arbitrage(df):
    add columns carry, reverse, inside_band using arbitrage_band_flags()

- save_results(df, path):
    write a tidy results.csv to data/processed/ (later)
"""
