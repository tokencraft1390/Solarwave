# Solarwave State

Snapshot date: 2026-10-29

## Commercial state

- Offer: ACTIVE FOR ORDER INTAKE.
- Prices: $5 Static / $10 CRUD / $50 CRUD + Webhook.
- Canonical live conversion storefront: https://melded-tide-md3d37b.shipstatic.com
- Storefront source: `index.html` on `main`.
- Storefront deployment status: success; no password; no expiry.
- Storefront UX includes interactive tier selection, dynamic price/deliverable preview, clickable example prefills, mobile CTA, trust boundaries, FAQ, and structured order handoff.
- Previous ShipStatic order page `https://viral-void-k22psqq.shipstatic.com` is superseded by the upgraded storefront and should not be used as the primary traffic destination.
- Shareable PayPal payment link: NOT PRESENT. Connected PayPal account returned zero payment links on 2026-10-29.
- Payment fallback: buyer-specific PayPal invoice after order/spec intake. Treat an order as paid only after payment is independently verified.
- Verified customer payment receipts: none recorded in this snapshot.

## GitHub state

- Canonical repository: `tokencraft1390/Solarwave`.
- Default branch: `main`.
- Repository is public.
- Founder/admin access was verified through the connected GitHub account.
- Deployable order-intake code, single-file storefront, and evidence ledgers are committed on `main`.
- Storefront commit: `a258c148548fa67e3748aeb42f4c14fd41e25ae0`.

## Railway state

- Project: `solar-tenant-poc` (`4eaffc6a-0c4d-4824-a638-255e74a14182`).
- Environment: `production` (`bd32a560-378b-4391-a5a0-a170bb1864cc`).
- Existing service: `tenant-demo-001` (`7762ab2b-8002-42c8-8b1a-46383b7616a4`).
- Observed state: `live`.
- Source: image `python:3.11-slim`, not GitHub.
- Replica count: 1.
- Region: `sfo`.
- Persistent volumes: none.
- Latest deployment object: not returned by the connector at the time of observation.

### Repo-backed deployment attempt

A deployment from `tokencraft1390/Solarwave` into the existing production environment was attempted on 2026-10-29. Railway returned:

> Your trial has expired. Please select a plan to continue using Railway.

Result: the new repo-backed `solarwave` Railway service is **not deployed**. The blocker is Railway account plan state, not an observed application build/runtime failure.

## ShipStatic state

- Canonical storefront deployment: `melded-tide-md3d37b.shipstatic.com`.
- Deployment status: `success`.
- Deployment labels: `solarwave`, `sales`, `production`, `ux-v1`.
- Password protection: none.
- Expiry: none.
- Previous sales/order-intake deployment `viral-void-k22psqq.shipstatic.com` remains available but is superseded.
- `solarwave.shipstatic.com` was checked and reported available.
- Attempting to link that cleaner domain failed because the ShipStatic account reported its domain limit was reached and requires a Pro upgrade.
- Do not represent `solarwave.shipstatic.com` as live.

## Validated implementation direction

- Deterministic generation rather than arbitrary LLM-generated executable code.
- Maximum five user-defined fields in the current bounded design.
- Static / CRUD / CRUD+webhook tiers.
- Per-app webhook secret for the webhook tier.
- AST/syntax validation before delivery.
- No `eval`, `exec`, `compile`, or dynamic `__import__` execution path.
- SHA-256 for evidence hashes.
- Hosted SQLite deployments require persistent storage.
- Tenant execution should be isolated by service/container rather than arbitrary customer subprocesses in one shared runtime.

## Current blockers

1. PayPal shareable payment link has not been created.
2. Railway repo deployment is blocked because the Railway trial/account plan has expired.
3. Full automatic pay -> provision -> receipt workflow is not yet verified end-to-end.
4. Railway persistent storage is not attached to the existing tenant demo.
5. Cleaner ShipStatic alias is blocked by the current ShipStatic domain plan limit.

## Next commercialization gate

Drive qualified traffic to the upgraded storefront, receive a real buyer order, issue a PayPal invoice, verify cleared payment, generate the bounded application, validate it, deliver/deploy it through an available route, and store the payment/delivery receipt and evidence hash.
