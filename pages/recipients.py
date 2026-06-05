import streamlit as st
from database import get_recipient_data


# =====================================
# RECIPIENT PAGE / TRANG NGƯỜI NHẬN
# =====================================

# Function displays the recipient list page / Hàm hiển thị trang danh sách người nhận
def show_recipients():

    st.title("🤝 Người nhận hỗ trợ")

    st.caption("Danh sách hộ gia đình và người nhận")

    st.write("")

    # LOAD DATA / TẢI DỮ LIỆU
    df = get_recipient_data()

    # TABLE / BẢNG DỮ LIỆU
    st.dataframe(
        df,
        use_container_width=True
    )

    st.write("")

    # FORM / MẪU THÊM NGƯỜI NHẬN
    with st.expander("➕ Thêm người nhận"):

        name = st.text_input("Tên người nhận")

        area = st.text_input("Khu vực")

        status = st.selectbox(
            "Trạng thái",
            [
                "Đã xác minh",
                "Ưu tiên cao",
                "Chờ hỗ trợ"
            ]
        )

        if st.button("Lưu người nhận"):

            st.success(
                f"Đã thêm người nhận: {name}"
            )