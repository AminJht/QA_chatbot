from g4f.client import Client
class ApiLlm:
    def __init__(self):  
        self.client = Client()
        self.model = "gpt-4o-mini"

    def generate_answer(self, prompt:str):
        print("start generate")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            web_search=False
        )
        print("finnish generate")
        
        return response.choices[0].message.content

if __name__ == "__main__":
    # این قسمت فقط زمانی اجرا می شود که مستقیماً این فایل را run کنید.
    llm = ApiLlm()
    prompt = "سلام خرس ها میخندن؟"
    answer = llm.generate_answer(prompt=prompt)
    print(answer)
