import os
import openai
import time
import requests
import re
import tiktoken
import streamlit as st

open_ai_key = st.secrets['open_ai_key']

prompt = f"""

we have a paragraph about this title: "مسابقات لیگ برتر انگلیس". please write an persian article introduction with the help of title

the introduction must mention that what is the purpose of article and the introduction should be in 400 words.
"""
def get_prompt(title):
    p = f"""

    we have a paragraph about this title: {title}. please write an persian article introduction with the help of title

    the introduction must mention that what is the purpose of article and the introduction should be in 400 words.
    """
    return p
def chat_gen(prompt, tmp = 0.7, model_name="gpt-3.5-turbo"):


    messages = [{"role": "user", "content": prompt}]
    res = openai.ChatCompletion.create(
    model=model_name,
    messages=messages,
    temperature=tmp,

    )
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    return res.choices[0].message["content"]
