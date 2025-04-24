# Author： Jonathan Tang
# Date： 2025/04/23
# File： simulation.py
# Project： Chasing Kinematics Simulation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import List, Tuple, Optional

class Simulation:
    def __init__(self, num_points: int, radius: float, speed: float, 
                 target_indices: List[int], dt: float = 0.005):
        """
        Initialize the simulation with given parameters.
        
        Args:
            num_points: Number of points in the simulation
            radius: Initial radius of the circle
            speed: Speed of each point
            target_indices: List of target indices for each point
            dt: Time step for the simulation
        """
        self.num_points = num_points
        self.radius = radius
        self.speed = speed
        self.dt = dt
        self.target_indices = target_indices
        
        # Initialize positions
        angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
        self.positions = np.zeros((num_points, 2))
        for i in range(num_points):
            self.positions[i, 0] = radius * np.cos(angles[i])
            self.positions[i, 1] = radius * np.sin(angles[i])
        
        # Initialize trajectories
        self.trajectories = [[self.positions[i].copy()] for i in range(num_points)]
        
        # Initialize plot
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-radius * 1.2, radius * 1.2)
        self.ax.set_ylim(-radius * 1.2, radius * 1.2)
        self.ax.set_title(f"{num_points}-Points Motion Simulation")
        
        # Draw initial circle
        circle = plt.Circle((0, 0), radius, color='g', fill=False, 
                          linestyle='--', alpha=0.3, linewidth=0.5)
        self.ax.add_patch(circle)
        
        # Initialize trajectory lines and point markers
        self.lines = []
        for i in range(num_points):
            line, = self.ax.plot([], [], marker='o', markersize=1, 
                               label=f'Point {chr(65+i)}')
            self.lines.append(line)
        self.ax.legend(loc='upper left')
        
        # Initialize target lines
        self.target_lines = []
        for i in range(num_points):
            line, = self.ax.plot([], [], 'r--', alpha=0.3, linewidth=0.5)
            self.target_lines.append(line)
    
    def update(self, frame: int) -> List[plt.Line2D]:
        """Update the simulation for each frame."""
        new_positions = self.positions.copy()
        
        # Update positions based on targets
        for i in range(self.num_points):
            target = self.positions[self.target_indices[i]]
            direction = target - self.positions[i]
            norm = np.linalg.norm(direction)
            if norm != 0:
                direction /= norm
            new_positions[i] = self.positions[i] + self.speed * self.dt * direction
            self.trajectories[i].append(new_positions[i].copy())
        
        self.positions[:] = new_positions
        
        # Update trajectory lines
        for i in range(self.num_points):
            traj = np.array(self.trajectories[i])
            self.lines[i].set_data(traj[:, 0], traj[:, 1])
        
        # Update target lines (connecting each point to its target)
        for i in range(self.num_points):
            target_idx = self.target_indices[i]
            self.target_lines[i].set_data(
                [self.positions[i, 0], self.positions[target_idx, 0]],
                [self.positions[i, 1], self.positions[target_idx, 1]]
            )
        
        return self.lines + self.target_lines
    
    def run(self, frames: int = 10000, interval: int = 5):
        """Run the simulation animation."""
        ani = FuncAnimation(self.fig, self.update, frames=frames, 
                          interval=interval, blit=True)
        plt.show()