import tensorflow as tf
pretrained_model_path = "./models/clf(2023-04-24 11_22).h5"
# put this in model.py
def predict_disease(path):
  
    """
    parameters:
    path - path to the image file.
    usage:
    >>> predict_disease("path to image.jpeg")
      {   
        'COVID19': 0.07, 
        'NORMAL': 4.06,
        'PNEUMONIA': 95.83, 
        'TURBERCULOSIS': 0.04
      }
    """

    # labels for each distinct category 
    labels = {0: 'COVID19', 1: 'NORMAL', 2: 'PNEUMONIA', 3: 'TURBERCULOSIS'} 

    # loading the model 
    model = tf.keras.models.load_model(pretrained_model_path)

    #resized_image = tf.image.resize(path, [100, 100,3])

    #loading the image from given path
    img = tf.keras.preprocessing.image.load_img(path, target_size=(100, 100,3), color_mode="grayscale")
    
    #img = tf.io.read_file(path)
    #img.get_shape().as_list()  # []
    #img = tf.image.decode_jpeg(img)
    #img.get_shape().as_list()  # [300, 400, 3]
    #img_resized = tf.image.resize(img, [100, 100])
    #img_resized.get_shape().as_list()  # [100, 100, 3]

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