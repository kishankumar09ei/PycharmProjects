from flask import Flask,request,jsonify,render_template
import os
from flask_cors import CORS,cross_origin
from predict import MyFriends
from utils.change_to_Base64 import decodeImage,encodeImageIntoBase64


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app= Flask(__name__)
CORS(app)


class clientApp:
    def __init__(self):
        self.filename="untitled.png"
        self.classifier= MyFriends(self.filename)


@app.route('/',methods=['GET'])
@cross_origin()
def home():
    return  render_template('index.html')

@app.route('/predict',methods=['POST'])
@cross_origin()
def predictRoute():
    image=request.json['image']
    decodeImage(image,clApp.filename)
    result= clApp.classifier.predictMyFriend()
    return jsonify(result)


if __name__ == '__main__':
    clApp=clientApp()
    app.run(debug=True)


