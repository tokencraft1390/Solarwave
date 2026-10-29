# Solarwave

Solarwave is a founder-directed micro-app fulfillment system for agencies, automation consultants, and operators who need a small custom application without turning it into a full software project.

The commercial posture is **agency-first and white-label**: the partner keeps the client relationship, branding, and markup; Solarwave accepts a bounded requirement and returns a tested buyer-specific artifact.

## Current wholesale offer

| Tier | Wholesale price | Hard scope |
|---|---:|---|
| Quick Utility | $350 USD | Static/intake/calculator/status utility; up to 5 core fields; no persistent CRUD |
| Working Micro-App | $650 USD | CRUD tracker/dashboard/portal-lite; up to 5 core fields; single role; simple persistence |
| Connected Micro-App | $1,250 USD | Working Micro-App plus one bounded webhook/API integration or workflow trigger |

Optional commercial add-ons:

- Rush acceptance/delivery lane: **+$250** when capacity is explicitly accepted.
- Recurring care: **$199/month** for up to two bounded changes per month; redesigns and new integrations are separate scope.
- First clean agency pilot: **$350** when the requirement fits the Quick Utility boundary.

The public buyer value proposition is fixed cost, bounded scope, white-label delivery, and fast turnaround. Solarwave does **not** advertise an internal build-time target as a customer guarantee.

## Buyer and delivery boundary

The Solarwave factory, generator, orchestration logic, internal prompts, validation rules, and operating process are not automatically part of a customer deliverable. A buyer may receive the generated artifact/source when that delivery type is included in the accepted order; that does not transfer the core factory.

Do not use the core GitHub repository as the sales CTA. Buyer-facing proof should be the storefront/demo, one-page scope sheet, example artifact, test evidence, and delivery receipt.

## Order-to-cash path

`partner requirement -> IN SCOPE / OUT OF SCOPE -> fixed quote -> payment/approved PO -> verify cleared payment -> generate -> validate -> acceptance test -> evidence receipt -> white-label delivery -> ask for next job`

For a new partner, standard jobs are prepaid. The connected PayPal path currently supports buyer-specific invoicing; a shareable one-click payment link has not yet been verified live. A deal is not counted as paid until the payment state is independently verified.

## Scope rules

The bounded instant lane rejects rather than improvises. It exits standard scope when the requirement includes any of the following without a separate quote:

- More than five core user-defined fields.
- Multiple user roles or custom RBAC/authentication.
- More than one external integration.
- Regulated or highly sensitive data handling.
- Complex relational data models or reporting.
- Embedded payment processing.
- Ambiguous acceptance criteria.

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

Current agency-wholesale sales surface: `https://baseless-mind-y8sgs9r.shipstatic.com`.

ShipStatic verified the deployment as successful on 2026-10-29 with labels `solarwave`, `sales`, `production`, and `agency-wholesale`. This storefront is buyer-facing; the GitHub repository is not the sales CTA.

Railway project: `solar-tenant-poc`.

The existing Railway service was previously observed live from the public image `python:3.11-slim`, not from this repository. A new repo-backed deployment was blocked because the Railway trial/account plan had expired. Do not represent the repo-backed Railway deployment as live until that changes and is verified.

## Evidence model

Solarwave keeps two separate ledgers:

1. **Provenance** — who originated/directed the architecture, iterations, decisions, and operations.
2. **Rights** — licenses, assignments, third-party dependencies, trademarks, and other chain-of-title issues.

AI assistance is recorded as an implementation/construction method, not as a founder, owner, or rights holder.

See `STATE.md`, `PROVENANCE.md`, `RIGHTS.md`, `AGENCY_ONE_PAGER.md`, and `COMMERCIALIZATION.md` for the current operating snapshot.
