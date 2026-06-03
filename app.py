import streamlit as st
from PIL import Image

from utils.styles import load_css
from components.header import render_header
from components.uploader import render_uploader
from components.results import render_results

st.set_page_config(
    page_title="Baroque Vision",
    page_icon="🎨",
    layout="wide"
)

load_css()

render_header()

uploaded_file, analyze, mode = render_uploader()

if analyze and uploaded_file:

    image = Image.open(uploaded_file)

    render_results(image, mode)