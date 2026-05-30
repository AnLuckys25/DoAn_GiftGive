import streamlit as st
from database import get_history_data


# =========================
# HISTORY
# =========================

def show_history():

    st.title("🕘 Lịch sử quyên góp")

    df = get_history_data()

    st.dataframe(df, use_container_width=True)