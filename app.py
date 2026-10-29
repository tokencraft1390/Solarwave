import os
from flask import Flask, Response

app = Flask(__name__)

CONTACT = "zachary.ribble@flowlinkrev.com"

HTML = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Solarwave Micro-App Factory</title>
<style>
:root{color-scheme:dark;background:#090d13;color:#eef4ff;font-family:system-ui,-apple-system,Segoe UI,sans-serif}
*{box-sizing:border-box}body{margin:0}main{max-width:960px;margin:auto;padding:64px 22px}h1{font-size:clamp(2.4rem,8vw,5.5rem);margin:.1em 0}.sub{font-size:1.15rem;color:#aab7c9;max-width:720px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin:36px 0}.card{border:1px solid #273446;border-radius:18px;padding:22px;background:#101722}.price{font-size:2.2rem;font-weight:800;margin:8px 0}.cta{display:inline-block;margin-top:12px;padding:11px 15px;border-radius:10px;background:#eef4ff;color:#090d13;text-decoration:none;font-weight:700}.note{border-left:3px solid #6c7d94;padding:10px 16px;color:#bdc8d7}code{color:#d9e9ff}.foot{margin-top:42px;color:#738398;font-size:.9rem}</style>
</head>
<body><main>
<p><strong>SOLARWAVE</strong></p>
<h1>Small apps. Fresh-built.</h1>
<p class="sub">Order a bounded micro-app generated for your exact need. No shared customer codebase. Each paid order is scoped, generated, validated, and delivered as its own application.</p>
<div class="grid">
<section class="card"><h2>Static</h2><div class="price">$5</div><p>Single-file display app for a simple page, directory, profile, menu, or information surface.</p><a class="cta" href="mailto:''' + CONTACT + r'''?subject=Solarwave%20Static%20Order&body=App%20name%3A%0AWhat%20should%20it%20do%3F%0AFields%20or%20content%3A">Order $5</a></section>
<section class="card"><h2>CRUD</h2><div class="price">$10</div><p>Single-table SQLite app with a bounded create/read/update/delete workflow and up to five requested fields.</p><a class="cta" href="mailto:''' + CONTACT + r'''?subject=Solarwave%20CRUD%20Order&body=App%20name%3A%0AWhat%20should%20it%20track%3F%0AFields%20(max%205)%3A">Order $10</a></section>
<section class="card"><h2>CRUD + Webhook</h2><div class="price">$50</div><p>CRUD app plus one isolated webhook endpoint and a per-app secret. External service integration is scoped separately.</p><a class="cta" href="mailto:''' + CONTACT + r'''?subject=Solarwave%20Webhook%20Order&body=App%20name%3A%0AWorkflow%3A%0AFields%20(max%205)%3A%0AWebhook%20purpose%3A">Order $50</a></section>
</div>
<div class="note"><strong>Payment flow:</strong> submit the order request, receive a PayPal invoice, then production starts after payment is verified. A public one-click payment link is not yet live.</div>
<p class="foot">Current offer is intentionally bounded. No unsupported uptime, revenue, integration, or production-scale claims are made.</p>
</main></body></html>'''

@app.get("/")
def home():
    return Response(HTML, mimetype="text/html")

@app.get("/health")
def health():
    return {"ok": True, "service": "solarwave", "payment_link_live": False}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
