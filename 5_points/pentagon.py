# Author： Jonathan Tang
# Date： 2025/04/24
# File： pentagon.py
# Project： Chasing Kinematics Simulation
#
# Problem Description:
# Five particles $A$, $B$, $C$, $D$, and $E$ are located at the five equally 
# spaced positions on a circle of radius $R$ at a certain moment. Assume that 
# each particle moves at a constant speed $v$, and during the motion:
# - Particle $A$ always points toward particle $C$,
# - Particle $B$ always points toward particle $D$,
# - Particle $C$ always points toward particle $E$,
# - Particle $D$ always points toward particle $A$,
# - Particle $E$ always points toward particle $B$.
# Questions:
# 1) How long does it take from the beginning until all five particles converge 
# at a single point?
# 2) Particle $A$ moves along a curved path. What is the radius of curvature of 
# this path at the initial moment?
#
# 问题描述：
# 五个质点$A$、$B$、$C$、$D$、$E$，某一时刻正好位于一个半径为$R$的圆上五个等分的位置。
# 今设各质点均以速率$v$运动，而且在运动中质点$A$始终指着$C$，质点$B$始终指着$D$，质点$C$
# 始终指着$E$，质点$D$始终指着$A$，质点$E$始终指着$B$。试问：
# 1）从开始到五个质点会聚一点经历的时间为多长？
# 2）质点$A$在运动中将沿一条曲线运动，求初始时此曲线的曲率半径为多大？
#


import sys
import os


# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Import the Simulation class from the src module
from src.simulation import Simulation

# 5-point pentagon (A->C, B->D, C->E, D->A, E->B)
sim = Simulation(
    num_points=5,
    radius=1.0,
    speed=0.35,
    target_indices=[2, 3, 4, 0, 1]  # A->C, B->D, C->E, D->A, E->B
)
sim.run()