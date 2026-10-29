# Solarwave

Solarwave is a founder-directed micro-app factory and commercialization experiment focused on generating small, isolated customer applications without a shared customer codebase.

## Current commercial offer

| Tier | Price | Scope |
|---|---:|---|
| Static | $5 USD | Single-file display app |
| CRUD | $10 USD | Single-table SQLite CRUD app |
| CRUD + Webhook | $50 USD | CRUD app plus isolated webhook endpoint and per-app secret |

Current live conversion storefront: https://melded-tide-md3d37b.shipstatic.com

The upgraded single-file storefront is committed as `index.html`. It includes an interactive tier configurator, dynamic scope/price preview, use-case prefills, bounded trust language, FAQ, mobile CTA, and a structured order handoff.

Payment checkout is **not yet verified live**. As of 2026-10-29, the connected PayPal account reports zero shareable payment links. The current collection path is: configure order -> send structured request -> buyer-specific PayPal invoice -> independently verify cleared payment -> generate/validate -> deliver/deploy -> receipt.

## Architecture direction

Solarwave uses a bounded generation pipeline:

`spec -> deterministic generator -> validation/lint -> isolated delivery/deployment -> evidence/state`

Production rules:

- No arbitrary `eval`/`exec` path.
- LLM output is not trusted as executable code.
- Generated code is constrained and validated before delivery.
- Customer execution should be isolated per tenant/service rather than spawning arbitrary customer subprocesses inside one shared runtime.
- SHA-256 is used for evidence hashes.
- Secrets belong in environment variables or platform secret stores, not source code.
- SQLite-backed hosted tiers require persistent storage when deployed.

## Verified infrastructure state

Railway project: `solar-tenant-poc`

Production environment: `bd32a560-378b-4391-a5a0-a170bb1864cc`

Existing service: `tenant-demo-001`

Service source: public image `python:3.11-slim` (not connected to this GitHub repository).

The Railway service was last observed in `live` state, with one replica in `sfo`, no attached volume, and no latest deployment object returned by the connector. A new repo-backed deployment from Solarwave was attempted and blocked because the Railway trial/account plan had expired.

## Evidence model

Solarwave keeps two separate ledgers:

1. **Provenance** — who originated/directed the architecture, iterations, decisions, and operations.
2. **Rights** — licenses, assignments, third-party dependencies, trademarks, and other chain-of-title issues.

AI assistance is recorded as an implementation/construction method, not as a founder, owner, or rights holder.

See `STATE.md`, `PROVENANCE.md`, and `RIGHTS.md` for the current evidence snapshot.
