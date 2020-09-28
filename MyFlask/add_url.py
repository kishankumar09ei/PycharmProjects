from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "welcome to the Flask"


@app.route('/hello')
def hello_world():
    return "hello world"

def home():
    return "My Home Page"
app.add_url_rule('/home','home',home) # not using the @app.route .Here it will  use add url rule as if /home is there then use the fun
#home()

if __name__ == '__main__':
    app.run(debug=True)