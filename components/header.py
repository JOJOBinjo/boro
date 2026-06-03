import streamlit as st

def render_header():

    st.markdown("""
    <div style="
    height:4px;
    background:linear-gradient(
    90deg,
    #5B4CF0,
    #7C6CFF,
    #9F93FF
    );
    border-radius:999px;
    margin-bottom:40px;
    ">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="title-main">
        Baroque Vision AI
    </div>

    <div class="subtitle-main">
        Загрузите изображение картины и получите анализ художественного стиля.
        Модель определит принадлежность к эпохе Барокко и покажет похожие произведения.
    </div>
    """, unsafe_allow_html=True)