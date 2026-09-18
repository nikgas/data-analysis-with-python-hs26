import streamlit as st
import random

st.title("Niklas's first app")

allowed_choices = ["r", "p", "s", "rock", "paper", "scissors"]

if "assistant_score" not in st.session_state:
    st.session_state.assistant_score = 0
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

with st.chat_message("assistant"):
    st.markdown("Hello, I have a square head. Let's play rock paper scissors.")
with st.chat_message("user"):
    user_choice = st.chat_input("Type your choice, you may use the whole word or only the letters r, p, s.")

if user_choice in allowed_choices:
    allowed_assistant_choices = ["r", "p", "s"]
    assistant_choice = random.choice(allowed_assistant_choices)
    user_choice = user_choice[0].lower()
    # draw
    if assistant_choice == user_choice:   
        with st.chat_message("assistant"):
            st.markdown(f"It's a draw, I chose {assistant_choice} too. Make a new choice to play again." \
                        f" The score is {st.session_state.assistant_score}:{st.session_state.user_score} (assistant:user).")
    # assistant wins
    elif (assistant_choice == "r" and user_choice == "s") or (assistant_choice == "p" and user_choice == "r") or (assistant_choice == "s" and user_choice == "p"):
        st.session_state.assistant_score += 1
        with st.chat_message("assistant"):
            st.markdown(f"I win! {assistant_choice} beats {user_choice}. Make a new choice to play again." \
                        f" The score is {st.session_state.assistant_score}:{st.session_state.user_score} (assistant:user).")
    # user wins
    elif (assistant_choice == "r" and user_choice == "p") or (assistant_choice == "p" and user_choice == "s") or (assistant_choice == "s" and user_choice == "r"):
        st.session_state.user_score += 1
        with st.chat_message("assistant"):
            st.markdown(f"You win! {user_choice} beats {assistant_choice}. Make a new choice to play again." \
                        f" The score is {st.session_state.assistant_score}:{st.session_state.user_score} (assistant:user).")
else:
    with st.chat_message("assistant"):
        st.markdown("You did not choose a valid option. Please try again." \
        f" The score is {st.session_state.assistant_score}:{st.session_state.user_score} (assistant:user).")