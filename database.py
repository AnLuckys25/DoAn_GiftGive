import pandas as pd


# =====================================
# INVENTORY / KHO HÀNG
# =====================================

# Function returns sample inventory data / Hàm trả về dữ liệu kho hàng mẫu
def get_inventory_data():

    return pd.DataFrame({

        "Tên vật phẩm": [
            "Gạo",
            "Nước",
            "Thuốc",
            "Quần áo"
        ],

        "Số lượng": [
            450,
            300,
            120,
            200
        ],

        "Trạng thái": [
            "Đủ",
            "Đủ",
            "Thiếu",
            "Đủ"
        ]
    })


# =====================================
# RECIPIENTS / NGƯỜI NHẬN
# =====================================

# Function returns sample recipient data / Hàm trả về dữ liệu người nhận mẫu
def get_recipient_data():

    return pd.DataFrame({

        "Mã hộ": [
            "H001",
            "H002",
            "H003"
        ],

        "Tên": [
            "Nguyễn Văn A",
            "Trần Thị B",
            "Lê Văn C"
        ],

        "Khu vực": [
            "TP.HCM",
            "Bình Dương",
            "Cần Thơ"
        ],

        "Trạng thái": [
            "Đã xác minh",
            "Ưu tiên cao",
            "Đã hỗ trợ"
        ]
    })


# =====================================
# HISTORY / LỊCH SỬ
# =====================================

# Function returns sample donation history data / Hàm trả về dữ liệu lịch sử quyên góp mẫu
def get_history_data():

    return pd.DataFrame({

        "Ngày": [
            "18/11",
            "15/11",
            "12/11"
        ],

        "Vật phẩm": [
            "Thuốc",
            "Quần áo",
            "Sữa"
        ],

        "Trạng thái": [
            "Đã giao",
            "Đang xử lý",
            "Thiếu"
        ]
    })