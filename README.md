# Amazon Sales Assistant
<img width="1920" height="869" alt="Screenshot (9)" src="https://github.com/user-attachments/assets/927a5ac3-debf-4d61-86ed-dc7b3a60f902" />

## Table of contents
* [General info](#general-info)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Setup](#setup)
* [Limitations](#limitations)
* [Inspiration](#inspiration)

## General info
This project is a simple streamlit web application that uses LangChain, Gemini 2.5 Pro , and Amazon sales data to answer natural language questions about Amazon sales data.
It automatically generates SQL queries, executes them on MySQL, and returns human-readable answers.

## Features
- Ask natural language questions about Amazon sales data
- Automatically generates SQL queries with LangChain
- Executes queries on MySQL database
- Returns easy-to-read answers
- Option to view the generated SQL query

## Tech Stack
- LangChain: framework for connecting the LLM with the database
- Gemini 2.5 Pro: Large Language Model
- Hugging Face Embeddings (sentence-transformers/all-MiniLM-L6-v2) + Chroma: for semantic search
- Streamlit: Web application framework
- MySQL: Database for Amazon sales data

## Setup
1. Clone the repository
```
git clone https://github.com/zhiwei03/amazon-sales-assistant.git
cd amazon-sales-assistant
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Set up .env file 
```
google_api_key= 'YOUR_GOOGLE_API_KEY'
db_user = 'YOUR_MYSQL_USERNAME'
db_password = 'YOUR_MYSQL_PASSWORD'
db_host = 'YOUR_MYSQL_HOST'
db_name = 'YOUR_DATABASE_NAME'
```
4. Run the app:
```
streamlit run main.py
```

## Limitations
- ⚠️ The free tier of Gemini 2.5 Pro only allows **50 requests per day**
-  Exceeding this quota may result in errors until the daily quota resets
  
## Inspiration
- This project is inspired by [codebasics YouTube](https://www.youtube.com/watch?v=4wtrl4hnPT8&t=1527s)
- The Amazon Sales 2025 dataset used in this project is obtained from [Kaggle](https://www.kaggle.com/datasets/zahidmughal2343/amazon-sales-2025)
