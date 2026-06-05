import streamlit as st
import plotly.express as px

from sample_data import summary_data


# =====================================
# DASHBOARD / BẢNG ĐIỀU KHIỂN
# =====================================

# Function displays the main dashboard page / Hàm hiển thị trang tổng quan chính
def show_dashboard():

    st.title("📊 Dashboard Tổng quan")

    st.caption("Theo dõi tình trạng quyên góp thời gian thực")

    st.write("")

    # =====================================
    # METRIC / CHỈ SỐ
    # =====================================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Tổng hộ",
        summary_data["tong_ho"]
    )

    col2.metric(
        "Đã xác minh",
        summary_data["da_xac_minh"]
    )

    col3.metric(
        "Ưu tiên cao",
        summary_data["uu_tien"]
    )

    col4.metric(
        "Tổng vật phẩm",
        summary_data["tong_quyen_gop"]
    )

    st.write("")

    # =====================================
    # CHART / BIỂU ĐỒ
    # =====================================

    left, right = st.columns([1.2, 1])

    with left:

        chart_data = {
            "Vật phẩm": [
                "Gạo",
                "Nước",
                "Đồ hộp",
                "Chăn"
            ],

            "Số lượng": [
                450,
                300,
                200,
                150
            ]
        }

        fig = px.bar(
            chart_data,
            x="Số lượng",
            y="Vật phẩm",
            orientation="h",
            title="📦 Tình trạng kho"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        pie_data = {
            "Loại": [
                "Gạo",
                "Khác",
                "Nước"
            ],

            "Số lượng": [
                450,
                350,
                300
            ]
        }

        fig2 = px.pie(
            pie_data,
            values="Số lượng",
            names="Loại",
            hole=0.55
        )

        fig2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.write("")

    # =====================================
    # RECENT ACTIVITY / HOẠT ĐỘNG GẦN ĐÂY
    # =====================================

    st.subheader("📌 Hoạt động gần đây")

    st.markdown("""
    ✅ Đã giao quà cho hộ H001 tại TP.HCM

    ⚠️ Kho thuốc đang thiếu số lượng

    🟢 3 hộ mới được xác minh

    📦 Tiếp nhận thêm 200kg gạo
    """)