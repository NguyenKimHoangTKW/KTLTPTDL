import pandas as pd
import matplotlib.pyplot as plt

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
