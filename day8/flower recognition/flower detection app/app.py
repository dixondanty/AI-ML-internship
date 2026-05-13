import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model
model = tf.keras.models.load_model("flower_model.keras")

# Class labels
class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

# App title
st.title("Flower Classification App")

st.write("Upload a flower image and the model will predict its class.")

# Upload imagea
uploaded_file = st.file_uploader(
    "Choose a flower image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    # Display uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Resize image
    image = image.resize((150, 150))

    # Convert image to array
    img_array = np.array(image)

    # Normalize image
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)

    predicted_class = class_names[np.argmax(prediction)]

    confidence = np.max(prediction) * 100

    # Display prediction
    st.subheader(f"Prediction: {predicted_class}")

    st.write(f"Confidence: {confidence:.2f}%")
