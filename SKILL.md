---
name: visual-bench-verify
description: >
  Coverage-and-correctness audit of the visible UI for a change set, run on a live bench in a real browser.
  Verifies every backend field reached the UI, defaults/labels/IA are right, no scaffold or placeholder values
  are active, save+reload persists, run-status states render, layout/a11y/console are clean. Use when the user says
  "visually verify", "UI verify the PR", "check the UI is complete", "live bench test", or before merging ANY
  UI-touching change (nodes, panels, doctype forms, settings, list views). Complements ui-verify (scripted journeys).
license: MIT
metadata:
  version: "1.0"
---

# visual-bench-verify

A change is "live-bench tested" only when the functional E2E **and** a PASS report from this skill exist for the **same head SHA**.
`ui-verify` = scripted journeys; `ui-design` = authoring; `screenshot` = capture. This skill audits *completeness and correctness* of the visible UI. Reuse `ui-verify`'s bench slot lease / preflight / evidence conventions (`scripts/slot_lease.sh`, `preflight.sh`); do not duplicate them.

## Hard rules
- Real built UI on a live bench only. No dev mocks, no Storybook.
- Drive the browser with Playwright MCP (`mcp__playwright__*`) or the browse tool. Screenshot for every check.
- No evidence = UNVERIFIED. Any UNVERIFIED or FAIL = overall FAIL. No "looks fine".
- Never change app state via API mid-check. Seeding a fixture beforehand is allowed but must be logged in the report.
- Bench blocked or stale build = BLOCKED, which never counts as verified.

## Inputs
PR / diff base, UX_SPEC.md (or equivalent), bench URL + credentials (look up in `environment-map`), head SHA. Domain notes: `modules/huf.md`.

## Procedure
0. **Scope**: `git diff --name-only base...HEAD`; classify into UI surfaces (nodes, panels, forms, settings, lists). Build an element inventory, one row each.
1. **Preflight**: bench runs the head SHA; frontend assets rebuilt (no stale bundle/hash); log in; clear console.
2. **Field coverage**: `python3 scripts/field_coverage.py --backend backend.json --ui ui.json [--whitelist w.json]`.
   Backend side = doctype JSON fields (minus hidden/computed/layout) or node config schema + defaults. UI side = controls collected from `browser_snapshot` or `browser_evaluate` (`[data-fieldname]`, `name`, `aria-label`). Backend-only = forgotten in UI (FAIL unless whitelisted with reason); UI-only = orphan/scaffold (FAIL); defaults must equal UI initial values; placeholders (`TODO`, `lorem`, `example.com`, `test_*`, empty where required) FAIL.
3. **Per-element checks**: fill `templates/CHECKLIST.md` for each element.
4. **Round-trip**: set every field to a non-default value, save, hard reload, reopen, all persist; run/submit and confirm the runtime honoured the config via the run log in the UI.
5. **States**: empty, validation error, loading, waiting/parked, resumed, failed, retried, completed.
6. **Layout and a11y**: widths 1440, 1024, 390 and compact panel (no clipping); keyboard reaches every control; labels present; focus visible.
7. **Console/network**: `node scripts/collect_console.mjs` for the snippet to paste into `browser_evaluate`, plus `browser_console_messages` / `browser_network_requests`. Zero new errors/warnings, no 4xx/5xx on involved endpoints.
8. **Report**: write `templates/REPORT.md` filled in; copy to the track dir and PR comment. PASS only if every row PASS; on FAIL list each row with screenshot and fix owner (backend/frontend).
