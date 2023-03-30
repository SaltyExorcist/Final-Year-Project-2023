import tensorflow as tf

pretrained_model_path = "./models/clf.h5"


def predict_disease(image_matrix):
    # Load pre-trained model
    model = tf.keras.models.load_model(pretrained_model_path)

    # Preprocess image
    preprocessed_image = preprocess_image(image_matrix)

    # Make prediction
    prediction = model.predict(preprocessed_image)

    return prediction


def preprocess_image(image_matrix):
    # Resize image to match pre-trained model input size
    resized_image = tf.image.resize(image_matrix, [200, 200])

    # Normalize pixel values to range [0, 1]
    normalized_image = resized_image / 255.0

    # Add batch dimension
    batched_image = tf.expand_dims(normalized_image, axis=0)

    return batched_image
