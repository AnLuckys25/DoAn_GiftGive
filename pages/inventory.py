import streamlit as st



# =====================================
# INVENTORY PAGE / TRANG KHO HÀNG
# =====================================

# Function displays the inventory management page / Hàm hiển thị trang quản lý kho hàng
def show_inventory():
    # Import data locally to avoid circular imports during app initialization / Import dữ liệu tại chỗ để tránh vòng lặp import khi khởi tạo ứng dụng
    from database import get_inventory_data 
    
    data = get_inventory_data()
  
    st.title("📦 Quản lý kho hàng")

    st.caption("Theo dõi vật phẩm hiện có trong kho")

    st.write("")


    # TABLE / BẢNG DỮ LIỆU
    st.dataframe(
        data,
        use_container_width=True
    )

    st.write("")

    # FORM / MẪU THÊM MỚI
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