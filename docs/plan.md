# ForwardPricing — Project Plan

**Author:** Stepan Logatskii  
**Goal:** Build a complete forward-pricing engine by December 2025.  
The tool will calculate theoretical forward prices and compare them to market data to identify potential arbitrage opportunities.

---

## 📅 Timeline

### Phase 1 — Setup (✅ Completed)
- Configure Git & GitHub connection  
- Create project structure  
- Write README and initial documentation

### Phase 2 — Level 1: Basic Forward Model (October)
- Implement theoretical formula: `F₀ = S₀ * e^(rT)`  
- Test with fixed inputs (S₀ = 100, r = 0.05, T = 1)  
- Add plotting: how forward price changes with `r` or `T`  
- Document results and basic theory

### Phase 3 — Level 2: Dividend Yield (Early November)
- Extend formula: `F₀ = S₀ * e^{(r - q)T}`  
- Add tests for `q` values  
- Update README with math + code examples

### Phase 4 — Level 3: Market Data Integration (Mid–Late November)
- Pull spot and forward data from Yahoo Finance or FRED  
- Compute theoretical forwards for same assets  
- Compare and visualize deviations  
- Save CSV of differences

### Phase 5 — Finalization (December)
- Add a clean PDF report (`docs/report.pdf`)  
- Polish visuals and documentation  
- Make project fully reproducible  
- Write LinkedIn post about results