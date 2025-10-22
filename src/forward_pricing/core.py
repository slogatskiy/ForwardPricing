"""
Core formulas for equity index forwards/futures (continuous compounding).

We will implement these in Level 1–3:
  F_th = S0 * exp((r - q) * T)                # theoretical forward (equity, cont. dividend q)
  r*   = q + (1/T) * ln(F_mkt / S0)           # implied risk-free rate from observed forward
  q*   = r - (1/T) * ln(F_mkt / S0)           # implied dividend yield from observed forward

Notes:
- S0 > 0, T >= 0 (T in years; ACT/365 convention)
- r, q are annualized (continuous)
- For T very close to 0, guard against division by zero when computing implieds
"""

# def forward_theoretical_equity(S0: float, r: float, q: float, T: float) -> float:
#     """Return theoretical forward price F_th = S0 * exp((r - q) * T)."""

# def implied_r_from_forward(S0: float, F_mkt: float, q: float, T: float) -> float:
#     """Return implied risk-free rate r* = q + (1/T) * ln(F_mkt / S0)."""

# def implied_q_from_forward(S0: float, F_mkt: float, r: float, T: float) -> float:
#     """Return implied dividend yield q* = r - (1/T) * ln(F_mkt / S0)."""

# def arbitrage_band_flags(F_mkt: float, F_th: float, costs_bps: float) -> dict:
#     """
#     Decide if cash-and-carry / reverse-carry is attractive using a simple cost band.
#     costs_bps is total friction in basis points (e.g., 10 bps = 0.001).
#     Let band = costs_bps / 10000.
#     Return dict:
#       {
#         'carry': bool,          # F_mkt sufficiently above F_th (short future, long spot)
#         'reverse': bool,        # F_mkt sufficiently below F_th (long future, short spot)
#         'inside_band': bool     # no trade (within band)
#       }
#     """