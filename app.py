import streamlit as st
import time
import chat


prompt = st.chat_input("لطفا عنوان مقاله را وارد کنید")
if prompt:
    with st.spinner('Wait for it...'):
        time.sleep(40)

    with st.chat_message("user"):
        prompt = chat.get_prompt(prompt)
        st.write(chat.chat_gen(prompt, model_name="gpt-3.5-turbo"))