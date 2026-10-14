import streamlit as st
from services.persistence.exercise_repository import get_or_create_user

def render_login_page():
    if st.session_state.get("user_id") is not None:
        return True

    st.title("AI Real-time GYM Trainer")
    st.caption("### Welcome to the AI Real-time GYM Trainer! Please log in to continue.")

    with st.form("login_form"):
        username = st.text_input("Username (unique identifier)", placeholder="Enter Unique username e.g. Bhalji")
        submit_button = st.form_submit_button("start session")


    if submit_button:
        if username:
            user = get_or_create_user(username)
            st.session_state["username"] = user["username"]
            st.session_state["user_id"] = user["id"]
            st.success(f"Logged in as {username}")
            st.rerun()
            return True
        else:
            st.error("Please enter a valid username.")

        st.rerun()
    return False
