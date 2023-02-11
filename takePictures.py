import os
import sys
from PIL import Image
from face_detect import getDataFromCamera
import shutil
import customtkinter


# customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# app = customtkinter.CTk()
# app.geometry("400x780")
# app.title("CustomTkinter simple_example.py")
# app.mainloop()


count = 1
IMAGE_SIZE = 224
current_dir = os.getcwd()
name = "yezarniko"
number_of_images_you_want = 300
train_dir = os.path.join(current_dir, "train")
train_dir_IMAGE_SIZE = os.path.join(train_dir, str(IMAGE_SIZE))
personID = len(os.listdir(train_dir_IMAGE_SIZE)) + 1
train_data_path = os.path.join(train_dir_IMAGE_SIZE, f"s{personID}")


if not os.path.exists(train_dir):
    os.mkdir(train_dir)
    if not os.path.exists(train_dir_IMAGE_SIZE):
        os.mkdir(train_dir_IMAGE_SIZE)

if not os.path.exists(train_data_path):
    os.mkdir(train_data_path)
else:
    resp = input("Do you want to overwrite: ")
    if(resp == 'y'):
        shutil.rmtree(train_data_path)
        os.mkdir(train_data_path)
    else:
        sys.exit()

def save_img(img_frame, file_name):
    global count
    img = Image.fromarray(img_frame)    
    img.save(f"{train_data_path}/{file_name}.jpg")
    print(count)


def takePics(img_test, _, __):
    global count
    save_img(img_test, count)
    if count == number_of_images_you_want:
        sys.exit()
    count += 1


getDataFromCamera(takePics)
