from flask import Flask, redirect, render_template, request, url_for, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))


@app.route('/success')
def success():
    return 'logeed in successfully'


if __name__ == '__main__':
    app.run(debug=True)
