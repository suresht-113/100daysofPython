pip install tensorflow
pip install keras
pip install Pillow

import tensorflow as tf

# Path to the directory containing the pre-trained model
model_path = 'path/to/model/directory'

# Load the model
model = tf.keras.models.load_model(model_path)

from PIL import Image

# Path to the image file
image_path = 'path/to/image.jpg'

# Load the image using the Pillow library
image = Image.open(image_path)

import numpy as np

# Resize the image to the required dimensions
image = image.resize((299, 299))

# Convert the image to a NumPy array
image_array = np.array(image)
image_array = np.expand_dims(image_array, axis=0)

# Generate the caption
caption = model.predict(image_array)

# Convert the output from the model to text
caption_text = caption[0].decode('utf-8')

# Print the caption
print(caption_text)
