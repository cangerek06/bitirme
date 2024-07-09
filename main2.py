from keras.models import load_model
import cv2 as cv
import numpy as np

def resize_image(img, size=(28,28)):

    h, w = img.shape[:2]
    c = img.shape[2] if len(img.shape)>2 else 1

    if h == w:
        return cv.resize(img, size, cv.INTER_AREA)

    dif = h if h > w else w

    interpolation = cv.INTER_AREA if dif > (size[0]+size[1])//2 else cv.INTER_CUBIC

    x_pos = (dif - w)//2
    y_pos = (dif - h)//2

    if len(img.shape) == 2:
        mask = np.zeros((dif, dif), dtype=img.dtype)
        mask[y_pos:y_pos+h, x_pos:x_pos+w] = img[:h, :w]
    else:
        mask = np.zeros((dif, dif, c), dtype=img.dtype)
        mask[y_pos:y_pos+h, x_pos:x_pos+w, :] = img[:h, :w, :]

    return cv.resize(mask, size, interpolation)


def predictImage(filename):
    img2 = cv.imread(filename)[:, :, 0]
    img2 = resize_image(img2)
    img2 = np.invert(np.array([img2]))
    prediction = model.predict(img2)
    print(str(np.argmax(prediction)))



model = load_model('mnist.h5')
print("*************************")
predictImage('/home/ubuntu/Downloads/7.png')