from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)


@app.route('/upload')
def upload():
    return render_template('FileUpload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "file uplaoded Successfully"


if __name__ == '__main__':
    app.run(debug=True)
