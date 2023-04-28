import tensorflow as tf
pretrained_model_path = "./models/Detect_Model_v2_Better.h5"
# put this in model.py
def predict_disease(path):
  

    # labels for each distinct category 
    labels = {0:'Bacterial Pneumonia',
 1:'Corona Virus Disease',
 2:'Normal',
 3:'Tuberculosis',
 4:'Viral Pneumonia'}

    # loading the model 
    model = tf.keras.models.load_model(pretrained_model_path)

    # loading the image from given path
    img = tf.keras.preprocessing.image.load_img(path, target_size=(224, 224))

    # Preprocessing
    img = tf.keras.utils.img_to_array(img)

    # Normalisation 
    img /= 255.
    img = tf.expand_dims(img, axis=0)

    # Make prediction 
    pred = model.predict(img, verbose=0)

    # Converting probabilities to percentage values 
    pred_percent =  {label: round(pred[0][i]*100, 2) for i, label in labels.items()}

    return pred_percent