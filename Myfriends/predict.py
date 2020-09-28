import numpy as np
from keras.models import load_model
from keras.preprocessing import image

class MyFriends():
    def __init__(self,filename):
        self.filename=filename

    def predictMyFriend(self):
        #load model
        model=load_model("image_classify_model.h5")
        imagename= self.filename
        test_image=image.load_img(imagename,target_size=(64,64))
        #chnaging image into array/matrix
        test_image=image.img_to_array(test_image)
        #flattening the image array
        test_image=np.expand_dims(test_image,axis=0)
        result=model.predict_proba(test_image)
        print(result)
        if np.argmax(result[0]) == 0:
            prediction = 'baby'
            return [{"image": prediction}]
        elif np.argmax(result[0]) == 1:
            prediction = 'Kishan'
            return [{"image": prediction}]
        else:
            prediction = 'Rakesh'
            return [{"image": prediction}]