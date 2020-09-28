from flask import Flask

app = Flask(__name__)


@app.route('/')
def show():
    return '<html><body> <h1> Hello its a simple HTML </h1></body></html>'


if __name__ == "__main__":
    app.run(debug=True)
