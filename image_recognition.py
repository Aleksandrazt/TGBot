from io import BytesIO
from os import remove

import numpy as np
from PIL import Image
from keras.utils import load_img, img_to_array


def find_class(b_photo, pattern):
    """
    Convert photo to needed format and predict solution with pre-learned nn
    :param b_photo: bytes photo from tg
    :param pattern: pre-learned model
    :return:
    """
    get_image_from_bytes(b_photo)
    image_width, image_height = 250, 250
    image = load_img("question.png", target_size=(image_width, image_height))
    input_arr = img_to_array(image)
    input_arr = np.array([input_arr])
    predictions = pattern.predict(input_arr)
    print(predictions)
    max_ind = np.unravel_index(np.argmax(predictions), predictions.shape)
    remove("question.png")
    return max_ind


def get_image_from_bytes(b):
    """
    Gets bytes and save it as an image
    :param b:
    :return:
    """
    stream = BytesIO(b)
    image = Image.open(stream).convert("RGBA")
    image.save("question.png", "PNG")
    stream.close()

