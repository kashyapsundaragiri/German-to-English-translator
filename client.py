import requests
import streamlit as st


def get_groq_response(input_text):
    json_body={
        "input": {
            "language": "German",
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }

    response=requests.post("http://127.0.0.1:8000/chain/invoke",json=json_body)

    print(response.json())
    return response.json()["output"]

## Streamlit app
st.title("LLM Application Using LCEL")
input_text =st.text_input("Enter the text you want to convert to German")

if input_text:
    translated_text = get_groq_response(input_text)

    st.subheader("Translation")
    st.success(translated_text)
