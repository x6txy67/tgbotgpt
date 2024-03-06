import os
from dotenv import load_dotenv
# from PyPDF2 import PdfReader

import google.generativeai as genai


def main():
    load_dotenv()
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    pdf = "data/output1.pdf"

    if pdf is not None:
        # pdf_reader = PdfReader(pdf)
        # text = ""
        # for page in pdf_reader.pages:
        #     text += page.extract_text()
        
        model = genai.GenerativeModel('gemini-pro')

        user_question = "Вы профессиональный финансист и экономист.Не говорите, что вы профессиональный финансист и экономист. Мне нужны 3 перспективные сектора для инвестиций. Сохраняйте профессионализм и читабельно напишите текст, в какие сферы лучше инвестировать. Кратко опишите каждую сферу. Не говорите, что вы профессиональный экономист и финансист."
        
        response = model.generate_content(user_question)

        if user_question:
            return response.text



if __name__ == "__main__":
    main()
