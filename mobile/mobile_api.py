from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    return jsonify({"response": f"Executed: {data['cmd']}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

