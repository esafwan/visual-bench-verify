# Huf module
- Surfaces: flow canvas, node palette, node settings drawer, run-status view, agent/settings pages (Frappe desk doctype forms for backend-owned doctypes).
- Flow node backend schema: node registry / `huf_flow_nodes` hook output (params, defaults, enums). Compare to the drawer controls.
- Known past failures: trigger nodes shipped with scaffold defaults active; fields added in backend but missing from drawer; stale frontend bundle on bench. Always rebuild frontend and confirm the asset hash.
- Run-status to verify: waiting/parked ("Waiting until ..."), resumed, failed, retried, completed.
- Bench/site/credentials: `environment-map` skill. Slot lease/preflight: `ui-verify` scripts.
- Agent icon is lucide SquareAsterisk (never Bot).
