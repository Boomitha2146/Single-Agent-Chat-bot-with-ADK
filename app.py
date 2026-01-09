import streamlit as st
import agent

st.title("Single Agent Chatbot with ADK")

user_input = st.text_input("Ask something")

if user_input:
    response = agent.run(user_input)
    st.write(response)

