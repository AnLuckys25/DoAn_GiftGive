import streamlit as st

from pages.dashboard import show_dashboard
from pages.inventory import show_inventory
from pages.recipients import show_recipients
from pages.history import show_history
from pages.reports import show_reports


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="GiftGive",
    page_icon="🎁",
    layout="wide"
)

# =====================================
# SESSION
# =====================================

if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"



# =====================================
# LOAD CSS
# =====================================

def load_css(file):
    with open(file, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


if st.session_state.theme == "dark":
    load_css("assets/Dark.css")
else:
    load_css("assets/Light.css")


# =====================================
# TOP NAV BAR (horizontal)
# =====================================

# App title
st.markdown("# 🎁 GiftGive")
st.caption("Hệ thống quản lý quyên góp")

# Horizontal navigation using columns — compact spacing
nav_items = [
    ("Dashboard", "📊 Dashboard"),
    ("Kho hàng", "📦 Kho hàng"),
    ("Người nhận", "🤝 Người nhận"),
    ("Lịch sử", "🕘 Lịch sử"),
    ("Báo cáo", "📈 Báo cáo"),
]

# Create one column per nav item plus one for the theme toggle
cols = st.columns(len(nav_items) + 1, gap="small")

for i, (page_key, label) in enumerate(nav_items):
    with cols[i]:
        if st.button(label, key=f"nav_{page_key}"):
            st.session_state.page = page_key
        # Underline indicator for active page
        if st.session_state.page == page_key:
            st.markdown("<div class='nav-underline'></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

# Theme toggle in the last column
theme_col = cols[-1]

with theme_col:

    icon = (
        "☀️"
        if st.session_state.theme == "dark"
        else "🌙"
    )

    if st.button(
        icon,
        key="theme_toggle",
        use_container_width=True
    ):

        if st.session_state.theme == "dark":
            st.session_state.theme = "light"
        else:
            st.session_state.theme = "dark"

        st.rerun()

# =====================================
# ROUTING
# =====================================

page = st.session_state.page

if page == "Dashboard":
    show_dashboard()

elif page == "Kho hàng":
    show_inventory()

elif page == "Người nhận":
    show_recipients()

elif page == "Lịch sử":
    show_history()

elif page == "Báo cáo":
    show_reports()