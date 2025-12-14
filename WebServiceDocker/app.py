from flask import Flask, request, render_template

app = Flask(__name__)

DATA = []  # simple in-memory store

@app.route("/submit", methods=["POST"])
def submit():
    json_data = request.get_json()
    DATA.append(json_data)
    return {"status": "ok"}

@app.route("/")
def index():
    return render_template("table.html", data=DATA)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
