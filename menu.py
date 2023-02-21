import customtkinter
from PIL import Image
from takePictures import TakePictures
from train import TD

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Menu(customtkinter.CTkToplevel):
  
  def __init__(self, root):
    super().__init__(root)
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
    self.withdraw()
    self.protocol("WM_DELETE_WINDOW", lambda: root.destroy())


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




    takePictureObj = TakePictures(root)
    TDObj = TD(root)

    takePictureButton = customtkinter.CTkButton(master=self, text="Take Picture", **button_properties,
    command=lambda: self.buttonCallbackd(takePictureObj)
    )
    takePictureButton.pack(pady=10)
    
    trainDatasetButton = customtkinter.CTkButton(master=self,  text="Train Dataset", **button_properties,
    command=lambda: self.buttonCallbackd(TDObj)
    )
    trainDatasetButton.pack(pady=10)

    recognizeButton = customtkinter.CTkButton(master=self, text="Face Recoginze", **button_properties,
    command=lambda: self.buttonCallback("test"))
    recognizeButton.pack(pady=10)

    # def switch_windows():
    #   self.withdraw()
    #   root.deiconify()
    #   root.grab_set()
    # welcomeButton = customtkinter.CTkButton(master=self, text="Welcome", **button_properties,
    # command=switch_windows)
    # welcomeButton.pack(pady=10)


  def buttonCallbackd(self, new_window):
    self.withdraw()
    new_window.deiconify()
    new_window.grab_set()
  
  def buttonCallback(self, page):
    self.destroy()
    __import__(page)