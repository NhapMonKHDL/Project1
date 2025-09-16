import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

#1. Đọc dữ liệu từ Excel
file_path = "khaosat.xlsx" 
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Đổi tên cột cho dễ xử lý
df = df.rename(columns={
    "Họ và Tên": "HoTen",
    "Giới tính": "GioiTinh",
    "Tuổi": "Tuoi",
    "Chiều cao (cm)": "ChieuCao"
})

#2Chuẩn hoá Z-score 
scaler = StandardScaler()
df["ChieuCao_Z"] = scaler.fit_transform(df[["ChieuCao"]])

# 3. Thống kê mô tả
mean = df["ChieuCao"].mean()
median = df["ChieuCao"].median()
var = df["ChieuCao"].var()
std = df["ChieuCao"].std()
min_val = df["ChieuCao"].min()
max_val = df["ChieuCao"].max()

print("📊 Thống kê mô tả chiều cao (cm):")
print(f"Trung bình: {mean:.2f}")
print(f"Trung vị: {median:.2f}")
print(f"Phương sai: {var:.2f}")
print(f"Độ lệch chuẩn: {std:.2f}")
print(f"Min: {min_val:.2f}")
print(f"Max: {max_val:.2f}")

#  4. Vẽ biểu đồ 
plt.figure(figsize=(14,6))

# Histogram
plt.subplot(1,2,1)
sns.histplot(df["ChieuCao"], bins=20, kde=True, color="skyblue")
plt.axvline(mean, color="red", linestyle="--", label=f"Mean = {mean:.2f}")
plt.axvline(median, color="green", linestyle="-.", label=f"Median = {median:.2f}")
plt.title("Phân phối Chiều cao (Histogram)")
plt.xlabel("Chiều cao (cm)")
plt.ylabel("Tần suất")
plt.legend()

# Boxplot
plt.subplot(1,2,2)
sns.boxplot(y=df["ChieuCao"], color="lightcoral")
plt.title("Boxplot Chiều cao")

plt.tight_layout()
plt.show()
