import numpy as np
from PIL import Image
import os

IMAGE_SIZE = 224
HOME = os.environ["HOME"]
current_dir = os.getcwd()
numberOfImages = 300

# def initialize_img():
#   input_path = f"{current_dir}/train"
#   output_path = f"{current_dir}/train/224x224"
#   for j in range(1, numberOfPersons+1):
#     for number in range(numberOfImages):
#         input_img_path = f"{input_path}/s{3}/{number}.jpg"
#         # change to gray scale
#         image = Image.open(input_img_path).convert('L')
#         print(image.filename)
#         image = image.resize((IMAGE_SIZE, IMAGE_SIZE), Image.LANCZOS)
#         image.save(f"{output_path}/s{j}/{number}.jpg")


def LoadData():
    data = []
    label = [] # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    input_path = os.path.join(current_dir, "train", str(IMAGE_SIZE))
    numberOfPersons = len(os.listdir(input_path))

    for j in range(1, numberOfPersons+1):
        for number in range(numberOfImages):
            input_img_path = f"{input_path}/s{j}/{number}.jpg"
            img = Image.open(input_img_path)
            img = np.reshape(img, (1, IMAGE_SIZE*IMAGE_SIZE))
            data.extend(img)

        # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        label.extend(np.ones(numberOfImages, dtype=np.int64) * j)
    data = np.reshape(data, (numberOfImages*j, IMAGE_SIZE*IMAGE_SIZE))
    """
        --- data ---
        [[168 150 137 ... 227 243 248]
        [106 106 106 ...  69  92  88]
        [218 217 216 ... 210 211 211]
        ...
        [241 241 243 ...  92  89  84]
        [241 241 241 ...  58  64  68]
        [255 255 255 ... 211 191 151]]
    """
    """
        Data and Label

        [[168 150 137 ... 227 243 248] [1]
        [106 106 106 ...  69  92  88]  [1]
        [218 217 216 ... 210 211 211]  [1]
        ...
        [241 241 243 ...  92  89  84]  [4]
        [241 241 241 ...  58  64  68]  [4]
        [255 255 255 ... 211 191 151]  [4]
        [1]
        [1]
        [1]
        [2]
        [2]
        [2]
        [2]
        [3]
        [3]
        [3]
        [3]
        [4]
        [4]
        [4]
        [4]]
    """
    return np.matrix(data), np.matrix(label).T


# if __name__ == '__main__':
    # initialize_img()