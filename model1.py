import tensorflow as tf
import numpy as np

pretrained_model_path = "./models/clf.h5"


def predict_disease(image_matrix):
    # Load pre-trained model
    model = tf.keras.models.load_model(pretrained_model_path)

    # Preprocess image
    preprocessed_image = preprocess_image(image_matrix)

    # Make prediction
    labels = ["COVID19", "NORMAL", "PNEUMONIA", "TUBERCULOSIS"]
    probabilities = model.predict(preprocessed_image).reshape(-1)
    pred = labels[np.argmax(probabilities)]
    return  {x:y*100 for x,y in zip(labels, probabilities)}


def preprocess_image(image_matrix):
    # Resize image to match pre-trained model input size
    resized_image = tf.image.resize(image_matrix, [200, 200])

    # Normalize pixel values to range [0, 1]
    normalized_image = resized_image / 255.0

    # Add batch dimension
    batched_image = tf.expand_dims(normalized_image, axis=0)

    return batched_image
