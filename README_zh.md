# chasing_kinematics_pre

**英文说明见 `README.md`**

本代码仓库包含了多点追及问题的运动学模拟代码。

## 问题描述

**本代码仓库讨论了程稼夫著的《中学奥林匹克竞赛物理教程 力学篇（第2版）》第2章习题2-10和习题2-29的追及运动学问题。**

### 2-10

![Problem](problem_img.jpeg)


如图所示，五个质点$A$、$B$、$C$、$D$、$E$，某一时刻正好位于一个半径为$R$的圆上五个等分的位置。今设各质点均以速率$v$运动，而且在运动中：

- 质点$A$始终指向质点$C$，
- 质点$B$始终指向质点$D$，
- 质点$C$始终指向质点$E$，
- 质点$D$始终指向质点$A$，
- 质点$E$始终指向质点$B$。

问题：

1）从开始到五个质点会聚一点经历的时间为多长？

2）质点$A$在运动中将沿一条曲线运动，求初始时此曲线的曲率半径为多大？

### 2-29

一只狐狸以不变的速度$v_{1}$沿直线$AB$逃跑，猎犬以不变的速率$v_{2}$追击，其追击方向始终对准狐狸。某时刻狐狸在$AB$上的$F$处，猎犬在$D$处，$FD \perp AB$，$\overline{FD} = L$。设$v_{2} > v_{1}$，问猎犬追上狐狸还需多长时间?

## 使用说明

### 2-10

对于模拟示例，请参考 `5_points` 和 `6_points` 文件夹。

对于通用情况的交互式绘图（其中仅将切线与径向轴之间的角度定义为参数），请参考 `generic_case` 文件夹。

`main.py` 目前仅作装饰用。

### 2-29

见`fox_chasing_scenario.py`。

## 运行要求

1. Python 3
2. Numpy
3. Matplotlib

在通用情况下的轨迹模拟我们也提供了MATLAB代码。

## 代码仓库地址

[GitHub: tsycstang/chasing_kinematics_pre](https://github.com/tsycstang/chasing_kinematics_pre)

[Gitee: Jonathan Toh/chasing_kinematics_pre](https://gitee.com/tech-navigator-jonathan-toh/chasing_kinematics_pre)

## 许可证

**MIT**