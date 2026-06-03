import streamlit as st
from PIL import Image

def render_uploader():

    left, right = st.columns([1, 1])

    uploaded_file = None

    with left:

        card = st.container(border=True)


        with card:

            st.subheader("Загрузить картину")

            uploaded_file = st.file_uploader(
                "",
                type=["jpg", "jpeg", "png", "webp"]
            )

            mode = st.radio(
                "Режим анализа",
                [
                    "Определение Барокко",
                    "Сходство с Барокко",
                    "Полный анализ"
                ]
            )

            analyze = st.button(
                "Начать анализ",
                use_container_width=True
            )


    with right:

        if uploaded_file:

            image = Image.open(uploaded_file)

            st.image(
                image,
                use_container_width=True
            )

        else:

            st.image(
                "preview.jpg",
                use_container_width=True
            )

    return uploaded_file, analyze, mode