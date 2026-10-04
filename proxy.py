#!/usr/bin/env python3
"""
Serveur local : fichiers statiques + proxy vers data.gouv.fr
Usage : python3 proxy.py
Puis ouvrir http://localhost:8000/monitor-api.html
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
import json

PROXY_PREFIX = "/api/"
TARGET_BASE = "https://www.data.gouv.fr"

class ProxyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # --- Route proxy : /api/... → https://www.data.gouv.fr/api/... ---
        if self.path.startswith(PROXY_PREFIX):
            self.handle_proxy()
            return
        # --- Sinon : fichier statique normal ---
        super().do_GET()

    def do_OPTIONS(self):
        # Preflight CORS pour les appels depuis le navigateur
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def handle_proxy(self):
        target = TARGET_BASE + self.path
        try:
            req = Request(target, headers={"User-Agent": "Monitor-DECP/1.0"})
            with urlopen(req, timeout=60) as resp:
                body = resp.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
        except HTTPError as e:
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
        except URLError as e:
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e.reason)}).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def log_message(self, fmt, *args):
        # Log plus lisible
        print(f"[proxy] {self.address_string()} - {fmt % args}")

if __name__ == "__main__":
    port = 8000
    server = HTTPServer(("localhost", port), ProxyHandler)
    print(f"✅ Serveur prêt sur http://localhost:{port}")
    print(f"   Proxy API : http://localhost:{port}/api/...")
    print(f"   Monitor   : http://localhost:{port}/monitor-api.html")
    print("   Ctrl+C pour arrêter.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Arrêt.")
