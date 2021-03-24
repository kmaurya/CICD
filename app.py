from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def print_Hello():
    return '<html><body><p style="color:red;">Hi</p></body></html>'


if __name__ == "__main__":
    app.run(port=5000,debug=True)
