import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Sale.csv")

# Số lượng dòng và cột trong bảng dữ liệu
num_rows, num_cols = df.shape
print(f"Số lượng dòng: {num_rows}")
print(f"Số lượng cột: {num_cols}")
print("--------------------------------------------")
# Xem nội dung của cột nào chứa dữ liệu không hợp lệ
for col in df.columns:
    if df[col].dtype == 'O':
        print(f"Cột {col} có dữ liệu không hợp lệ: {df[col].isnull().sum()} giá trị null")
print("--------------------------------------------")
# Số lượng nhóm khách hàng (Segment)
num_segments = df['Segment'].nunique()
print(f"Số lượng nhóm khách hàng: {num_segments}")
print("Các nhóm khách hàng:")
print(df['Segment'].unique())
print("--------------------------------------------")
# Số lượng hình thức giao hàng (Ship Mode)
num_ship_modes = df['Ship Mode'].nunique()
print(f"Số lượng hình thức giao hàng: {num_ship_modes}")
print("Các hình thức giao hàng:")
print(df['Ship Mode'].unique())
print("--------------------------------------------")
# Số lượng khu vực bán hàng (Region)
num_regions = df['Region'].nunique()
print(f"Số lượng khu vực bán hàng: {num_regions}")
print("Các khu vực bán hàng:")
print(df['Region'].unique())
print("--------------------------------------------")
# Số lượng loại sản phẩm (Category)
num_categories = df['Category'].nunique()
print(f"Số lượng loại sản phẩm: {num_categories}")
print("Các loại sản phẩm:")
print(df['Category'].unique())
print("--------------------------------------------")
# Số lượng hình thức thanh toán (Payment Mode)
num_payment_modes = df['Payment Mode'].nunique()
print(f"Số lượng hình thức thanh toán: {num_payment_modes}")
print("Các hình thức thanh toán:")
print(df['Payment Mode'].unique())

# Xóa các cột bị lỗi dữ liệu 
print("--------------------------------------------")
# Số lượng khách hàng
num_customers = df['Customer ID'].nunique()
print(f"Số lượng khách hàng: {num_customers}")
print("--------------------------------------------")
# Tổng số lượng sản phẩm
total_quantity = df['Quantity'].sum()
print(f"Tổng số lượng sản phẩm: {total_quantity}")
print("--------------------------------------------")
# Tổng doanh thu
total_sales = df['Sales'].sum()
print(f"Tổng doanh thu: {total_sales}")
print("--------------------------------------------")
# Thống kê số lượng khách hàng theo hình thức giao hàng và nhóm khách hàng
customer_counts = df.groupby(['Ship Mode', 'Segment'])['Customer ID'].count()
print("Thống kê số lượng khách hàng theo hình thức giao hàng và nhóm khách hàng :")
print(customer_counts)
print("--------------------------------------------")
# Thống kê số lượng khách hàng theo nơi chốn và vẽ biểu đồ biểu diễn
region_customer_counts = df.groupby('Region')['Customer ID'].count()
print("Thống kê số lượng khách hàng theo nơi chốn :")
print(region_customer_counts)

region_customer_counts.plot(kind='bar', color='skyblue')
plt.title('Thống kê số lượng khách hàng theo nơi chốn')
plt.xlabel('Khu vực bán hàng')
plt.ylabel('Số lượng khách hàng')
plt.xticks(rotation=45) 
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() 
plt.show()
