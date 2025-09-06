import streamlit as st
import time
from main_rag import main

# تنظیمات صفحه با پشتیبانی RTL
st.set_page_config(
    page_title="چت‌بات چندزبانه",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# اضافه کردن CSS برای راست‌چین کردن کامل صفحه
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    
    * {
        font-family: 'Vazirmatn', sans-serif;
        text-align: right;
        direction: rtl;
    }
    
    .stTextInput > div > div > input {
        text-align: right;
        direction: rtl;
        font-family: 'Vazirmatn', sans-serif;
    }
    
    .stChatInput {
        direction: rtl;
    }
    
    .stChatMessage {
        direction: rtl;
        text-align: right;
    }
    
    .stButton button {
        font-family: 'Vazirmatn', sans-serif;
        width: 100%;
    }
    
    h1, h2, h3, h4, h5, h6 {
        text-align: right;
        direction: rtl;
    }
    
    .css-1d391kg, .css-1y4p8pa {
        text-align: right;
        direction: rtl;
    }
</style>
""", unsafe_allow_html=True)

# عنوان برنامه
st.title("🤖 چت‌بات راهنما")
st.write("سوال خود را بپرسید")

# ذخیره‌سازی تاریخچه چت در session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# نمایش تاریخچه چت
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# دریافت ورودی کاربر
prompt = st.chat_input("...سوال خود را اینجا بنویسید")
response = main(prompt)
if prompt:
    # نمایش سوال کاربر
    with st.chat_message("user"):
        st.write(prompt)
    
    # ذخیره سوال در تاریخچه
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # شبیه‌سازی پردازش (در نسخه واقعی به API مدل زبانی متصل می‌شود)
    with st.chat_message("assistant"):
        with st.spinner("...در حال پردازش"):
            time.sleep(1)  # شبیه‌سازی تاخیر پردازش

            st.write(response)
    
    # ذخیره پاسخ در تاریخچه
    st.session_state.messages.append({"role": "assistant", "content": response})