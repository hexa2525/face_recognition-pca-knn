import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
  
  def __init__(self):
    super().__init__()
    self.title("Welcome")
    # self.configure(fg_color="#ffffff")
    self.resizable(False, False)  # This code helps to disable windows from resizing
    window_height = 540
    window_width = 900
    screen_width =  self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    bgImg = Image.open("Frame 1.png")
    bgImg = customtkinter.CTkImage(light_image=bgImg, size=(window_width,window_height))
    label1 = customtkinter.CTkLabel(self, text="", image=bgImg)
    label1.pack()
    
    button = customtkinter.CTkButton(master=self, width=100, text="Continue", fg_color="#ffffff", text_color="#4D339E", border_color="#4D339E",
    border_width=2, hover="disable", corner_radius=50)
    button.place(x=200, y=320)




app = App()
app.mainloop()