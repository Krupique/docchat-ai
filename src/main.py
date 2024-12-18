
import sys
from langchain_community.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAIEmbeddings, OpenAI

from data.document_loader import read_pdf
from prompts.prompt_builder import get_answer

import warnings
import json

import os

warnings.filterwarnings('ignore')

def main():
    config_path = 'config/secret_key.json'
    with open(config_path, "r") as f:
        config = json.load(f)

    # Gets the custom prompt as a parameter
    if len(sys.argv) < 2:
        print("Uso: python main.py '<seu_prompt>'")
        return
    custom_prompt = sys.argv[1]

    # Executing the function
    doc = read_pdf('src/files/')

    # Creating the embedding generator
    embedding_generator = OpenAIEmbeddings(api_key = config['secret_key'])

    # Creating the vector store
    index = Chroma.from_documents(doc, embedding_generator, collection_name='docchat-index')

    # Create LLM instance
    llm = OpenAI(openai_api_key = config['secret_key'], temperature = 0.3)

    # Creates the chain for questions and answers in documents
    chain = load_qa_chain(llm, chain_type = 'stuff')

    response = get_answer(index, chain, custom_prompt)
    print(response['output_text'])


if __name__ == "__main__": 
    main()