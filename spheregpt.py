from dotenv import load_dotenv
from langchain.callbacks import get_openai_callback
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai import OpenAI, OpenAIEmbeddings
from libretranslatepy import LibreTranslateAPI
from openai import BadRequestError
from PyPDF2 import PdfReader

lt = LibreTranslateAPI("https://translate.terraprint.co/")


def main():
    load_dotenv()

    pdf = "data/output1.pdf"

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = CharacterTextSplitter(
            separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
        )
        chunks = text_splitter.split_text(text)

        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        user_question = "You are a professional financier and economist.Do not say you are a professional financier and economist. I need 3 promising areas for investment. Keep professionalism and readably write a text in which spheres it is better to invest in. Briefly describe each area. Don't say you are a professional economist and financier"
        if user_question:
            docs = knowledge_base.similarity_search(user_question)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")

            try:
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=user_question)
                    return lt.translate(response, "en", "ru")

            except BadRequestError as e:
                print(f"OpenAI API Error: {e}")
                print(
                    "There was an error processing your request. Please try again later or contact support."
                )


if __name__ == "__main__":
    main()
