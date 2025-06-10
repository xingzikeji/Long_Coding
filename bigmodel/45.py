# 训练的结果测试结果 后场

import scipy.io
import numpy as np
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter
params={
    'axes.labelsize': '12',
    'xtick.labelsize':'12',
    'ytick.labelsize':'12',
    'lines.linewidth':2 ,
    'legend.fontsize': '12',
    'figure.figsize'   : '18, 6'
}
pylab.rcParams.update(params)
# plt.style.use('bmh')
savefile = "C:\\Users\\lxl\\Desktop\\Doctor\\chapt03\\"


# 定义数据
categories = ['Baseline-BT', 'PSRO-BT', 'VDN-BT', 'QMIX-BT', 'PSRO-BT', 'MASK-VDN-BT', 'MASK-QMIX-BT', 'DyHG-MASK-PSRO-BT', 'DyHG-MASK-VDN-BT', 'DyHG-MASK-QMIX-BT']
values = [55.031, 57.123, 62.235, 64.135, 58.956, 67.456, 69.12, 58.956, 69.125, 73.956]  # 假设这些值代表百分比

# 转换为百分比形式
values = np.array(values)


# 设置字体
# plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']
# plt.rcParams['axes.unicode_minus'] = False

# 自定义柱子宽度
bar_width = 0.1

# 定义不同的颜色
colors = ['gray','yellow', 'red', 'green', 'blue', 'black', 'orange', 'purple', 'brown', 'pink']

# 绘制柱状图
fig, ax = plt.subplots()
bars = []
print()
for i, category in enumerate(categories):
#     if category=='Baseline-BT':
#         bar = ax.bar(category, values[i], width=bar_width + 0.2, color=colors[i], edgecolor='black', label=category, alpha=0.6)
#         bars.append(bar)
#     if category=='PSRO-BT':
#         bar = ax.bar(category, values[i], width=bar_width + 0.2, color=colors[i], edgecolor='black', label=category, alpha=0.6)
#         bars.append(bar)
#     if category=='VDN-BT':
#         bar = ax.bar(category, values[i], width=bar_width + 0.2, color=colors[i], edgecolor='black', label=category, alpha=0.6)
#         bars.append(bar)
#     if category=='QMIX-BT':
#         bar = ax.bar(category, values[i], width=bar_width + 0.2, color=colors[i], edgecolor='black', label=category, alpha=0.6)
#         bars.append(bar)
#     if category=='MASK-VDN-BT':
#         bar = ax.bar(category, values[i], width=bar_width + 0.2, color=colors[i], edgecolor='black', label=category, alpha=0.6)
#         bars.append(bar)
#     if category=='MASK-PSRO-BT':
#         bar = ax.bar(category, values[i], width=bar_width + 0.2, color=colors[i], edgecolor='black', label=category, alpha=0.6)
#         bars.append(bar)
#     if category=='MASK-QMIX-BT':
#         bar = ax.bar(category, values[i], width=bar_width + 0.2, color=colors[i], edgecolor='black', label=category, alpha=0.6)
#         bars.append(bar)
#     if category=='DyHG-MASK-PSRO-BT':
#         bar = ax.bar(category, values[i], width=bar_width + 0.2, color=colors[i], edgecolor='black', label=category, alpha=0.6)
#         bars.append(bar)
#     if category=='DyHG-MASK-VDN-BT':
#         bar = ax.bar(category, values[i], width=bar_width + 0.2, color=colors[i], edgecolor='black', label=category, alpha=0.6)
#         bars.append(bar)
#     if category=='DyHG-MASK-QMIX-BT':
#         bar = ax.bar(category, values[i], width=bar_width + 0.2, color=colors[i], edgecolor='black', label=category, alpha=0.6)
#         bars.append(bar)

    bar = ax.bar(category, values[i], width=bar_width + 0.2, color=colors[i], edgecolor='black', label=category, alpha=0.6)
    bars.append(bar)

# 添加标题和标签
# ax.set_title('定制的柱状图', fontsize=16, fontweight='bold')
# ax.set_xlabel('类别', fontsize=12)
# ax.set_ylabel('百分比', fontsize=12)

# 设置 y 轴范围为 0 到 100，并以百分比形式显示
ax.set_ylim(0, 100)
ax.yaxis.set_major_formatter(PercentFormatter())

ax.legend(loc='upper center', ncol=2)

# 不显示 X 轴标签
ax.set_xticklabels([])

# 隐藏 X 轴的刻度线和标签
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

plt.grid(True,linestyle='-.',color='grey',alpha=0.6, zorder=3)
plt.legend(loc="upper left", frameon=False, ncol = 2, fontsize=10)
plt.savefig(savefile + "total-result.pdf", dpi=1200)

# 调整图形布局
plt.tight_layout()

# 显示图形
plt.show()
