import streamlit as st
from pathlib import Path

from pages.dashboard import show_dashboard
from pages.inventory import show_inventory
from pages.recipients import show_recipients
from pages.history import show_history
from pages.reports import show_reports


# =====================================
# PAGE CONFIG / CấU HìNH TRANG
# =====================================

st.set_page_config(
    page_title="GiftGive",
    page_icon="🎁",
    layout="wide"
)

# =====================================
# SESSION / PHIêN LàM VIệC
# =====================================

if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "page" not in st.session_state:
    st.session_state.page = "dashboard"


# =====================================
# LOAD CSS / CSS
# =====================================

# Function to load CSS into the page / Hàm tải tệp CSS và chèn nội dung vào trang
def load_css(file):
    css_path = Path(__file__).parent / file
    with open(css_path, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================
# ROUTING / điều hướng trang
# =====================================

valid_pages = {
    "dashboard": show_dashboard,
    "inventory": show_inventory,
    "recipients": show_recipients,
    "history": show_history,
    "reports": show_reports,
}

query_params = st.query_params

requested_page = query_params.get("page", None)
requested_theme = query_params.get("theme", None)

if requested_page in valid_pages:
    st.session_state.page = requested_page
else:
    st.session_state["page"] = st.session_state.page

if requested_theme == "light":
    st.session_state.theme = "light"
elif requested_theme == "dark":
    st.session_state.theme = "dark"
else:
    st.session_state["theme"] = st.session_state.theme

#Tải CSS tương ứng với theme
if st.session_state.theme == "dark":
    load_css("assets/Dark.css")
else:
    load_css("assets/Light.css")

page = st.session_state.page

# Load Material Icons for sidebar icons
st.markdown(
    "<link href='https://fonts.googleapis.com/icon?family=Material+Icons' rel='stylesheet'>",
    unsafe_allow_html=True,
)

# =====================================
# SIDE NAV BAR / THANH điều hướng 
# =====================================

nav_items = [
    ("dashboard", "dashboard", "Dashboard"),
    ("history", "history", "Lịch sử"),
    ("inventory", "inventory_2", "Kho hàng"),
    ("recipients", "group", "Người nhận"),
    ("reports", "bar_chart", "Báo cáo"),
]

left_col, main_col = st.columns([0.18, 0.82], gap="small")

with left_col:
    theme_target = "dark" if st.session_state.theme == "light" else "light"
    theme_icon = "dark_mode" if st.session_state.theme == "light" else "light_mode"
    theme_label = "Dark mode" if st.session_state.theme == "light" else "Light mode"

    sidebar_html = ""
    sidebar_html += "<div class='side-panel'>"
    sidebar_html += "<div class='side-brand'>"
    sidebar_html += "<div class='brand-title'>GiftGiven</div>"
    sidebar_html += "<div class='brand-caption'>Quản lý quyên góp</div>"
    sidebar_html += "</div>"
    sidebar_html += "<div class='sidebar-links'>"

    for item_key, icon_name, label in nav_items:
        active_class = "active" if page == item_key else ""
        sidebar_html += (
        "<a class='sidebar-link " + active_class + "' href='?page=" + item_key + "&theme=" + st.session_state.theme + "'target='self'>"
        "<span class='material-icons sidebar-icon'>" + icon_name + "</span>"
        "<span class='sidebar-text'>" + label + "</span>"
        "</a>"
    )

    sidebar_html += "</div>"
    sidebar_html += (
        "<a class='theme-pill' href='?page=" + page + "&theme=" + theme_target + "'target='_self'>"
        "<span class='material-icons theme-icon'>" + theme_icon + "</span>"
        "<span>" + theme_label + "</span>"
        "</a>"
    )
    sidebar_html += "</div>"

    st.markdown(sidebar_html, unsafe_allow_html=True)

with main_col:
    valid_pages[page]()
