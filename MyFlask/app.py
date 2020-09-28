from flask import Flask

app = Flask(__name__)


@app.route('/') #/ with the Running URL will be give the output of the hello world(). This is the work of @app.route()
def hello_world():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
