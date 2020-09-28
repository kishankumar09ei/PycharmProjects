import base64

def decodeImage(imgString,filename):
    imgdata=base64.b64decode(imgString)
    with open(filename,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read())
