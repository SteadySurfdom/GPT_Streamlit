import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
openai.api_key = "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"
output = {
        "choices": [
            {
                "message": {
                    "content": "Hi, How can I help you today?"
                }
            }
        ]
    }
with st.sidebar:
    with st.form(key = 'querySubmission'):
        context = st.text_area(
            "CONTEXT",
            placeholder="Enter the context paragraph",
            key="1",
        )
        query = st.text_area(
            "QUERY",
            placeholder="Enter the query",
            key="2",
        )

        submit = st.form_submit_button()
        
        if context and query:
            output = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                temperature=0.6,
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": query},
                ],
            )
    
st.markdown(f'{output["choices"][0]["message"]["content"]}</div>', unsafe_allow_html=True)
