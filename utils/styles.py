import streamlit as st

def load_css():

    st.markdown("""
    <style>
    



    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #111827 40%,
            #1e293b 100%
        );
    }

    .block-container{
        padding-top:4rem;
        max-width:1400px;
    }

    .title-main {
        text-align:center;
        font-size:58px;
        font-weight:800;
        color:white;
    }
    
    .subtitle-main {
        text-align:center;
        font-size:18px;
        color:#cbd5e1;
        max-width:900px;
        margin:auto;
        line-height:1.8;
        margin-bottom:50px;
    }

    .upload-box {
        background: rgba(30, 41, 59, 0.8);
        backdrop-filter: blur(12px);
    
        border: 1px solid rgba(255,255,255,0.08);
    
        border-radius: 24px;
        padding: 30px;
    
        box-shadow:
            0 10px 30px rgba(0,0,0,0.25);
    }
    
    .upload-box * {
        color: white !important;
    }   

    .gallery-title{
        font-size:30px;
        font-weight:800;
        margin-top:50px;
    }

    .score-number{
        font-size:72px;
        font-weight:800;
        color:#5B4CF0;
    }
    

    /* Карточки Streamlit */
    div[data-testid="stVerticalBlock"] {
        border-radius: 24px;
    }
    
    [data-testid="stContainer"] {
        background: #273449;
    
        border: 1px solid #3b4b63;
    
        border-radius: 24px;
    
        padding: 24px;
    
        box-shadow:
            0 10px 30px rgba(0,0,0,0.25);
    }

    .result-card {
        background: rgba(30, 41, 59, 0.9);
    
        border: 1px solid rgba(255,255,255,0.08);
    
        border-radius: 24px;
    
        box-shadow:
            0 10px 30px rgba(0,0,0,0.25);
    }
    
    .stButton > button {
        background: linear-gradient(
            135deg,
            #7c3aed,
            #5b4cf0
        );
    
        color:white;
        border:none;
    }


    </style>
    """, unsafe_allow_html=True)