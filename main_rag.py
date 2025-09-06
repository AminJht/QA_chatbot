from hazm_normalizer import NormalizerFarsi
from search_in_cromadb import search_db
from llm_api import ApiLlm
normalizer = NormalizerFarsi()
def main(question:str):
    norm_q = normalizer.h_normalizer(question)
    # در cromadb سرج میکند و 5 متن میگیرد و از ان 5 متن اگر فاصله کمتراز 0.4 باشد برمیگرداند
    search = search_db()
    dict_of_results= search.search(norm_q)
    print(dict_of_results)
    if not dict_of_results:
        return "جوابی برای سوالتان ندارم"
    result_text=""
    for doc_id, doc_info in dict_of_results.items():
        # اضافه کردن document text به صورت خط جداگانه
        result_text += doc_info['document'] + "\n\n"

    final_prompt=f"""
    بر اساس متن زیر به سوال پاسخ دهید:

    متن:
    {result_text}

    سوال: 
    {question}

    دستورالعمل:
    - فقط از اطلاعات داخل متن استفاده کنید
    - اگر جواب را نمی دانید بگویید "اطلاعات کافی ندارم"
    - پاسخ واضح و مختصر باشد
    - به زبان فارسی پاسخ دهید

    پاسخ:
    """
    llm = ApiLlm()
    answer = llm.generate_answer(prompt=final_prompt)
    return(answer)