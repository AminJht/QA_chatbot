📋 پیش‌نیازهای اجرای پروژه
ساختار پوشه‌ها
تمام فایل‌های پروژه را در یک مسیر واحد قرار دهید.

ایجاد محیط مجازی
دستور زیر را در ترمینال اجرا کنید:

bash
python -m venv venv
فعال‌سازی محیط مجازی

ویندوز:

bash
.\venv\Scripts\activate
لینوکس/مک:

bash
source venv/bin/activate
نصب کتابخانه‌ها

bash
pip install -r requirements.txt
اجرای پروژه

bash
streamlit run UI.py
⚠️ ملاحظات مهم
اتصال به اینترنت ضروری است (برای دسترسی به API GPT-4o-mini)

پروژه در localhost بر روی پورت 8501 اجرا می‌شود

محیط مجازی باید فعال باشد قبل از اجرای دستور نهایی

