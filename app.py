import tkinter as tk
import numpy as np
import cv2
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import ImageTk,Image,ImageDraw
from urllib.request import urlopen
import time

import tensorflow as tf

model = tf.keras.models.load_model('MNIST_model.h5')

def event_function(event):
    
    x=event.x
    y=event.y
    
    x1=x-20
    y1=y-20
    x2=x+20
    y2=y+20

    canvas.create_oval((x1,y1,x2,y2),fill='black')
    img_draw.ellipse((x1,y1,x2,y2),fill='white')

def save():
    
    img_array=np.array(img)
    img_array=cv2.resize(img_array,(256,256)) 
    cv2.imwrite(str(time.time())+'image.jpg',img_array)
    messagebox.showinfo("Save", "Image saved successfully !")


def clear():
    
    global img,img_draw
    canvas.delete('all')
    img=Image.new('RGB',(500,500),(0,0,0))
    img_draw=ImageDraw.Draw(img)    
    entry.delete(0 , tk.END)
    label_status.config(text='Draw a Digit')


def upload():

    global img , dispimg
    path=fd.askopenfilename(filetypes=[("Image File",'.jpg')])
    img = Image.open(path)
    dispimg = ImageTk.PhotoImage(img.resize((400,400)))
    canvas.create_image(250,250,image= dispimg)
    predict()


def predict():

    global img , dispimg
    if(len(str(entry.get())) > 5 ):
        img = Image.open(urlopen(str(entry.get())))
        dispimg = ImageTk.PhotoImage(img.resize((400,400)))
        canvas.create_image(250,250,image= dispimg)


    img_array=np.array(img)
    img_array=cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
    img_array=cv2.resize(img_array,(28,28))
        
    img_array=img_array/255.0
    img_array=img_array.reshape(-1,784)
    result=model.predict(img_array)
    label=np.argmax(result,axis=1)
    
    label_status.config(text='Predicted Digit :  '+str(label[0]))
    
    
win=tk.Tk()
win.title("MNIST Digit Prediction by Sahil Kavitake")
win.resizable(height=False,width=False)


label_status=tk.Label(win,text='Draw a Digit',bg='pink',font='Helvetica 24 bold')
label_status.grid(row=0,column=0,columnspan=4 )

canvas=tk.Canvas(win,width=500,height=500,bg='white')
canvas.grid(row=1,column=0,columnspan=4)

button_save=tk.Button(win,text='SAVE',bg='green',fg='white',font='Helvetica 20 bold',command=save)
button_save.grid(row=2,column=0)

button_predict=tk.Button(win,text='PREDICT',bg='blue',fg='white',font='Helvetica 20 bold',command = predict)
button_predict.grid(row=2,column=1)

button_clear=tk.Button(win,text='CLEAR',bg='cyan',fg='white',font='Helvetica 20 bold',command=clear)
button_clear.grid(row=2,column=2)

button_exit=tk.Button(win,text='UPLOAD',bg='red',fg='white',font='Helvetica 20 bold',command=upload)
button_exit.grid(row=2,column=3)

dummy = tk.Label(win, font = 'Helvetica 15 bold' , text=" ")
dummy.grid(row = 3 , column = 0)

label_link = tk.Label(win, font = 'Helvetica 13 bold' , text="Image link :")
label_link.grid(row = 4 , column = 0)


entry = tk.Entry(win , width = 60)
entry.grid(row=4, column = 1, columnspan=3)

dummy = tk.Label(win, font = 'Helvetica 15 bold' , text=" ")
dummy.grid(row = 5 , column = 0)

canvas.bind('<B1-Motion>',event_function)
img=Image.new('RGB',(500,500),(0,0,0))
img_draw=ImageDraw.Draw(img)

win.mainloop()