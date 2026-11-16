"""Intentionally vulnerable local API for learning authorization.

WARNING: This is a teaching lab, not production code. The --secure flag
adds an ownership check but does NOT authenticate the X-Lab-User header.
Run only on localhost with fictional data.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys

SECURE = "--secure" in sys.argv

accounts = {
    "101": {"owner": "alice", "balance": 100},
    "102": {"owner": "bob", "balance": 200},
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        account_id = self.path.removeprefix("/accounts/")
        user = self.headers.get("X-Lab-User", "")
        account = accounts.get(account_id)

        if not self.path.startswith("/accounts/") or not account:
            self.respond(404, {"error": "Not found"})
        elif SECURE and account["owner"] != user:
            self.respond(403, {"error": "Access denied"})
        else:
            self.respond(200, account)

    def respond(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


print(f"Lab running at http://127.0.0.1:8000 (secure={SECURE})")
HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
