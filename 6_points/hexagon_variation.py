# Author： Jonathan Tang
# Date： 2025/04/24
# File： hexagon_variation.py
# Project： Chasing Kinematics Simulation
#
# Extended from hexagon.py

import sys
import os


# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Import the Simulation class from the src module
from src.simulation import Simulation

# 6-point scenario (each point chases the next)
sim = Simulation(
    num_points=6,
    radius=1.0,
    speed=0.35,
    target_indices=[1, 2, 3, 4, 5, 0]  # Each point chases the next
)
sim.run()
