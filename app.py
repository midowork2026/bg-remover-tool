import streamlit as st
from PIL import Image
import time

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Background Remover",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# CUSTOM CSS (IMPORTANT)
# =========================
st.markdown("""
<style>

body {
    background-color: #f5f7fb;
}

/* Hide Streamlit default menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* HERO */
.hero {
    text-align: center;
    padding: 60px 20px 20px 20px;
}

.hero h1 {
    font-size: 52px;
    font-weight: 800;
    color: #111;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    color: #666;
}

/* UPLOAD BOX */
.upload-box {
    border: 2px dashed #4f46e5;
    border-radius: 18px;
    padding: 40px;
    text-align: center;
    background: white;
    transition: 0.3s;
}

.upload-box:hover {
    transform: scale(1.01);
    border-color: #6366f1;
}

/* BUTTON */
.stButton>button {
    background-color: #4f46e5;
    color: white;
    padding: 12px 20px;
    border-radius: 10px;
    border: none;
    font-size: 16px;
    width: 100%;
}

.stButton>button:hover {
    background-color: #3730a3;
}

/* FEATURE BOX */
.feature {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.05);
}

/* FOOTER */
.footer {
    text-align: center;
    padding: 30px;
    color: gray;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
st.markdown("""
<div class="hero">
    <h1>Remove Background Instantly</h1>
    <p>AI-powered tool to remove image backgrounds in one click — fast, clean, and free.</p>
</div>
""", unsafe_allow_html=True)

# =========================
# UPLOAD SECTION
# =========================
st.markdown("### 📤 Upload Your Image")

uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"])

col1, col2 = st.columns(2)

# =========================
# PROCESS IMAGE (FAKE DEMO OR REAL INTEGRATION PLACE)
# =========================
def remove_background(image):
    # هنا تربط كود الـ AI بتاعك
    time.sleep(2)
    return image  # placeholder

if uploaded_file:
    image = Image.open(uploaded_file)

    with col1:
        st.markdown("### Before")
        st.image(image, use_container_width=True)

    with col2:
        st.markdown("### After (AI Result)")
        
        with st.spinner("Processing..."):
            result = remove_background(image)
            time.sleep(1)

        st.image(result, use_container_width=True)

        st.download_button(
            "⬇️ Download Result",
            data=uploaded_file,
            file_name="result.png",
            mime="image/png"
        )

# =========================
# FEATURES SECTION
# =========================
st.markdown("## ⚡ Why Use Our Tool?")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature">
        <h3>⚡ Fast AI</h3>
        <p>Remove backgrounds in seconds using AI.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature">
        <h3>🎯 High Quality</h3>
        <p>Clean edges and professional results.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature">
        <h3>💸 Free to Use</h3>
        <p>No hidden charges or subscriptions.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
    © 2026 AI Background Remover • Built with Streamlit
</div>
""", unsafe_allow_html=True)
