import random
import streamlit as st

# Initialize session state variables
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "message" not in st.session_state:
    st.session_state.message = "I'm thinking of a number between 1 and 100."

st.title("🎯 Number Guessing Game")

st.write("Try to guess the number I'm thinking of!")

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Guess button
if st.button("Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.session_state.message = "🔽 Too low! Try again."
    elif guess > st.session_state.secret_number:
        st.session_state.message = "🔼 Too high! Try again."
    else:
        st.session_state.message = f"🎉 Congratulations! You guessed the number {st.session_state.secret_number} in {st.session_state.attempts} attempts."
        # Reset game after winning
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0

# Show message
st.write(st.session_state.message)

# Reset button
if st.button("Restart Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.message = "Game restarted! I'm thinking of a new number."
    st.experimental_rerun()
