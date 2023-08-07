import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
openai.api_key = st.secrets['API_KEY']  # capped at 5$ (No need to add it to st.secrets)
output = {"choices": [{"message": {"content": "Hi, How can I help you today?"}}]}
context = "Answer respectfully. You are an obedient chatbot."
with st.sidebar:
    with st.form(key="querySubmission"):
        context_entered = st.text_area(
            "CONTEXT",
            placeholder="Enter the context paragraph",
            key="1",
        )
        context = context_entered if context_entered else context
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
            # output = {
            #     "choices": [
            #         {
            #             "message": {
            #                 "content": f"API ran with context:{context} and query:{query}"
            #             }
            #         }
            #     ]
            # }
        if not query:
            st.markdown(f"Query not entered</div>", unsafe_allow_html=True)
st.markdown(
    f'<div>{output["choices"][0]["message"]["content"]}</div>', unsafe_allow_html=True
)
