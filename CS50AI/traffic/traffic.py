import cv2
import numpy as np
from numpy.typing import NDArray
import os
import sys
import keras

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
IMG_COLOUR_CHANNELS = 3
IMG_DIMENSIONS_TUPLE = (IMG_WIDTH, IMG_HEIGHT, IMG_COLOUR_CHANNELS)
NUM_CATEGORIES = 43  # 3 for small dataset and 43 for large data set
TEST_SIZE = 0.4


def func1(input):
    try:
        int(input)
        return True
    except:
        return False


def main():
    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test, y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def is_integer(text):
    try:
        int(text)
        return True
    except ValueError:
        return False


def load_data(data_dir: str):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    attr1: list[NDArray] = []
    attr2: list[int] = []
    image = None
    img_array = None
    files1 = os.listdir(data_dir)
    for i in files1:
        if func1(i):
            break
        attr3 = os.path.join(data_dir, i)
        print("label_dir", attr3)

        files2 = os.listdir(attr3)
        for j in files2:
            image = cv2.imread(os.path.join(attr3, j))
            image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
            img_array = np.array(image)
            attr1.append(img_array)
            attr2.append(int(i))

    print("count:", "images:", len(attr1), "labels:", len(attr2))
    if image is not None:
        print("image size:", image.shape, "target", IMG_DIMENSIONS_TUPLE,)
    if img_array is not None:
        print("image array size", img_array.shape, "target", IMG_DIMENSIONS_TUPLE,)
    return (attr1, attr2)


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.

    See https://www.tensorflow.org/guide/keras
    """

    model = keras.models.Sequential(
        [keras.layers.Conv2D(32, (3, 3), input_shape=IMG_DIMENSIONS_TUPLE, activation="relu"),
         keras.layers.MaxPooling2D(pool_size=(2, 2)),
         keras.layers.Flatten(),
         keras.layers.Dense(100, activation="relu"),
         keras.layers.Dense(NUM_CATEGORIES, activation="softmax"),])

    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"],)

    return model


if __name__ == "__main__":
    main()
