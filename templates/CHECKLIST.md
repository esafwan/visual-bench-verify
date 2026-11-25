## <Element name>  (type: node | form | setting | view)   SHA: <sha>
| # | Check | Expected (UX_SPEC ref) | Result PASS/FAIL/UNVERIFIED | Evidence (screenshot) | Note |
|---|-------|------------------------|-----------------------------|-----------------------|------|
| 1 | Appears in palette/menu in right group & order | | | | |
| 2 | Loads/renders on canvas or screen without error | | | | |
| 3 | Label, icon, copy match spec (no raw keys/snake_case) | | | | |
| 4 | Panel shows every backend field (0 missing, 0 orphan) | | | | |
| 5 | Defaults match backend; no scaffold/placeholder/test values | | | | |
| 6 | Grouping, order, sections, help text = IA in spec | | | | |
| 7 | Conditional fields show/hide correctly (depends_on) | | | | |
| 8 | Validation: required/invalid shows clear message, blocks save | | | | |
| 9 | Save -> hard reload -> values persist | | | | |
| 10 | Runtime honours config (run log/result via UI) | | | | |
| 11 | Run-status states render (waiting/parked/resumed/failed/retried/done) | | | | |
| 12 | Empty / error / loading states | | | | |
| 13 | Responsive 1440 / 1024 / 390 + compact panel, no clipping | | | | |
| 14 | Console clean, no failing network calls | | | | |
| 15 | A11y: labels, keyboard reach, focus visible | | | | |
Overall: PASS only if all rows PASS.
