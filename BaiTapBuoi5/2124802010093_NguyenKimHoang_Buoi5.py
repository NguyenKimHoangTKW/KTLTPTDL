import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

def BaiTap1():
    X = np.array([[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,0,1],[1,0,1],[0,1,1],[1,1,1]])
    Y = np.array([[0,0,0,0,0,0,0,1]]).T
    W = np.random.random((3,1))
    for i in range(10000):
        z = np.dot(X,W)
        O = 1 / (1 + np.exp(-z))
        W -= np.dot(X.T,(O-Y) * O * (1-O))
    print(W)

def BaiTap2():
    data = pd.read_excel("Covid_19.xlsx")

    data = data.replace('-', np.nan)

    data['Lãnh thổ'] = data['Lãnh thổ'].astype(str)

    fig, ax = plt.subplots(figsize=(100, 6))

    for col in ['Lây nhiễm', 'Tử vong', 'Nghiêm trọng', 'Phục hồi']:
        ax.plot(data['Lãnh thổ'], data[col], marker='o', label=col)

    ax.set_title('Biểu đồ số ca nhiễm, tử vong, nghiêm trọng và phục hồi theo vùng lãnh thổ')
    ax.set_xlabel('Vùng lãnh thổ')
    ax.set_ylabel('Số lượng')
    ax.legend()

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def BaiTap3():
    df = pd.read_csv('insulin.csv')

    plt.figure(figsize=(10, 6))

    male_data = df[df['sex'] == 0]
    female_data = df[df['sex'] == 1]

    plt.scatter(male_data['age'], male_data['insulin'], color='blue', label='Male')
    plt.scatter(female_data['age'], female_data['insulin'], color='red', label='Female')

    plt.title('Biểu đồ tán xạ biểu diễn mối liên hệ giữa độ tuổi (Age) với lượng insulin (insulin) theo giới tính.')
    plt.xlabel('Tuổi')
    plt.ylabel('Insulin')
    plt.legend()

    plt.grid(True)
    plt.show()

def BaiTap4():
    df = pd.read_csv('VNIndex_ByWeekDay.csv')
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
    
def BaiTap5():
    data = pd.read_excel("Covid_19.xlsx")

    data = data[data['Lãnh thổ'] != 'WORLD']

    top_10_regions = data.sort_values(by='Lây nhiễm', ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10, 6))

    for col in ['Lây nhiễm', 'Tử vong', 'Nghiêm trọng', 'Phục hồi']:
        ax.plot(top_10_regions['Lãnh thổ'], top_10_regions[col], marker='o', label=col)

    ax.set_title('Biểu đồ số ca nhiễm, tử vong, nghiêm trọng và phục hồi theo 10 vùng lãnh thổ có số lượng lớn nhất')
    ax.set_xlabel('Lãnh thổ')
    ax.set_ylabel('Số lượng')
    ax.legend()

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    formatter = FuncFormatter(lambda x, pos: '{:,.0f}'.format(x/1000000) + ' triệu' if x != 0 else '0')
    ax.yaxis.set_major_formatter(formatter)

    plt.ylim(0, 70000000) 
    plt.yticks(range(0, 70000001, 5000000), ['0', '5 triệu', '10 triệu', '15 triệu', '20 triệu', '25 triệu', '30 triệu', '35 triệu', '40 triệu', '45 triệu', '50 triệu', '55 triệu', '60 triệu', '65 triệu', '70 triệu'])
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

while True:
    print("MENU")
    print("Bài làm Buổi 5 của sinh viên NGUYỄN KIM HOÀNG")
    print("----------------------------------------------------------------------------------")
    print("1. Cài đặt mô hình ANN cho cổng AND ba ngõ vào")
    print("2. Vẽ line chart biểu diễn số ca nhiễm, tử vong, nghiêm trọng và phục hồi theo vùng lãnh thổ.")
    print("3. Vẽ biểu đồ Scatter plot (biểu đồ tán xạ) biểu diễn mối liên hệ giữa độ tuổi (Age) với lượng insulin (insulin) theo giới tính")
    print("4. Thể hiện chỉ số VN_Index_Rate của 10 dòng đầu tiên và 10 dòng cuối cùng | Thể hiện chỉ số VN_Index_Rate của 10 dòng cuối cùng | Thể hiện chỉ số VN_Index_Rate của dòng từ 11 đến 30")
    print("5. Vẽ line chart biểu diễn số ca nhiễm, tử vong, nghiêm trọng và phục hồi theo 10 vùng lãnh thổ có số lượng lớn nhất")
    print("Nhập 0 để kết thúc chương trình")
    print("----------------------------------------------------------------------------------")
    choice = input("Vui lòng chọn bài toán :")
    print("----------------------------------------------------------------------------------")
    if choice == "1":
        print("----------------------------------------------------------------------------------")
        BaiTap1()
        print("----------------------------------------------------------------------------------")
    elif choice == "2":
        print("----------------------------------------------------------------------------------")
        BaiTap2()
        print("----------------------------------------------------------------------------------")
    elif choice == "3":
        print("----------------------------------------------------------------------------------")
        BaiTap3()
        print("----------------------------------------------------------------------------------")
    elif choice == "4":
        print("----------------------------------------------------------------------------------")
        BaiTap4()
        print("----------------------------------------------------------------------------------")
    elif choice == "5":
        print("----------------------------------------------------------------------------------")
        BaiTap5()
        print("----------------------------------------------------------------------------------")
    elif choice =="0":
        print("GoodBye")
        break
    else:
        print("Sai lựa chọn, vui lòng chọn lại từ 1 đến 16")