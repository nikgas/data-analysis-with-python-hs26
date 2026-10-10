import streamlit as st
import random
import yfinance as yf
import numpy as np
import pandas as pd

st.title("Niklas's first app")

tab1, tab2, tab3 = st.tabs(["Rock, Paper, Scissors Game", "Currency Converter", "Disney+ Data Explorer"])

with tab1:

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


with tab2:

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import yfinance as yf 

    exchange_rates = yf.download(["EURCHF=X", "CHFEUR=X"], start = "2026-01-01", interval = "1d")

    st.header("Currency converter")

    col1, col2 = st.columns(2)

    with col1:
        amount = st.number_input("Enter amount:", step = 1.00)
    
    with col2:
        selected_currency = st.selectbox("Select currency:", {"EUR", "CHF"})

    if selected_currency == "CHF":
        money_in_EUR = amount * exchange_rates["Close", "CHFEUR=X"].iloc[-1]
        st.write(f"{amount} CHF is {round(money_in_EUR, 2)} EUR on {exchange_rates.index[-1].date()}")
    elif selected_currency == "EUR": 
        money_in_CHF = amount * exchange_rates["Close", "EURCHF=X"].iloc[-1]
        st.write(f"{amount} EUR is {round(money_in_CHF, 2)} CHF on {exchange_rates.index[-1].date()}")

    st.divider()

    st.write("""
    #### Future ideas:
    - st.date_input()
    - st.metric()
    - chart
    """)



with tab3:

    st.header("Disney+ Data Explorer")
    st.markdown("Explore the Disney+ catalogue and filter movies and series by content type.")

    # load dataset
    df_disney = pd.read_csv("week_4/disney_plus_shows.csv")

    # select content types
    selected_types = st.multiselect("Select content type:", options=df_disney["type"].dropna().unique(), default=df_disney["type"].dropna().unique().tolist())

    # filter dataset
    df_filtered = df_disney.loc[df_disney["type"].isin(selected_types)]

    # display results
    st.markdown(f"**Number of titles:** {len(df_filtered)}")
    st.dataframe(df_filtered, use_container_width=True)