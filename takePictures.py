import os
import threading
import sys
from PIL import Image
from face_detect import getDataFromCamera
import shutil
import customtkinter
import cv2

customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("300x300")
app.configure(fg_color="#ffffff")
app.resizable(False, False)  # This code helps to disable windows from resizing
app.title("CustomTkinter simple_example.py")

button_properties = {
    "fg_color": "#ffffff",
    "text_color": "#4D339E",
    "border_color": "#4D339E",
    "border_width": 2,
    "hover": "disable",
    "corner_radius": 5,
    "width": 200,
    "font": ("Poppins",18)

}

takePictureButton = customtkinter.CTkButton(master=app, text="Take Picture", **button_properties,
command=(lambda: getDataFromCamera(takePics))
)
takePictureButton.pack(pady=10)

textbox = customtkinter.CTkTextbox(app,activate_scrollbars=False, 
    text_color="#ffffff", fg_color="#484040"
)
textbox.insert("0.0", "0\n")  
textbox.pack()


count = 0
IMAGE_SIZE = 224
current_dir = os.getcwd()
name = "yezarniko"
number_of_images_you_want = 300
train_dir = os.path.join(current_dir, "train")
train_dir_IMAGE_SIZE = os.path.join(train_dir, str(IMAGE_SIZE))
personID = len(os.listdir(train_dir_IMAGE_SIZE)) + 1
train_data_path = os.path.join(train_dir_IMAGE_SIZE, f"s{personID}")
color = (0, 255, 0)


# if not os.path.exists(train_dir):
#     os.mkdir(train_dir)
#     if not os.path.exists(train_dir_IMAGE_SIZE):
#         os.mkdir(train_dir_IMAGE_SIZE)

# if not os.path.exists(train_data_path):
#     os.mkdir(train_data_path)
# else:
#     resp = input("Do you want to overwrite: ")
#     if(resp == 'y'):
#         shutil.rmtree(train_data_path)
#         os.mkdir(train_data_path)
#     else:
#         sys.exit()

def save_img(img_frame, file_name):
    global count
    img = Image.fromarray(img_frame)    
    img.save(f"{train_data_path}/{file_name}.jpg")
    print(count)


def takePics(img_test, frame, faceRect):
    global count,textbox
    x, y, w, h = faceRect
    cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, thickness = 2)
    # save_img(img_test, count)
    if count == 0:
        pass
    else:
        print(textbox)
        textbox.insert("end", f"{count}\n")
        textbox.pack()
        # print(count)
    if count == number_of_images_you_want:
        sys.exit()
    count += 1


app.mainloop()

# def b():

# def a():
#     # getDataFromCamera(takePics)
#     pass

# t1 = threading.Thread(target=a)
# t2 = threading.Thread(target=b)

# # starting thread 1
# t1.start()
# # starting thread 2
# t2.start()

# # wait until thread 1 is completely executed
# t1.join()
# # wait until thread 2 is completely executed
# t2.join()

# # both threads completely executed
# print("Done!")