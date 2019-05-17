from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc")

a = ["北京", "西京", "东京", "南京"]
b_16 = [1, 2, 3, 4]
b_15 = [2, 1, 3, 1]
b_14 = [4, 3, 4, 4]
x_14 = list(range(len(a)))
x_15 = [i + 0.2 for i in b_15]
x_16 = [i + 0.2 * 2 for i in b_16]

# 图片大小要在最上方设置
plt.figure(figsize=(20,8),dpi=80)

# label设置图例
plt.bar(range(len(a)), b_14, width=0.2,label="14日")
plt.bar(x_15, b_15, width=0.2,label="15日")
plt.bar(x_16, b_16, width=0.2,label="16日")
# 设置图例必须加上legend
plt.legend(prop=my_font)
# 让x轴对应a
plt.xticks(x_15, a, fontproperties=my_font)


plt.show()
