
import sys
from langchain_community.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAIEmbeddings, OpenAI

from src.data.document_loader import read_pdf
from src.prompts.prompt_builder import get_answer

import warnings
import json

import os

warnings.filterwarnings('ignore')

def lambda_handler(event, context):
    config_path = 'config/secret_key.json'
    with open(config_path, "r") as f:
        config = json.load(f)

    if not config:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Secret key not found."})
        }

    custom_prompt = event.get("custom_prompt")
    if not custom_prompt:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "The 'custom_prompt' field is required."})
        }


    try:
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
        
        return {
            "statusCode": 200,
            "body": json.dumps({"response": response['output_text']})
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

