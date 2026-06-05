import streamlit as st
from database import get_history_data


# =========================
# HISTORY / LỊCH SỬ
# =========================

# Function displays the donation history page / Hàm hiển thị trang lịch sử quyên góp
def show_history():

    st.title("🕘 Lịch sử quyên góp")

    df = get_history_data()

    st.dataframe(df, use_container_width=True)