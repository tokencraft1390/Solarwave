import os
from pathlib import Path

from flask import Flask, Response

app = Flask(__name__)
INDEX = Path(__file__).with_name("index.html")


@app.get("/")
def home():
    return Response(INDEX.read_text(encoding="utf-8"), mimetype="text/html")


@app.get("/health")
def health():
    return {
        "ok": True,
        "service": "solarwave",
        "offer": "agency-wholesale",
        "fit_check": "deterministic",
        "payment_link_live": False,
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
