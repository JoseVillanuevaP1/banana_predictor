import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore

# ====================
# RUTAS DEL DATASET
# ====================
train_dir = 'train'
val_dir = 'valid'

# ====================
# PARÁMETROS
# ====================
IMG_SIZE = (416, 416)
BATCH_SIZE = 16
EPOCHS = 10
CLASSES = ['unripe', 'ripe', 'overripe']

# ====================
# CARGA DE DATOS
# ====================
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    classes=CLASSES,
    class_mode='sparse'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    classes=CLASSES,
    class_mode='sparse'
)

# ====================
# DEFINICIÓN DEL MODELO
# ====================
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')  # 3 clases
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# ====================
# ENTRENAMIENTO
# ====================
model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=EPOCHS
)
 
# ====================
# GUARDAR MODELO
# ====================
model.save("banana_ripeness_model.h5")
print("Modelo guardado como banana_ripeness_model.h5")
