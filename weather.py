from pprint import pprint
from tkinter import *

import requests
from PIL import ImageTk, Image

images = []


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


# pprint(data)
def weather(para):
    print(para)
    root = Tk()
    root.title("Weather Frog")
    root.iconbitmap("c:\Gui\snowstorm.ico")


    #images
    image_desc = ImageTk.PhotoImage(Image.open("c:\Gui\weather.png"))

    myLabel_t = Label(root, text=para[0])
    myLabel_t.grid(row=0, column=0, columnspan=3)
    # Framing for Temp
    frame_t = LabelFrame(root, text="Temperature", padx=25, relief=RIDGE)
    frame_t.grid(row=1, column=1)

    frame_d = LabelFrame(root, text="Description", padx=20, cursor="circle", relief = RIDGE)
    frame_d.grid(row=2, column=1)
    # color grading for negative and positive temperature
    if float(para[1]) >= 0:
        myLabel = Label(frame_t, text=para[1] + "°C", fg="#FF8C00", )
        myLabel.pack()
    else:
        myLabel = Label(frame_t, text=para[1] + "°C", fg="blue")
        myLabel.pack()

    # Weather description Label
    descLabel = Label(frame_d, text=para[2],)
    descLabel.pack()

    #Image to description
    imageL= Label(image=image_desc)
    imageL.grid(row=2, column=2)

    # Button Exit
    ExButton = Button(root, text="Close", command=root.quit)
    ExButton.grid(row=3, column=1)
    root.mainloop()


weather(info())