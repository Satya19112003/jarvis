import streamlit as st
from brain import think
from memory import remember, recall

st.set_page_config(page_title="JARVIS", layout="wide")
st.title("🧠 JARVIS – AI Assistant")

name = recall("name")
if name:
    st.success(f"Welcome back, {name}")

user_input = st.text_input("Enter command")

if st.button("Execute"):
    if "my name is" in user_input:
        remember("name", user_input.replace("my name is", "").strip())
        st.write("Name saved")
    else:
        response = think(user_input)
        st.write(response)
