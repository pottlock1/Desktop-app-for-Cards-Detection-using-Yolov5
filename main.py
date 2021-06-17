from tkinter import *
from predict import Predict
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import os


prediction = Predict()
def single_predict():
    image_path = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select Image', filetypes = (('JPG File','*.jpg'), ('PNG File', '*.png'), ('All Files', '*.*')))
    img = prediction.single_predict(image_path)
    img = Image.fromarray(img)
    img = img.resize((500, 350))
    img = ImageTk.PhotoImage(img)
    img_lbl.configure(image = img)
    img_lbl.image = img

def live_cam():
    prediction.live_predict()


root = Tk()
root.geometry('900x500')
root.title('Card Detection')

frm1 = Frame(root, bd = 5, bg = 'white')
frm1.place(bordermode = OUTSIDE, height = 250, width = 550, x = 0, y = 0)

lbl1 = Label(frm1, text = 'Click here for single image test', bd = 5, bg = 'black', fg = 'white',font = ('times new roman', 20, 'bold'))
lbl1.pack(fill = X)

btn1 = Button(frm1, text = 'Browse Image', command = single_predict)
btn1.place(x = 225, y = 125)

frm2 = Frame(root, bd = 5, bg = 'pink')
frm2.place(bordermode = OUTSIDE, height = 250, width = 550, x = 0, y = 250)

lbl2 = Label(frm2, text = 'Click here for live testing', bd = 5, bg = 'black', fg = 'white', font = ('times new roman', 20, 'bold'))
lbl2.pack(fill = X)

btn2 = Button(frm2, text = 'Open Camera', command = live_cam)
btn2.place(x = 225, y = 125)

frm3 = Frame(root, bd = 5, bg = 'skyblue')
frm3.place(bordermode = OUTSIDE, height = 500, width = 350, x = 550, y = 0)

img_lbl = Label(frm3, bd = 5)
img_lbl.pack(fill = BOTH)

root.mainloop()






