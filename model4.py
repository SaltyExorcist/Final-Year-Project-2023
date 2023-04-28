import tensorflow as tf
pretrained_model_path = "./models/Detect_Model_v2_Better.h5"

def predict_disease(img):
  
    # labels for each distinct category 
    labels = {0:'Bacterial Pneumonia',
              1:'Corona Virus Disease',
              2:'Normal',
              3:'Tuberculosis',
              4:'Viral Pneumonia'}

    # loading the model 
    model = tf.keras.models.load_model(pretrained_model_path)

    # Preprocessing
    img = tf.image.resize(img, [224, 224]) # resize the image
    img = tf.keras.utils.img_to_array(img)

    # Normalisation 
    img = img/255.
    img = tf.expand_dims(img, axis=0)

    # Make prediction 
    pred = model.predict(img, verbose=0)

    # Converting probabilities to percentage values 
    pred_percent =  {label: round(pred[0][i]*100, 2) for i, label in labels.items()}

    return pred_percent