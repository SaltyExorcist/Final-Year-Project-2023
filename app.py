import tkinter as tk
from tkinter import filedialog
import tkinter
from PIL import ImageTk, Image

from model import predict_disease

image = None

# Define a function to open the file dialog and select an image


def open_image():
    global image_path, image_display, image
    image_path = filedialog.askopenfilename()
    image = Image.open(image_path)
    image = image.resize((400, 400), Image.ANTIALIAS)
    image_display.image = ImageTk.PhotoImage(image)
    image_display.config(image=image_display.image)

# Define a function to make a prediction using the pre-trained model


def make_prediction():
    # Load the pre-trained model and make a prediction using the selected image
    global image
    # Make prediction
    prediction = predict_disease(image)
    tkinter.messagebox.showwarning(
        title="prediction!", message=prediction)


# Create the main window
root = tk.Tk()

# Create the image viewer
image_display = tk.Label(root)
image_display.pack()

# Create the "Select Image" button
select_button = tk.Button(root, text="Select Image", command=open_image)
select_button.pack()

# Create the "Predict" button
predict_button = tk.Button(root, text="Predict", command=make_prediction)
predict_button.pack()

# Run the main loop
root.mainloop()
