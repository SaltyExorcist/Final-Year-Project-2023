import tkinter as tk
from tkinter import filedialog
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from PIL import ImageTk, Image

from model3 import predict_disease

root = ttk.Window(themename="pulse")

root.title("ML Project")
# root.iconbitmap('')
root.geometry("1300x1000")
root.minsize(620, 850)
# root.maxsize(1000, 1000)

# All styles
# For input button
in_style = ttk.Style()
in_style.configure('info.Outline.TButton', font=("forte", 20))
# For Submit button
sub_style = ttk.Style()
sub_style.configure('success.TButton', font=("Consolas", 13))
# For Reset button
res_style = ttk.Style()
res_style.configure('danger.TButton', font=("Consolas", 13))


# from model import predict_disease
image = None
cvdm = 0
pnm = 0
tbm = 0
nm = 0

# To Change theme


def chgtheme():
    global sub_style, res_style
    if tb.get() == 0:
        root.style.theme_use("pulse")
        # Input Button
        light_style = ttk.Style()
        light_style.configure('info.Outline.TButton', font=("forte", 20))
        input_button.configure(style="info.Outline.TButton")
        # Submit Button
        light_sub_style = ttk.Style()
        light_sub_style.configure('success.TButton', font=("Consolas", 13))
        submit_button.configure(style="success.TButton")
        # Reset Button
        light_res_style = ttk.Style()
        light_res_style.configure('danger.TButton', font=("Consolas", 13))
        reset_button.configure(style="danger.TButton")

    else:
        root.style.theme_use("cyborg")
        # Input Button
        dark_style = ttk.Style()
        dark_style.configure('info.Outline.TButton', font=("forte", 20))
        input_button.configure(style="info.Outline.TButton")
        # Submit Button
        dark_sub_style = ttk.Style()
        dark_sub_style.configure('success.TButton', font=("Consolas", 13))
        submit_button.configure(style="success.TButton")
        # Reset Button
        dark_res_style = ttk.Style()
        dark_res_style.configure('danger.TButton', font=("Consolas", 13))
        reset_button.configure(style="danger.TButton")

# Openning required image and resizing it


def open_image():
    global image_path, image_display, image
    image_path = filedialog.askopenfilename()
    image = Image.open(image_path)
    image = image.resize((652, 485), Image.ANTIALIAS)
    input_button.image = ImageTk.PhotoImage(image)
    input_button.config(image=input_button.image, padding=(0, 0))


# Calculating Probability
def make_prediction():
    global cvdm, pnm, tbm, nm

    prediction = predict_disease(image)
    cvdm = round(list(prediction.values())[0], 2)
    nm = round(list(prediction.values())[1], 2)
    pnm = round(list(prediction.values())[2], 2)
    tbm = round(list(prediction.values())[3], 2)
    covid_meter.configure(amountused=cvdm)
    pneumonia_meter.configure(amountused=pnm)
    tuberculosis_meter.configure(amountused=tbm)
    normal_meter.configure(amountused=nm)


# To Reset Everything
def clear_all():
    global input_button, cvdm, pnm, tbm, nm
    cvdm = 0
    pnm = 0
    tbm = 0
    nm = 0
    input_button.configure(text="Select the Image",
                           image="", padding=(152, 224))

    covid_meter.configure(amountused=cvdm)
    pneumonia_meter.configure(amountused=pnm)
    tuberculosis_meter.configure(amountused=tbm)
    normal_meter.configure(amountused=nm)


tb = ttk.IntVar()
theme_button = ttk.Checkbutton(text="Change Theme", bootstyle="info-square-toggle",
                               variable=tb, onvalue=1, offvalue=0, command=chgtheme)
theme_button.grid(row=0, column=0, sticky="e")

# Input Part
# Creating Label to Seperate
input_label = ttk.Labelframe(
    root, text="Input", padding=(8, 8), style="success.TLabelframe")
input_label.grid(row=1, column=0, padx=20, pady=10)

# Input Button
input_button = ttk.Button(input_label, text="Select the Image", padding=(
    152, 224), width=20, style="info.Outline.TButton", command=open_image)
input_button.grid(row=0, column=0, pady=20, padx=20)

# Submit Button
submit_button = ttk.Button(input_label, text="Submit", padding=(
    80, 20), width=15, style="success.TButton", command=make_prediction)
submit_button.grid(row=1, column=0, pady=20, padx=20, sticky="w")

# Reset Button
reset_button = ttk.Button(input_label, text="Reset", padding=(
    60, 20), width=5, style="danger.TButton", command=clear_all)
reset_button.grid(row=1, column=0, pady=20, padx=20, sticky="e")

# Result Part
# Creating Label to Seperate
result_label = ttk.Labelframe(
    root, text="Result", padding=(8, 8), style="info.TLabelframe")
result_label.grid(row=1, column=1, padx=8, pady=10)

# Meter for Covid
covid_meter = ttk.Meter(result_label, bootstyle="success", subtext="Covid", interactive=False,
                        textright="%", metertype="full", stripethickness=10, metersize=130, padding=4,
                        amounttotal=100, subtextstyle="danger", amountused=cvdm)
covid_meter.grid(row=0, column=0, padx=4, pady=4)

# Meter for Pneumonia
pneumonia_meter = ttk.Meter(result_label, bootstyle="success", subtext="Pneumonia", interactive=False,
                            textright="%", metertype="full", stripethickness=10, metersize=130, padding=4,
                            amounttotal=100, subtextstyle="danger", amountused=pnm)
pneumonia_meter.grid(row=0, column=1, padx=4, pady=4)

# Meter for Tuberculosis
tuberculosis_meter = ttk.Meter(result_label, bootstyle="success", subtext="Tubelculosis", interactive=False,
                               textright="%", metertype="full", stripethickness=10, metersize=130, padding=4,
                               amounttotal=100, subtextstyle="danger", amountused=tbm)
tuberculosis_meter.grid(row=1, column=0, padx=4, pady=4)

# Meter for Normal
normal_meter = ttk.Meter(result_label, bootstyle="success", subtext="Normal", interactive=False,
                         textright="%", metertype="full", stripethickness=10, metersize=130, padding=4,
                         amounttotal=100, subtextstyle="danger", amountused=nm)
normal_meter.grid(row=1, column=1, padx=4, pady=4)

root.mainloop()
