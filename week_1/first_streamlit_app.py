import streamlit as st

st.title("Niklas's first app")

with st.chat_message("assistant"):
    st.markdown("Hello, I have a square head. Let's play rock paper scissors.")
with st.chat_message("user"):
    user_choice = st.chat_input("Type your choice, you may use the whole word or only the letters r, p, s.")
allowed_choices = ["rock", "paper", "scissors", "r", "p", "s"]
if user_choice in allowed_choices:
    assistant_choice = choice(["rock", "paper", "scissors"])
    with st.chat_message("assistant"):
        st.markdown(f"You chose: {user_choice}")
else:
    with st.chat_message("assistant"):
        st.markdown("You did not choose a valid option. Please try again.")
