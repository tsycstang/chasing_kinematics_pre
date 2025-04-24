# Author： Jonathan Tang
# Date： 2025/04/24
# File： pentagon_variation.py
# Project： Chasing Kinematics Simulation
#
# Extended from pentagon.py



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
    target_indices=[1, 2, 3, 4, 0]  # A->B, B->C, C->D, D->E, E->A
)
sim.run()