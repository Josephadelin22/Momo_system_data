import base64
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import re

# Load transactions data from the previous parsing step
with open("sms_transactions2.json", "r") as f:
    transactions = json.load(f)

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    # Authentication Helpers
    def check_auth(self):
        auth_header = self.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Basic '):
            return False
        encoded = auth_header.split(' ', 1)[1]
        try:
            decoded = base64.b64decode(encoded).decode('utf-8')
            username, password = decoded.split(':', 1)
        except Exception:
            return False
        # Mock credentials
        return username == 'admin' and password == 'password123'

    def authenticate(self):
        if not self.check_auth():
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm="API"')
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}')
            return False
        return True

    # CRUD Endpoints
    def do_GET(self):
        if not self.authenticate():
            return
        if self.path == "/transactions":
            self._set_headers()
            self.wfile.write(json.dumps(transactions).encode())
        elif re.match(r"^/transactions/\d+$", self.path):
            transaction_id = self.path.rsplit('/', 1)[-1]
            tx = next((tx for tx in transactions if tx['id'] == transaction_id), None)
            if tx:
                self._set_headers()
                self.wfile.write(json.dumps(tx).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Not found"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Invalid endpoint"}).encode())

    def do_POST(self):
        if not self.authenticate():
            return
        if self.path == "/transactions":
            length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(length)
            new_tx = json.loads(post_data)
            transactions.append(new_tx)
            self._set_headers(201)
            self.wfile.write(json.dumps(new_tx).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Invalid endpoint"}).encode())

    def do_PUT(self):
        if not self.authenticate():
            return
        if re.match(r"^/transactions/\d+$", self.path):
            transaction_id = self.path.rsplit('/', 1)[-1]
            tx = next((tx for tx in transactions if tx['id'] == transaction_id), None)
            if not tx:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Not found"}).encode())
                return
            length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(length)
            updated_data = json.loads(put_data)
            tx.update(updated_data)
            self._set_headers()
            self.wfile.write(json.dumps(tx).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Invalid endpoint"}).encode())

    def do_DELETE(self):
        if not self.authenticate():
            return
        if re.match(r"^/transactions/\d+$", self.path):
            transaction_id = self.path.rsplit('/', 1)[-1]
            index = next((i for i, tx in enumerate(transactions) if tx['id'] == transaction_id), None)
            if index is None:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Not found"}).encode())
                return
            deleted = transactions.pop(index)
            self._set_headers()
            self.wfile.write(json.dumps(deleted).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Invalid endpoint"}).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    print(f'API running on port {port}...')
    server_class(('', port), handler_class).serve_forever()

if __name__ == "__main__":
    run()
