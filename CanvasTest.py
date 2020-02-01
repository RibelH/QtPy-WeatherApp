from tkinter import *

root = Tk()

T = Text(root, height=2, width=30)
T.configure( font=("Arial", 12, "bold", "italic"))
T.pack()
T.insert(END, "Just a text Widget\nin two lines\n",)
quote = "Bblblbllbl"
T.insert(END, quote)

root.mainloop()
