from model4 import predict_disease
import cv2
image_path=r".\Final-Year-Project-2023\sample-images\person118_bacteria_559.jpeg"
image = cv2.imread(image_path)
prediction = predict_disease(image)
print("Prediction:", prediction)
print("-"*40)