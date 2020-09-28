from werkzeug.utils import redirect
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return "Hello Admin"


@app.route('/guest/<guest>')
def hello_guest(guest):
    return f" Hello {guest} as Guest"


@app.route('/user/<name>')
def hello_user(name):
    if name == "admin":
        return redirect(url_for('hello_admin'))
        #if name ==Admin then redirect to the url for function 'hello admin' and this return data is shown

    else:
        return redirect((url_for('hello_guest', guest=name)))
#if name is something else then this will be routed to function hello_guest function and the argument is passed along with it as name that is passed i  URL


if __name__ == '__main__':
    app.run(debug=True)
