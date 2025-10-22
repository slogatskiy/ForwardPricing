"""
Data helpers (no network yet):

- read_forwards_csv(path) -> DataFrame
    Expected columns:
      as_of (YYYY-MM-DD), symbol, spot, future, expiry (YYYY-MM-DD),
      q (annual, cont), r_assumed (annual, cont), costs_bps (float)
- add_year_fraction(df) -> DataFrame
    Compute T (years) from as_of to expiry using ACT/365.
- validate_columns(df) -> None
    Raise a clear error if required columns are missing.
"""
