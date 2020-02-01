from tkinter import *
from PIL import ImageTk, Image







root = Tk()
root.title("Demo")
root.geometry("100x100")
root.iconbitmap("c:\Gui\snowstorm.ico")
image_loc ="C:/Users/Robert/Pictures/weather.png"
img = ImageTk.PhotoImage(Image.open(r"C:/Users/Robert/Pictures/weather.png"))



myLabel = Label(image=img)
myLabel.pack()


root.mainloop()

