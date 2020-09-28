from flask import Flask

app = Flask(__name__) #for creating the app as flask application


@app.route('/')
def index():
    return "welcome to the Flask"


@app.route('/hello') #this will route to this function is /hello is provided in url
def hello_world():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
