from dotenv import load_dotenv
from langchain.callbacks import get_openai_callback
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from openai import BadRequestError
from PyPDF2 import PdfReader


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

        user_question = "As a professional economist and financier, you possess a unique ability to accurately predict stock movements. Your task is to present stock recommendations in an enticing manner, sparking the reader's interest to consider these investments. Maintain a professional tone throughout and offer sound investment advice. The chosen stocks align with your research criteria, based on a confidential Levermann strategy. However, it's important to note that the bot should not disclose Levermann scores or specific details about the strategy. Provide only the company names and their ticker labels, crafting each recommendation with a pleasantly readable style that captivates potential investors. Please share 3 such recommendations."
        if user_question:
            docs = knowledge_base.similarity_search(user_question)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")

            try:
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=user_question)
            
                    return response

            except BadRequestError as e:
                print(f"OpenAI API Error: {e}")
                print(
                    "There was an error processing your request. Please try again later or contact support."
                )


if __name__ == "__main__":
    main()
