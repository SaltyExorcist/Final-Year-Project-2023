import tkinter as tk
from tkinter import filedialog
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from PIL import ImageTk, Image

from model1 import predict_disease

image = None
theme="cyborg"
m1=0
m2=0
m3=0
m4=0

#Openning required image and resizing it
def open_image():
    global image_path, image_display, image
    image_path = filedialog.askopenfilename()
    image = Image.open(image_path)
    image = image.resize((652, 485), Image.ANTIALIAS)
    input_button.image = ImageTk.PhotoImage(image)
    input_button.config(image=input_button.image,padding=(0,0))

#Calculating Probability
def make_prediction():
    global image
    global m1,m2,m3,m4
    prediction = predict_disease(image)
    m1=list(prediction.values())[0]
    m2=list(prediction.values())[1]
    m3=list(prediction.values())[2]
    m4=list(prediction.values())[3]

def clearimage():
    global input_button
    input_button.configure(text="Select the Image",image="",padding=(152,224))


root = ttk.Window(themename=theme)
root.title("ML Project")
#root.iconbitmap('')
root.geometry("773x1000")
root.minsize(620,850)
root.maxsize(773,1000)


#Input Part
#Creating Label to Seperate
input_label = ttk.Labelframe(root,text="Input",padding=(8,8),style="success.TLabelframe")
input_label.grid(row=0,column=0,padx=20,pady=10)

#Input Button
in_style = ttk.Style()
in_style.configure('info.Outline.TButton',font=("forte",20))
input_button = ttk.Button(input_label,text="Select the Image",padding=(152,224),width=20,style="info.Outline.TButton",command=open_image)
input_button.grid(row=0,column=0,pady=20,padx=20)

#Submit Button
sub_style = ttk.Style()
sub_style.configure('success.TButton',font=("Consolas",13))
submit_button = ttk.Button(input_label,text="Submit",padding=(80,20),width=15,style="success.TButton",command=make_prediction)
submit_button.grid(row=1,column=0,pady=20,padx=20,sticky="w")

#Reset Button
res_style = ttk.Style()
res_style.configure('danger.TButton',font=("Consolas",13))
reset_button = ttk.Button(input_label,text="Reset",padding=(60,20),width=5,style="danger.TButton",command=clearimage)
reset_button.grid(row=1,column=0,pady=20,padx=20,sticky="e")

#Result Part
#Creating Label to Seperate
result_label = ttk.Labelframe(root,text="Result",padding=(8,8),style="info.TLabelframe")
result_label.grid(row=1,column=0,padx=20,pady=10)

#Meter for m1
meter1= ttk.Meter(result_label, bootstyle="success",subtext="1stResult",interactive=False,
                 textright="%",metertype="full",stripethickness=10,metersize=130,padding=4,
                 amounttotal=100,subtextstyle="danger",amountused=m1)
meter1.grid(row=0,column=0,padx=4,pady=4)

#Meter for m2
meter2= ttk.Meter(result_label, bootstyle="success",subtext="2ndResult",interactive=False,
                 textright="%",metertype="full",stripethickness=10,metersize=130,padding=4,
                 amounttotal=100,subtextstyle="danger",amountused=m2)
meter2.grid(row=0,column=1,padx=4,pady=4)

#Meter for m3
meter3= ttk.Meter(result_label, bootstyle="success",subtext="3rdResult",interactive=False,
                 textright="%",metertype="full",stripethickness=10,metersize=130,padding=4,
                 amounttotal=100,subtextstyle="danger",amountused=m3)
meter3.grid(row=0,column=2,padx=4,pady=4)

#Meter for m4
meter4= ttk.Meter(result_label, bootstyle="success",subtext="4thResult",interactive=False,
                 textright="%",metertype="full",stripethickness=10,metersize=130,padding=4,
                 amounttotal=100,subtextstyle="danger",amountused=m4)
meter4.grid(row=0,column=3,padx=4,pady=4)

root.mainloop();