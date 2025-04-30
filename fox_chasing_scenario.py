# Author： Jonathan Tang
# Date： 2025/04/30
# File： fox_chasing_scenario.py
# Project： Chasing Kinematics Simulation
#
# Problem Description:
# A fox escapes at a constant speed $v_1$ along the straight line $AB$. A hound 
# chases with a constant speed $v_2$, and its pursuit direction always points 
# directly at the fox. At a certain moment, the fox is at point $F$ on line $AB$, 
# and the hound is at point $D$ where the line segment $FD$ is perpendicular 
# to $AB$ and has a length $L$, as shown in the figure. Given that $v_2 > v_1$, 
# how much time will it take for the hound to catch the fox?
#
# 问题描述：
# 一只狐狸以不变的速度$v_{1}$沿直线$AB$逃跑，猎犬以不变的速率$v_{2}$追击，其追击方向始终对
# 准狐狸。某时刻狐狸在$AB$上的$F$处，猎犬在$D$处，$FD \perp AB$，$\overline{FD} = L$，
# 如图所示。设$v_{2} > v_{1}$，问猎犬追上狐狸还需多长时间?
#


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def simulate_chase(v1, v2, L, dt=0.001, max_time=100):
    """
    模拟猎犬追击狐狸的过程
    参数:
        v1: 狐狸的速度
        v2: 猎犬的速度 (v2 > v1)
        L: 初始垂直距离
        dt: 时间步长
        max_time: 最大模拟时间
    返回:
        t: 时间数组
        fox_positions: 狐狸的位置轨迹
        dog_positions: 猎犬的位置轨迹
    """
    # 初始条件
    fox_x, fox_y = 0, 0  # 狐狸初始位置
    dog_x, dog_y = 0, L  # 猎犬初始位置
    
    # 存储轨迹
    fox_positions = [(fox_x, fox_y)]
    dog_positions = [(dog_x, dog_y)]
    time_points = [0]
    
    t = 0
    while t < max_time:
        # 计算狐狸新位置 (沿x轴移动)
        fox_x += v1 * dt
        fox_y = 0
        
        # 计算猎犬到狐狸的方向向量
        dx = fox_x - dog_x
        dy = fox_y - dog_y
        distance = np.sqrt(dx**2 + dy**2)
        
        # 检查是否追上
        if distance < 0.01:
            break
            
        # 计算猎犬新位置 (沿狐狸方向移动)
        dog_x += v2 * dt * (dx / distance)
        dog_y += v2 * dt * (dy / distance)
        
        # 存储结果
        fox_positions.append((fox_x, fox_y))
        dog_positions.append((dog_x, dog_y))
        time_points.append(t)
        
        t += dt
    
    return time_points, fox_positions, dog_positions

def plot_results(t, fox_positions, dog_positions):
    """绘制追击轨迹和动态模拟"""
    fig, ax = plt.subplots(figsize=(12, 8))
    # ax.set_xlim(min(fox_x[0], dog_x[0])-1, max(fox_x[-1], dog_x[-1])+1)
    # ax.set_ylim(min(min(fox_y), min(dog_y))-1, max(max(fox_y), max(dog_y))+1)
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(-5.5, 0.5)
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_title('Pursuit Simulation: Dog Chasing Fox')
    ax.grid(True)
    
    # 绘制完整轨迹
    fox_line, = ax.plot([], [], 'r-', alpha=0.3, label='Fox Path')
    dog_line, = ax.plot([], [], 'b-', alpha=0.3, label='Dog Path')
    
    # 当前点标记
    fox_point, = ax.plot([], [], 'ro', markersize=8, label='Fox')
    dog_point, = ax.plot([], [], 'bo', markersize=8, label='Dog')
    
    # 虚线辅助线
    connection_line, = ax.plot([], [], 'k--', alpha=0.5, linewidth=1, label='Connection')
    
    ax.legend(loc='lower right')
    ax.axis('equal')
    
    def init():
        fox_line.set_data([], [])
        dog_line.set_data([], [])
        fox_point.set_data([], [])
        dog_point.set_data([], [])
        connection_line.set_data([], [])
        return fox_line, dog_line, fox_point, dog_point, connection_line
    
    def update(frame):
        # 更新轨迹
        fox_line.set_data(fox_x[:frame], fox_y[:frame])
        dog_line.set_data(dog_x[:frame], dog_y[:frame])
        
        # 更新当前点 - 修改为使用列表包装坐标值
        fox_point.set_data([fox_x[frame]], [fox_y[frame]])
        dog_point.set_data([dog_x[frame]], [dog_y[frame]])
        
        # 更新虚线辅助线
        connection_line.set_data([fox_x[frame], dog_x[frame]], 
                                [fox_y[frame], dog_y[frame]])
        
        return fox_line, dog_line, fox_point, dog_point, connection_line
    
    # 创建动画
    ani = FuncAnimation(fig, update, frames=len(fox_x),
                        init_func=init, blit=True, interval=1)
    
    plt.show()
    return ani

# 参数设置

gamma = 0.7
v2 = 5.0  # 猎犬速度 (v2 > v1)
v1 = gamma * v2  # 狐狸速度
L = -5.0  # 初始垂直距离

# 运行模拟
t, fox_pos, dog_pos = simulate_chase(v1, v2, L)

# 解压位置数据
fox_x, fox_y = zip(*fox_pos)
dog_x, dog_y = zip(*dog_pos)

# 输出结果
print(f"猎犬在 {t[-1]:.2f} 秒后追上狐狸")
print(f"狐狸最终位置: ({fox_pos[-1][0]:.2f}, {fox_pos[-1][1]:.2f})")
print(f"猎犬最终位置: ({dog_pos[-1][0]:.2f}, {dog_pos[-1][1]:.2f})")

# 绘制动态轨迹
ani = plot_results(t, fox_pos, dog_pos)