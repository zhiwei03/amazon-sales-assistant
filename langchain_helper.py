from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate

from few_shots import few_shots

import os
from dotenv import load_dotenv
load_dotenv() # take environment variables from .env (especially openai api key)

def get_few_shot_db_chain():
    # Step 1: Connect with the database
    db_user = os.environ['db_user']
    db_password = os.environ['db_password']
    db_host = os.environ['db_host']
    db_name = os.environ['db_name']

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                              sample_rows_in_table_info=3)

    # Step 2: Initialize the LLM
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    google_api_key=os.environ['google_api_key'],
    temperature=0.2
    )

    # Step 3: Create the SQL Database Chain
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    # join all values in few shot into single string, separated by space 
    # does this for every dictionary (example) in the list (few_shots)
    to_vectorize = [" ".join(example.values()) for example in few_shots] 

    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots)

    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
    )

    example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector, # retrieves the top-k most similar from  vectorstore (Chroma)
    example_prompt=example_prompt, # Defines how each example is formatted (like Q: {question}\nA: {answer}).
    prefix=_mysql_prompt, # instructions before the examples
    suffix=PROMPT_SUFFIX, # instructions after the examples
    input_variables=["input", "table_info", "top_k"], # These variables are used in the prefix and suffix
    )

    # Build SQL generator
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt, return_intermediate_steps=True)
    return chain