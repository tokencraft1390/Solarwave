import os
from flask import Flask, Response

app = Flask(__name__)

CONTACT = "zachary.ribble@flowlinkrev.com"

HTML = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Solarwave — White-Label Micro-App Fulfillment</title>
<style>
:root{color-scheme:dark;background:#07111f;color:#f7fbff;font-family:Inter,system-ui,-apple-system,Segoe UI,sans-serif}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 15% 0%,rgba(94,234,212,.1),transparent 32%),#07111f}main{max-width:1050px;margin:auto;padding:68px 22px}h1{font-size:clamp(2.5rem,8vw,5.3rem);line-height:.98;letter-spacing:-.055em;margin:.15em 0}.sub{font-size:1.15rem;color:#9fb0c7;max-width:760px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(235px,1fr));gap:16px;margin:38px 0}.card{border:1px solid #20324d;border-radius:20px;padding:24px;background:#0d1a2d}.price{font-size:2.35rem;font-weight:900;margin:8px 0}.cta{display:inline-block;margin-top:12px;padding:12px 16px;border-radius:11px;background:#5eead4;color:#06121d;text-decoration:none;font-weight:850}.note{border:1px solid #27445c;background:#0a1729;padding:16px;border-radius:14px;color:#c9d5e6;margin:22px 0}.muted{color:#9fb0c7}.foot{margin-top:42px;color:#738398;font-size:.9rem}ul{padding-left:20px;color:#b8c6d9}</style>
</head>
<body><main>
<p><strong>SOLARWAVE</strong> · agency wholesale</p>
<h1>You keep the client. Solarwave handles the bounded build.</h1>
<p class="sub">White-label micro-app fulfillment for agencies, automation consultants, and operators. Send one sanitized requirement; receive a fixed scope, fixed wholesale price, tested artifact, and delivery evidence.</p>
<div class="grid">
<section class="card"><h2>Quick Utility</h2><div class="price">$350</div><p>Intake, calculator, status page, or small static utility.</p><ul><li>Up to 5 core fields</li><li>No persistent CRUD</li><li>First clean pilot fits here</li></ul><a class="cta" href="mailto:''' + CONTACT + r'''?subject=Solarwave%20Agency%20Pilot%20-%20Quick%20Utility&body=Agency%3A%0AApp%20name%3A%0AOutcome%3A%0AFields%20(max%205)%3A%0ADone%20when%3A">Send $350 pilot scope</a></section>
<section class="card"><h2>Working Micro-App</h2><div class="price">$650</div><p>CRUD tracker, dashboard, portal-lite, or admin utility.</p><ul><li>Up to 5 core fields</li><li>Single role</li><li>Simple persistence</li></ul><a class="cta" href="mailto:''' + CONTACT + r'''?subject=Solarwave%20Wholesale%20-%20Working%20Micro-App&body=Agency%3A%0AApp%20name%3A%0AOutcome%3A%0AFields%20(max%205)%3A%0AActions%3A%0ADone%20when%3A">Send $650 scope</a></section>
<section class="card"><h2>Connected Micro-App</h2><div class="price">$1,250</div><p>Working micro-app plus one bounded webhook/API integration or trigger.</p><ul><li>One integration maximum</li><li>Per-app secret where applicable</li><li>Separate scope for extras</li></ul><a class="cta" href="mailto:''' + CONTACT + r'''?subject=Solarwave%20Wholesale%20-%20Connected%20Micro-App&body=Agency%3A%0AApp%20name%3A%0AOutcome%3A%0AFields%20(max%205)%3A%0AIntegration%3A%0ADone%20when%3A">Send $1,250 scope</a></section>
</div>
<div class="note"><strong>Order-to-cash:</strong> scope → IN SCOPE / OUT OF SCOPE → fixed quote → PayPal invoice or approved payment rail → verify cleared payment → build → validate → acceptance test → evidence receipt → white-label delivery.</div>
<p class="muted"><strong>Boundary:</strong> the generated artifact/source may be included when specified in the accepted order. The Solarwave core factory, generator, orchestration logic, internal prompts, and validation process are not transferred through an ordinary micro-app order.</p>
<p class="foot">Standard accepted scopes target same-business-day delivery after complete inputs and verified payment. No unsupported uptime, revenue, integration, or production-scale claims are made.</p>
</main></body></html>'''

@app.get("/")
def home():
    return Response(HTML, mimetype="text/html")

@app.get("/health")
def health():
    return {"ok": True, "service": "solarwave", "payment_link_live": False, "offer": "agency-wholesale"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
