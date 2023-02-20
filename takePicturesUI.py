import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
  
  def __init__(self):
    super().__init__()
    self.title("Take Picture")
    self.configure(fg_color="#ffffff")
    self.resizable(False, False)  # This code helps to disable windows from resizing
    window_height = 600
    window_width = 864
    screen_width =  self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    img = Image.open("0.jpg")
    img = img.resize(40,40)
    img = customtkinter.CTkImage(light_image=img)

    icon_img = customtkinter.CTkLabel(self, text="", image=img, size=(40,40))
    icon_img.grid(row=0,column=0,pady=20,padx=20)

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




app = App()
app.mainloop()