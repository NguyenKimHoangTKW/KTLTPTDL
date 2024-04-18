import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
