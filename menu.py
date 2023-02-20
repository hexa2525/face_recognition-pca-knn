import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
  
  def __init__(self):
    super().__init__()
    self.title("Welcome")
    self.configure(fg_color="#ffffff")
    self.resizable(False, False)  # This code helps to disable windows from resizing
    window_height = 480
    window_width = 330
    screen_width =  self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    img = Image.open("menu_icon.png")
    img = customtkinter.CTkImage(light_image=img, size=(200,220))

    icon_img = customtkinter.CTkLabel(self, text="", image=img)
    icon_img.pack(pady=30)

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

    takePictureButton = customtkinter.CTkButton(master=self, text="Take Picture", **button_properties)
    takePictureButton.pack(pady=10)
    
    trainDatasetButton = customtkinter.CTkButton(master=self,  text="Train Dataset", **button_properties)
    trainDatasetButton.pack(pady=10)

    recognizeButton = customtkinter.CTkButton(master=self, text="Face Recoginze", **button_properties)
    recognizeButton.pack(pady=10)



app = App()
app.mainloop()