from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(
        {
            "remote_addr": request.remote_addr,
            "x_forwarded_for": request.headers.get("X-Forwarded-For"),
            "headers": dict(request.headers),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)