from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ar/status")
def ar_status():
    return jsonify({
        "assistant": "Jarvis",
        "status": "online",
        "alert": "All systems normal"
    })

if __name__ == "__main__":
    app.run(port=6000)

