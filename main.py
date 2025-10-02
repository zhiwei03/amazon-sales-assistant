import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Amazon Sales: Database Q&A 💰")

question = st.text_input("Question: ")
show_sql = st.checkbox("Show SQL query") 

if question:
    with st.spinner("⏳ Finding answer..."):
        chain = get_few_shot_db_chain()

        # Get structured output including intermediate steps
        response = chain({"query": question})

        # Final answer
        st.header("Answer")
        st.write(response["result"])

    # Extract SQL query if checkbox is selected
    if show_sql: 
        sql_query = None
        for step in response['intermediate_steps']:
            if isinstance(step, dict) and 'sql_cmd' in step:
                sql_query = step['sql_cmd']
                break

        if sql_query:
            st.header("SQL Query")
            st.code(sql_query)
        else:
            st.write("No SQL query found")