
import streamlit as st
import random

st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

# Custom design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
.stButton > button {
    width: 100%;
    height: 75px;
    font-size: 22px;
    border-radius: 15px;
    background-color: #00c9a7;
    color: black;
    font-weight: bold;
    border: none;
}
.stButton > button:hover {
    background-color: #00f5c4;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# Game settings
if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "result" not in st.session_state:
    st.session_state.result = "Choose your move to start!"

if "player" not in st.session_state:
    st.session_state.player = "❔"

if "computer" not in st.session_state:
    st.session_state.computer = "❔"

st.title("🎮 ROCK PAPER SCISSORS")
st.markdown("### Challenge the Computer!")
st.write("Choose your move and see who wins!")

st.divider()

# Scoreboard
col1, col2 = st.columns(2)

with col1:
    st.metric("👤 Your Score", st.session_state.player_score)

with col2:
    st.metric("🤖 Computer Score", st.session_state.computer_score)

st.divider()

st.subheader("Choose Your Move")

# Game choices
choices = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}

def play_game(player_choice):
    computer_choice = random.choice(list(choices.keys()))

    st.session_state.player = choices[player_choice]
    st.session_state.computer = choices[computer_choice]

    if player_choice == computer_choice:
        st.session_state.result = "🤝 IT'S A DRAW!"

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.session_state.result = "🎉 YOU WIN!"
        st.session_state.player_score += 1

    else:
        st.session_state.result = "😢 COMPUTER WINS!"
        st.session_state.computer_score += 1

# Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✊ Rock"):
        play_game("Rock")

with col2:
    if st.button("✋ Paper"):
        play_game("Paper")

with col3:
    if st.button("✌️ Scissors"):
        play_game("Scissors")

st.divider()

# Result display
st.subheader("Game Result")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👤 You")
    st.markdown(f"# {st.session_state.player}")

with col2:
    st.markdown("### 🤖 Computer")
    st.markdown(f"# {st.session_state.computer}")

st.markdown(
    f"<h2 style='text-align:center; color:#00f5c4;'>{st.session_state.result}</h2>",
    unsafe_allow_html=True
)

st.divider()

# Reset button
if st.button("🔄 RESET GAME"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.result = "Choose your move to start!"
    st.session_state.player = "❔"
    st.session_state.computer = "❔"
    st.rerun()

st.markdown(
    "<p style='text-align:center;'>Made by Ishrat ❤️</p>",
    unsafe_allow_html=True
)
