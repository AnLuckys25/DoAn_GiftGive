import streamlit as st



# =====================================
# INVENTORY PAGE
# =====================================

def show_inventory():
    # Mang dòng import bỏ vào ĐÂY, thay vì để ở đầu file
    from database import get_inventory_data 
    
    data = get_inventory_data()
  
    st.title("📦 Quản lý kho hàng")

    st.caption("Theo dõi vật phẩm hiện có trong kho")

    st.write("")


    # TABLE
    st.dataframe(
        data,
        use_container_width=True
    )

    st.write("")

    # FORM
    with st.expander("➕ Thêm vật phẩm mới"):

        item_name = st.text_input("Tên vật phẩm")

        quantity = st.number_input(
            "Số lượng",
            min_value=0
        )

        status = st.selectbox(
            "Trạng thái",
            ["Đủ", "Thiếu", "Sắp hết"]
        )

        if st.button("Lưu vật phẩm"):

            st.success(
                f"Đã thêm '{item_name}' vào kho"
            )