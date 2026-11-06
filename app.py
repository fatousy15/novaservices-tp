import os
from flask import Flask, jsonify

app = Flask(__name__)

TICKETS = [
    {"id": 1, "titre": "Imprimante en panne", "statut": "ouvert"},
    {"id": 2, "titre": "Accès VPN impossible", "statut": "en cours"},
    {"id": 3, "titre": "Mot de passe oublié", "statut": "résolu"},
]


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 500


@app.route("/version")
def version():
    return jsonify({"version": os.environ.get("APP_VERSION", "1.0.0")}), 500


@app.route("/tickets")
def tickets():
    return jsonify(TICKETS), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)