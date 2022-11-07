from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

#Fetch hostname and IP
def fetchdetails():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, host_ip = fetchdetails()
    return render_template('index.html', HOSTNAME=hostname, IP=host_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)