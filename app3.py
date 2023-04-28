from model4 import predict_disease

image_path=r".\Final-Year-Project-2023\sample-images\person118_bacteria_559.jpeg"

prediction = predict_disease(image_path)
print("Image path is:", image_path)
print("Prediction:", prediction)
print("-"*40)

