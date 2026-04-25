import streamlit as st
from rembg import remove
from PIL import Image
import io

# إعدادات الصفحة
st.set_page_config(page_title="ميدو - إزالة الخلفية", page_icon="✂️", layout="wide")

# تصميم الواجهة باستخدام CSS
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        color: #2d3436;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 20px;
        color: #636e72;
        text-align: center;
        margin-bottom: 40px;
    }
    .upload-box {
        border: 2px dashed #00b894;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# الهيدر (العنوان)
st.markdown('<p class="title">إزالة خلفية الصورة</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">مجاني بنسبة 100% وتلقائي</p>', unsafe_allow_html=True)

# تقسيم الصفحة لعمودين عشان الشكل يبقى زي المواقع الاحترافية
col1, col2 = st.columns([1, 1])

with col1:
    st.info("💡 نصيحة: ارفع صور واضحة للحصول على أفضل نتيجة")
    uploaded_file = st.file_uploader("قم بتحميل صورة هنا...", type=["jpg", "jpeg", "png"])

with col2:
    # هنا ممكن تحط صورة توضيحية "قبل وبعد" عشان اللي يدخل يفهم الموقع بيعمل إيه
    st.write("### كيف يعمل؟")
    st.write("1. ارفع صورتك من الجهاز.")
    st.write("2. انتظر ثواني ليقوم الذكاء الاصطناعي بعمله.")
    st.write("3. حمل صورتك بخلفية شفافة!")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    with st.spinner('جاري المعالجة... انتظر قليلاً'):
        # إزالة الخلفية
        result = remove(image)
        
        # عرض النتيجة
        st.success("تمت الإزالة بنجاح!")
        st.image(result, caption='صورتك الجديدة', use_column_width=True)
        
        # زر التحميل
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="تحميل الصورة بدون خلفية",
            data=byte_im,
            file_name="mido_no_bg.png",
            mime="image/png"
        )

# فوتر (Footer) بسيط في الآخر
st.markdown("---")
st.markdown("<p style='text-align: center;'>صُنع بكل حب بواسطة ميدو © 2026</p>", unsafe_allow_html=True)
