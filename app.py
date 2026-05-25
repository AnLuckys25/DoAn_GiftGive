import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# --- 1. CẤU HÌNH TRANG CHUẨN GRID ---
st.set_page_config(layout="wide", page_title="GiftGive Dashboard")

# Tinh chỉnh CSS tổng thể: Màu nền, ẩn Header mặc định và căn chỉnh khoảng cách
st.markdown("""
    <style>
    /* 1. Đổi màu nền hồng pastel siêu nhẹ */
    .stApp { background-color: #FFF2F5; }
    
    /* 2. ẨN HOÀN TOÀN THANH HEADER MẶC ĐỊNH CỦA STREAMLIT (Chứa nút Deploy và 3 chấm) */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        background: transparent !important;
        height: 0px !important;
        overflow: hidden !important;
        display: none !important;
    }
    
    /* 3. Đẩy nội dung chính lên sát mép trên sau khi đã giấu thanh header */
    .block-container { 
        padding-top: 2rem !important; 
        padding-bottom: 2rem !important; 
    }
    
    /* 4. CSS định dạng cho các liên kết Tab phẳng */
    .nav-tab {
        text-decoration: none !important;
        font-size: 16px !important;
        font-family: sans-serif !important;
        display: inline-block !important;
        padding-bottom: 6px !important;
        transition: all 0.2s ease;
        text-align: center;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. QUẢN LÝ TRẠNG THÁI KHỞI TẠO TAB (SESSION STATE) ---
# Xử lý lấy thông tin Tab trực tiếp từ Query Parameters của URL để đồng bộ mượt mà
query_params = st.query_params
if "tab" in query_params:
    st.session_state.current_tab = query_params["tab"]
elif 'current_tab' not in st.session_state:
    st.session_state.current_tab = "Trang chủ"

# --- 3. THANH ĐIỀU HƯỚNG TRÊN CÙNG (SỬ DỤNG COLUMNS THUẦN) ---
# Tỷ lệ 1.5 và 2.5 giúp cân bằng tuyệt đối khoảng cách giữa Logo và Menu
col_head_l, col_head_r = st.columns([1.5, 2.5])

with col_head_l:
    # Định dạng Logo canh giữa dòng mượt mà
    st.markdown("<h2 style='margin:0; color:#C71585; font-family: sans-serif; padding-left: 10px; line-height: 40px;'>❤️ GiftGive</h2>", unsafe_allow_html=True)

with col_head_r:
    # Chia nhỏ thành 5 cột tương ứng với 5 phân hệ
    t1, t2, t3, t4, t5 = st.columns(5)
    
    with t1:
        is_active = st.session_state.current_tab == "Trang chủ"
        style = "color: #C71585; font-weight: bold; border-bottom: 3px solid #F492A5;" if is_active else "color: #555555; font-weight: 500; border-bottom: 3px solid transparent;"
        st.markdown(f'<a href="?tab=Trang+chủ" target="_self" class="nav-tab" style="{style}">Trang chủ</a>', unsafe_allow_html=True)
        
    with t2:
        is_active = st.session_state.current_tab == "Kho hàng"
        style = "color: #C71585; font-weight: bold; border-bottom: 3px solid #F492A5;" if is_active else "color: #555555; font-weight: 500; border-bottom: 3px solid transparent;"
        st.markdown(f'<a href="?tab=Kho+hàng" target="_self" class="nav-tab" style="{style}">Kho hàng</a>', unsafe_allow_html=True)
        
    with t3:
        is_active = st.session_state.current_tab == "Người nhận"
        style = "color: #C71585; font-weight: bold; border-bottom: 3px solid #F492A5;" if is_active else "color: #555555; font-weight: 500; border-bottom: 3px solid transparent;"
        st.markdown(f'<a href="?tab=Người+nhận" target="_self" class="nav-tab" style="{style}">Người nhận</a>', unsafe_allow_html=True)
        
    with t4:
        is_active = st.session_state.current_tab == "Lịch sử"
        style = "color: #C71585; font-weight: bold; border-bottom: 3px solid #F492A5;" if is_active else "color: #555555; font-weight: 500; border-bottom: 3px solid transparent;"
        st.markdown(f'<a href="?tab=Lịch+sử" target="_self" class="nav-tab" style="{style}">Lịch sử</a>', unsafe_allow_html=True)
        
    with t5:
        is_active = st.session_state.current_tab == "Báo cáo"
        style = "color: #C71585; font-weight: bold; border-bottom: 3px solid #F492A5;" if is_active else "color: #555555; font-weight: 500; border-bottom: 3px solid transparent;"
        st.markdown(f'<a href="?tab=Báo+cáo" target="_self" class="nav-tab" style="{style}">Báo cáo</a>', unsafe_allow_html=True)

st.write("---")

# --- 4. KIỂM TRA ĐIỀU KIỆN HIỂN THỊ CHỈ KHI Ở TAB "TRANG CHỦ" ---
if st.session_state.current_tab == "Trang chủ":

    # Giới hạn khoảng cách hiển thị nội dung vào trung tâm
    left_space, main_content, right_space = st.columns([0.3, 9.4, 0.3])

    with main_content:
        # Hàng 1: Chia 2 khối lớn (Tình trạng kho & Tổng quan người nhận)
        col1, col2 = st.columns([1, 1])
        
        # --- KHỐI TRÁI: TÌNH TRẠNG KHO HÀNG ---
        with col1:
            st.subheader("Tình trạng Kho hàng")
            st.caption("Biểu đồ động")
            
            sub_col1, sub_col2 = st.columns([1.2, 1])
            with sub_col1:
                fig_bar = go.Figure(go.Bar(
                    y=['Chăn', 'Đồ hộp', 'Nước', 'Gạo'],
                    x=[150, 200, 300, 450],
                    orientation='h',
                    text=['150', '200 units', '300 bottles', '500 kg'],
                    textposition='outside',
                    marker=dict(color='#FBBFCA', line=dict(color='#F492A5', width=1)),
                ))
                fig_bar.update_layout(
                    xaxis=dict(range=[0, 550], showgrid=False, fixedrange=True, visible=False),
                    yaxis=dict(fixedrange=True),
                    margin=dict(l=40, r=40, t=10, b=10), height=180,
                    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
                )
                st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
                
            with sub_col2:
                fig_pie = go.Figure(go.Pie(
                    labels=['Gạo', 'Nước', 'Khác'], values=[450, 300, 350], hole=.6,
                    marker=dict(colors=['#FBBFCA', '#AEC6CF', '#F492A5']), showlegend=False
                ))
                fig_pie.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=180, paper_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_pie, use_container_width=True, config={'displayModeBar': False})
                
            st.button("Quản lý kho", use_container_width=True, key="btn_inventory")

        # --- KHỐI PHẢI: TỔNG QUAN NGƯỜI NHẬN ---
        with col2:
            st.subheader("Tổng quan Người nhận")
            st.write("")
            
            r_col1, r_col2 = st.columns([1, 1.2])
            with r_col1:
                st.info("🏠 **120** \n\n Số hộ đã đăng ký")
                st.success("👤 **98** \n\n Người nhận đã xác minh")
                st.warning("⚠️ **25** \n\n Mức ưu tiên cao")
            with r_col2:
                st.markdown("""
                * 🟢 Xác minh hộ 045
                * 🟢 Yêu cầu mới từ Phường 12
                * 🟢 Đã phát: Hộ 023 (TP.HCM)
                * 🔴 Thiếu: Hộ 078 (Thiếu gạo, Bình Dương)
                * 🟡 Tình huống: Hộ 066 (Chủ hộ vắng mặt)
                * 🔴 Thiếu: Hộ 011 (Thiếu thuốc y tế, Cần Thơ)
                * 🟢 Đã phát: Hộ 102 (Đà Nẵng)
                """)
            st.button("Xem tất cả người nhận", use_container_width=True, key="btn_recipients")

        st.write("---")

        # --- HÀNG 2: LỊCH SỬ QUYÊN GÓP GẦN ĐÂY ---
        st.subheader("Lịch sử Quyên góp gần đây")
        st.caption("Công khai minh bạch")
        
        data = {
            "Ngày": ["18 thg 11, 10:15", "15 thg 11, 13:30", "12 thg 11, 09:00", "10 thg 11, 14:45"],
            "Loại quà tặng": ["Thuốc y tế", "Quần áo", "Sữa em bé", "Gạo"],
            "Số lượng/Mục": ["1 Gói", "5 Kiện", "2 Thùng", "10 Bao"],
            "Trạng thái": ["⏳ Đang chờ nhận", "✅ Đã giao", "❌ Thiếu", "⚠️ Sai địa chỉ"],
            "Hành động": ["[Chi tiết]", "[Chi tiết]", "[Chi tiết]", "[Chi tiết]"],
            "Xác minh": ["🟢 Đã xác minh", "🟢 Đã xác minh", "🟢 Đã xác minh", "🟢 Đã xác minh"]
        }
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True, hide_index=True)

# --- 5. ĐIỀU HƯỚNG SANG CÁC PHÂN HỆ KHÁC KHI CLICK MENU ---
else:
    st.markdown(f"### 🚀 Phân hệ: {st.session_state.current_tab}")
    st.info(f"Bạn đang đứng ở khu vực quản lý dữ liệu của mục '{st.session_state.current_tab}'.")

# --- 6. FOOTER THÔNG TIN HỆ THỐNG ---
st.write("---")
foot1, foot2, foot3 = st.columns(3)
with foot1: st.caption("© Copyright all, GiftGive, Inc.")
with foot2: st.caption("Cách hoạt động | Cập nhật tình hình")
with foot3: st.caption("Hệ thống thông tin quản lý minh bạch")