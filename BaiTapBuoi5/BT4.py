import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('VNIndex_ByWeekDay.csv')

# Tạo lưới 1x3 cho 3 biểu đồ
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Biểu đồ 1: 10 dòng đầu và 10 dòng cuối
axs[0].plot(df['STT'][:10], df['Vnindex_rate'][:10], label='10 dòng đầu', marker='o')
axs[0].plot(df['STT'][-10:], df['Vnindex_rate'][-10:], label='10 dòng cuối', marker='o')
axs[0].set_title('Chỉ số VN_Index_Rate của 10 dòng đầu và 10 dòng cuối cùng')
axs[0].set_xlabel('STT')
axs[0].set_ylabel('VN Index Rate')
axs[0].legend()
axs[0].grid(True)

# Biểu đồ 2: 10 dòng cuối
axs[1].plot(df['STT'][-10:], df['Vnindex_rate'][-10:], label='10 dòng cuối', marker='o')
axs[1].set_title('Chỉ số VN_Index_Rate của 10 dòng cuối cùng')
axs[1].set_xlabel('STT')
axs[1].set_ylabel('VN Index Rate')
axs[1].legend()
axs[1].grid(True)

# Biểu đồ 3: dòng từ 11 đến 30
axs[2].plot(df['STT'][10:30], df['Vnindex_rate'][10:30], label='dòng 11 to 30', marker='o')
axs[2].set_title('Chỉ số VN_Index_Rate của dòng từ 11 đến 30')
axs[2].set_xlabel('STT')
axs[2].set_ylabel('VN Index Rate')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()
