
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/choleburbank/projects/face_recognition-pca-knn/TEST/build/assets/frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    215.0,
    188.0,
    784.0,
    770.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    272.0,
    633.0,
    462.0,
    710.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    261.0,
    236.0,
    738.0,
    573.0,
    fill="#484040",
    outline="")

canvas.create_text(
    282.0,
    276.0,
    anchor="nw",
    text="Before PCA Transform\n[[ 34  34  34 ... 129 129 128]\n [ 40  39  38 ... 125 127 127]\n [ 25  24  24 ... 156 156 156]\n ...\n [116 106  91 ...  47  51  55]\n [120 116 103 ...  51  54  56]\n [128 128 125 ...  68  74  79]]\n\nnumber of values in one image: 50176",
    fill="#FFFFFF",
    font=("UbuntuMono Bold", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
