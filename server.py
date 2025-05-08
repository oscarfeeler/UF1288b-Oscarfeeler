from flask import Flask
import socket

app = Flask(__name__)

def get_ipv4_address():
    # Connect to an external host; doesn't actually send data
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # This IP doesn't need to be reachable;
        # just used to determine the local IP
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


# Constants for client
LOCAl_IP = get_ipv4_address()
DEFAULT_PORT = 5000
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=DEFAULT_PORT, debug=False)