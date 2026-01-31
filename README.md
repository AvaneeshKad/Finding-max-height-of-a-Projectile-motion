# Projectile Motion: Maximum Height Calculator

This Python project automates the calculation of the maximum height reached by a projectile under different launch conditions. It utilizes nested loops to generate a 2D data matrix, comparing various initial velocities against different launch angles.

## 🚀 Overview

The script calculates H_max​ based on the kinematic formula:

<img width="232" height="104" alt="image" src="https://github.com/user-attachments/assets/bf6382e0-024f-4ede-8425-bfcfbb208e67" />


Where:

- v: Initial velocity (m/s)

- θ: Launch angle (degrees)

- g: Acceleration due to gravity (9.81m/s2)


#🛠️ Implementation Details

The program is structured to:

- Initialize Data: Sets up lists for velocities (10–50m/s) and angles (30∘,45∘,60∘).

- Matrix Computation: Uses a nested for loop to iterate through every combination of velocity and angle.

- Data Storage: Populates a pre-allocated 2D list (matrix) with the results.

- Formatted Output: Prints a clean, tab-separated table for easy data visualization.


## 📊 Sample Output

The script generates a table where the columns represent velocities and the rows represent launch angles:

<img width="395" height="103" alt="image" src="https://github.com/user-attachments/assets/094a06bd-81d4-43f0-a886-c4976c8f914d" />
