#!/usr/bin/env node
// Prints a JS snippet to paste into browser_evaluate / page.evaluate.
// Run it BEFORE the interaction (install), then again AFTER (dump) to get errors + failed requests.
const snippet = `(() => {
  if (!window.__vbv) {
    window.__vbv = { errors: [], failed: [] };
    const oe = console.error, ow = console.warn;
    console.error = (...a) => { window.__vbv.errors.push('error: ' + a.join(' ')); oe(...a); };
    console.warn = (...a) => { window.__vbv.errors.push('warn: ' + a.join(' ')); ow(...a); };
    window.addEventListener('error', e => window.__vbv.errors.push('uncaught: ' + e.message));
    window.addEventListener('unhandledrejection', e => window.__vbv.errors.push('rejection: ' + e.reason));
    const of = window.fetch;
    window.fetch = async (...a) => { const r = await of(...a); if (r.status >= 400) window.__vbv.failed.push(r.status + ' ' + (a[0].url || a[0])); return r; };
    return 'installed';
  }
  return window.__vbv;
})()`;
console.log(snippet);
