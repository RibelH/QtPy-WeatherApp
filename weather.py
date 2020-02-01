from pprint import pprint
from tkinter import *

import requests
from PIL import ImageTk, Image


def img_d(descrip):
    images = ["c:\Gui\cloudy_sun.png", "c:\Gui\sun.png", "c:\Gui\\rain.png"]

    if "rain" in descrip:
        return images[2]
    elif "clear sky" in descrip:
        return images[1]
    elif "cloud" in descrip:
        return images[0]
    else:
        return images[0]


def info():
    city = "Kreuzlingen"

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=ac7c75b9937a495021393024d0a90c44&units=metric".format(
        city)

    res = requests.get(url)

    data = res.json()

    temp = str(data["main"]["temp"])
    desc = data["weather"][0]["description"]

    result = "Die Temperatur in {} beträgt:\n".format(city) + (28 + len(city)) * "-"
    pprint(data)

    return result, temp, desc

def color_grad(temp_num):
    if temp_num > 10:
        return "#E62600"
    elif temp_num >0:
        return "#FF8C00"
    else:
        return "#0055FF"


# pprint(data)
def weather(para):
    print(para)
    root = Tk()
    root.title("Weather")
    root.iconbitmap("c:\Gui\snowstorm.ico")
    root.geometry("230x150")

    # images
    image_loc = img_d(para[2])
    image_desc = ImageTk.PhotoImage(Image.open(image_loc))

    #Title Font
    # T =  Text(root)
    # T.configure(font=("Arial", 12, "bold", "italic"))
    # T.grid(row=0, column=0, columnspan=3)
    # T.insert(END, para[0])

    #Title
    myLabel_t = Label(root, text=para[0])
    myLabel_t.grid(row=0, column=0, columnspan=3)

    # Creating and packing frames
    frame_t = LabelFrame(root, text="Temperature", padx=25, relief=RIDGE)
    frame_t.grid(row=1, column=1)

    frame_d = LabelFrame(root, text="Description", padx=20, cursor="circle", relief=RIDGE)
    frame_d.grid(row=2, column=1)

    # color grading for negative and positive temperature
    clr = color_grad(float(para[1]))

    # Defining and Packing Temperature number in Frame
    myLabel = Label(frame_t, text=para[1] + "°C", fg=clr, )
    myLabel.pack()


    # Weather description Label
    desc_l = para[2].split()
    new_desc=""
    desc_l[0] = desc_l[0].capitalize()

    for word in desc_l:
        new_desc = new_desc + " "+ word


    descLabel = Label(frame_d, text=new_desc, )
    descLabel.pack()

    # Image to description

    imageL = Label(image=image_desc)
    imageL.grid(row=1, column=2, rowspan=2)

    # Button Exit
    ExButton = Button(root, text="Close", command=root.quit)
    ExButton.grid(row=3, column=1)
    root.mainloop()


weather(info())
