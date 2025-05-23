import tensorflow as tf
import numpy as np
import serial
import time
from tensorflow.keras.preprocessing.image import load_img, img_to_array # type: ignore

# ====================
# CONFIGURACIÓN DEL MODELO
# ====================
MODEL_PATH = 'banana_ripeness_model.h5'
IMG_SIZE = (416, 416)
CLASSES = ['unripe', 'ripe', 'overripe']

# ====================
# CARGAR MODELO
# ====================
model = tf.keras.models.load_model(MODEL_PATH)

# ====================
# ABRIR PUERTO SERIE (COM3)
# ====================
ser = serial.Serial('COM3', 9600)
time.sleep(1)

# ====================
# FUNCIÓN DE PREDICCIÓN
# ====================
def predict_image(image_path):
    img = load_img(image_path, target_size=IMG_SIZE)
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    label = CLASSES[class_index]

    return label

# ====================
# EJEMPLO DE USO
# ====================
image_path = 'test_overripe.jpg'  # pon la imagen del plátano aquí
estado = predict_image(image_path)

estado_letra = {
    'unripe': 'U',
    'ripe': 'R',
    'overripe': 'O'
}[estado]

# ====================
# ENVIAR AL COM3
# ====================
print(f"Estado del plátano: {estado}")
print(estado_letra.encode())
ser.write(estado_letra.encode())
ser.close()
