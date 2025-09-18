import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Đọc dữ liệu từ Excel
file_path = "khaosatTHPT.xlsx"   
df = pd.read_excel(file_path,sheet_name="khaosatTHPT")

#print(df.head())
# 2. Lấy các cột cần thiết
# tên,điểm, ttNV
df_small = df[["diemTHPT","ttNV"]]
#print(df_small.head())
# ép điểm sang float
df_small.loc[:,"diemTHPT"] = (
    df_small["diemTHPT"]
    .astype(str)
    .str.replace(",",".", regex=False)
    .astype(float)
    )
#print(df_small.dtypes)
#lấy số thứ tự nguyện vọng
df_small["ttNV"] = (
    df_small["ttNV"]
    .astype(str)
    .str.extract(r'Nguyện vọng\s*(\d+)', expand=False)
    .astype(float)
    .astype("Int64")
    )
#print(df_small.head)
mean_value   = df_small["diemTHPT"].mean()    # trung bình
median_value = df_small["diemTHPT"].median()  # trung vị
var_value    = df_small["diemTHPT"].var()     # phương sai 
std_value    = df_small["diemTHPT"].std()     # độ lệch chuẩn 

print("Trung bình:", mean_value)
print("Trung vị:", median_value)
print("Phương sai:", var_value)
print("Độ lệch chuẩn:", std_value)
