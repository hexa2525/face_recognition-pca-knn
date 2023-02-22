import os
import threading
import sys
import json
from PIL import Image
from face_detect import getDataFromCamera
import shutil
import customtkinter
import cv2
from train import TD

customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# app = customtkinter.CTk()

IMAGE_SIZE = 224
current_dir = os.getcwd()
train_dir = os.path.join(current_dir, "train")
train_dir_IMAGE_SIZE = os.path.join(train_dir, str(IMAGE_SIZE))


class TakePictures(customtkinter.CTkToplevel):
    def __init__(self, root):

        self.count = 0
        self.name = ""
        self.number_of_images_you_want = 300

        super().__init__()
        self.root = root
        self.geometry("300x340")
        self.configure(fg_color="#ffffff")
        self.resizable(False, False)  # This code helps to disable windows from resizing
        self.title("Take Picture")
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())
        button_properties = {
            "fg_color": "#ffffff",
            "text_color": "#4D339E",
            "border_color": "#4D339E",
            "border_width": 2,
            "hover": "disable",
            "corner_radius": 5,
            "width": 20,

        }

        self.t1 = threading.Thread(target=lambda:getDataFromCamera(self.takePics) )
        def takePictureButtonCallback():
            if not os.path.exists(train_dir):
                os.mkdir(train_dir)
                if not os.path.exists(train_dir_IMAGE_SIZE):
                    os.mkdir(train_dir_IMAGE_SIZE)

            personID = len(os.listdir(train_dir_IMAGE_SIZE)) + 1
            self.train_data_path = os.path.join(train_dir_IMAGE_SIZE, f"s{personID}")

            if not os.path.exists(self.train_data_path):
                os.mkdir(self.train_data_path)
            else:
                resp = input("Do you want to overwrite: ")
                if(resp == 'y'):
                    shutil.rmtree(self.train_data_path)
                    os.mkdir(self.train_data_path)
                else:
                    sys.exit()


            if personID == 1:
                with open("persons_data.json", "w") as persons_data:
                    persons_data.write("{}")

            with open("persons_data.json", "r") as persons_data_r:
                p_data = json.load(persons_data_r)
                p_data[f"s{personID}"] = self.name
            
            with open("persons_data.json", "w") as persons_data_w:
                persons_data_w.write(json.dumps(p_data, indent=4))

            self.t1.start()
            takePictureButton.pack_forget()

        takePictureButton = customtkinter.CTkButton(master=self, text="Take Picture", **button_properties,
        font=("Poppins",18),command=takePictureButtonCallback)

        self.textbox = customtkinter.CTkTextbox(self,activate_scrollbars=False, 
            text_color="#ffffff", fg_color="#484040")

        self.textbox.insert("0.0", "0\n")  
        self.textbox.pack(pady=20)

        entry_frame = customtkinter.CTkFrame(master=self)
        entry_frame.pack(pady=10)

        entry_1 = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Enter your name",corner_radius=0)
        entry_1.grid(row=1,column=1)


        name_label = customtkinter.CTkLabel(master=self, text="",
        font=("Poppins",16))


        def okButtonCallback():
            self.name = entry_1.get()
            name_label.configure(text=f"name: {self.name}")
            takePictureButton.pack_forget()
            name_label.pack(pady=10)
            takePictureButton.pack()
            entry_frame.pack_forget()
        okButton = customtkinter.CTkButton(master=entry_frame, text="ok",width=20,corner_radius=0,
        command=okButtonCallback)
        okButton.grid(row=1,column=2)
    
        def trainButtonCallback():
            TDObj = TD(root)
            self.withdraw()
            TDObj.deiconify()
            TDObj.grab_set()
        
        self.trainDatasetButton = customtkinter.CTkButton(master=self,  text="Train Dataset", **button_properties,
        command=trainButtonCallback
        )


    def save_img(self, img_frame, file_name):
        img = Image.fromarray(img_frame)    
        img.save(f"{self.train_data_path}/{file_name}.jpg")


    def takePics(self, img_test, frame, faceRect, cap):
        x, y, w, h = faceRect
        color = (0, 255, 0)
        cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, thickness = 2)
            # print(count)
        if self.count != self.number_of_images_you_want:
            if self.count == 0:
                pass
            else:
                self.textbox.insert("end", f"{self.count}\n")
            self.textbox.yview("end")
            self.save_img(img_test, self.count)
            self.count += 1
        else:
            self.textbox.insert("end", f"finished\n")
            self.trainDatasetButton.pack()


# app.mainloop()

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