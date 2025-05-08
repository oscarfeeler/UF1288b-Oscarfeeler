from flask import Flask, request
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
@app.route("/", methods=["GET", "POST"])
def recibir_mensajes():
    mensaje_recibido = request.json
    if mensaje_recibido:
        print(f"Mensaje recibido: {mensaje_recibido}")
        return "Mensaje recibido"
    else:
        return "No se recibió ningún mensaje"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=DEFAULT_PORT, debug=False)