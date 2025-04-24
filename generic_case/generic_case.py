# Author： Jonathan Tang
# Date： 2025/04/24
# File： generic_case.py
# Project： Chasing Kinematics Simulation
#
# For MATLAB code, please refer to `generic_chasing_matlab.m` in the `generic_case` folder.


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 初始化参数
# 修改初始角度为36度（转换为弧度）
alpha_initial = np.radians(36)  # 36度转弧度
θ = np.linspace(0, 20*np.pi, 2500)  # 角度范围（保持弧度单位）

# 创建图形和坐标轴
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
plt.subplots_adjust(bottom=0.25)  # 为滑块腾出空间

# 计算初始对数螺线
r = np.exp(θ * (1 / np.tan(alpha_initial)))
line, = ax.plot(θ, r, lw=2)

# 创建滑块轴
# 修改滑块参数为度数显示
ax_alpha = plt.axes([0.2, 0.1, 0.6, 0.03])
alpha_slider = Slider(
    ax=ax_alpha,
    label='α (deg)',  # 标签改为度数
    valmin=5,        # 最小5度
    valmax=85,        # 最大85度
    valinit=36,       # 初始36度
    valfmt='%0.0f°'   # 添加度数符号
)

# 修改更新函数（添加弧度转换）
def update(val):
    current_alpha = np.radians(alpha_slider.val)  # 度数转弧度
    new_r = np.exp(θ * (1 / np.tan(current_alpha)))
    line.set_ydata(new_r)
    fig.canvas.draw_idle()

# 注册更新事件
alpha_slider.on_changed(update)

# 设置极坐标图的显示参数
ax.set_rmax(60)  # 最大半径限制
ax.grid(True)
plt.show()