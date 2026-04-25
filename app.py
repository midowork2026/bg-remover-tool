import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="إزالة خلفية الصور مجاناً", layout="centered")

st.title("✂️ أداة إزالة خلفية الصور")
st.write("ارفع صورتك الآن واحصل عليها بخلفية شفافة في ثوانٍ!")

uploaded_file = st.file_uploader("اختر صورة...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='الصورة الأصلية', use_column_width=True)
    
    with st.spinner(' جاري إزالة الخلفية...'):
        # معالجة الصورة
        result = remove(image.convert("RGBA"))
        
        # تحويل الصورة لبيانات قابلة للتحميل
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        byte_im = buf.getvalue()

    st.image(result, caption='الصورة بدون خلفية', use_column_width=True)
    
    st.download_button(
        label="تحميل الصورة الشفافة (PNG)",
        data=byte_im,
        file_name="no-bg.png",
        mime="image/png"
    )
