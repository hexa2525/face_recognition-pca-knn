import numpy as np
from sklearn.decomposition import PCA
import os
import threading
import pickle as pk
import  pandas as pd

from data import LoadData
import customtkinter


class TD(customtkinter.CTkToplevel):
  
  def __init__(self, root):

    super().__init__()
    window_height = 500
    window_width = 500
    screen_width =  self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    self.root = root
    self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    self.configure(fg_color="#ffffff")
    self.resizable(False, False)  # This code helps to disable windows from resizing
    self.title("CustomTkinter simple_example.py")
    self.withdraw()
    self.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())

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
    textBox_properties = {
      "text_color": "#ffffff",
      "fg_color": "#484040",
      "width": 450,
      "height": 400,
      "font": ("Ubuntu Mono", 16)
    }

    textbox = customtkinter.CTkTextbox(self,activate_scrollbars=True, **textBox_properties)
    t1 = threading.Thread(target=lambda: self.train(textbox)) 
    
    def trainButtonCallback():
      t1.start()
      trainButton.pack_forget()

    trainButton = customtkinter.CTkButton(master=self, text="Train", **button_properties,
    command=trainButtonCallback)

    def saveButtonCallback():
      self.save_train_data()
      self.saveButton.pack_forget()
      textbox.insert("end","\nsaved!")
      textbox.yview("end")
      recognizeButton.pack()

    self.saveButton = customtkinter.CTkButton(master=self, text="save", **button_properties,
    command=saveButtonCallback)


    def recognizeButtonCallback(page):
      self.root.destroy()
      __import__(page)

    recognizeButton = customtkinter.CTkButton(master=self, text="Face Recoginze", **button_properties,
    command=lambda: recognizeButtonCallback("test"))

    textbox.pack(pady=20)
    trainButton.pack()

    # td.save_train_data()

  def train(self, textbox):

    """"
    Original Data Set
    224*224 = 50176 values in one image

    [168 150 137 ... 227 243 248]
    """
    self.Data, self.Label = LoadData()
    self.Data = np.asarray(self.Data)
    self.Label = np.asarray(self.Label)

    output = ""

    print(f"number of images: {len(self.Data)}")
    output += f"number of images: {len(self.Data)}\n"
    print("Before PCA Transform")
    output += "Before PCA Transform\n"
    print(self.Data)
    output +=  f"{self.Data}\n"
    print(f"number of values in one image: {len(self.Data[0])}")
    output += f"number of values in one image: {len(self.Data[0])}\n"

    textbox.insert("0.0", output)
    self.pca = PCA(n_components=0.9)
    self.trainDataS = self.pca.fit_transform(self.Data)

    print("After PCA Transform")
    textbox.insert("end", "\nAfter PCA Transform\n")

    print(self.trainDataS)
    textbox.insert("end", f"{self.trainDataS}\n")
    print(f"number of values in one image: {len(self.trainDataS[0])}\n")
    textbox.insert("end", f"number of values in one image: {len(self.trainDataS[0])}\n")
    textbox.insert("end","\nfinished")
    textbox.yview("end")
    self.saveButton.pack()
    # self.save_train_data()
    """
    PCA Transform
    0.9 -> 10 values in one image

    [ 11312.26086973  2283.70464563   788.50317713  -936.93123612
      10767.52238881  -1138.2489218   269.6564662   -690.08832049
      -960.30505439   -524.99817064
    ]
    """
  
  def save_train_data(self):
    pk.dump(self.pca, open(f"pca.pkl","wb"))
    pk.dump(self.trainDataS, open(f"trainDataS.pkl","wb"))
    pd.DataFrame(np.asarray(self.trainDataS)).to_csv(f"trainDataS.csv")

