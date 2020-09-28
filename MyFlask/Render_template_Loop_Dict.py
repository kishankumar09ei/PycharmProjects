from flask import Flask, render_template

app = Flask(__name__)


@app.route('/result')
def result():
    dict = {'Kishan': 1, "shiavm": 2, "Satyam": 3, "Shubha": 4}
    return render_template('loopTableDict.html', result=dict)


if __name__ == "__main__":
    app.run(debug=True)