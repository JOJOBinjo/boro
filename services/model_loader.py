import tensorflow as tf
import streamlit as st

@st.cache_resource
def load_model():

    model = tf.keras.models.load_model(
        "models/baroque_model.h5"
    )

    return model