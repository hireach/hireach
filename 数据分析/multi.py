import matplotlib
# matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

# mac设置中文
my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc")

y1 = [0,1,1,2,3,2,1,2,1,7,3,6,3,1,2,5,0,3,0,1]
y2 = [0,3,1,5,1,2,1,0,0,1,1,2,2,1,2,5,0,3,0,1]
x = range(10,30)
fig = plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y1,label="自己")
plt.plot(x, y2,label="同桌")

# # 调整x轴刻度
# _x = list(x)[::3]
_xtick_lable = ["{}岁".format(i) for i in x]
# _xtick_lable += ["11点{}分".format(i) for i in range(60)]

plt.xticks(x,_xtick_lable,fontproperties=my_font)

# 添加描述信息
plt.xlabel("岁数",fontproperties=my_font)
plt.ylabel("女朋友数",fontproperties=my_font)
plt.title("女朋友数目",fontproperties=my_font)
plt.grid(alpha=0.4)

# 添加图例
plt.legend(prop=my_font)
#获取最大值最小值的索引
max_indx=y1.index(max(y1))
#设置最大值
plt.plot(x[max_indx],y1[max_indx],'ks')
#显示最大值
show_max='['+str(x[max_indx])+','+str(y1[max_indx])+']'
plt.annotate(show_max,xytext=(x[max_indx],y1[max_indx]),xy=(x[max_indx],y1[max_indx]))
#添加水印
fig.text(0.75, 0.45, 'hello world',
fontsize=40, color='gray',
ha='right', va='bottom', alpha=0.4)
plt.show()
