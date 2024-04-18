import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

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
