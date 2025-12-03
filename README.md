Shortest Path Roadmap (SPR) — Motion Planning for a Point Robot

This project implements a complete Shortest Path Roadmap (SPR) algorithm for a translating point robot navigating a 2D environment with polygonal obstacles.
The system constructs a visibility-based roadmap, then uses Uniform-Cost Search to compute the optimal collision-free path.

This project was completed for Rutgers CS 460/560 (Computational Robotics).
Technologies used: Python, NumPy, Matplotlib.

Features Implemented
1. Reflex Vertex Detection

Identifies all reflex vertices from polygonal obstacles

Implements geometric orientation checks

Outputs a clean list of vertex coordinates
✔ Demonstrates understanding of computational geometry and polygon structures


2. Roadmap Construction

Connects all mutually visible reflex vertices

Performs line-of-sight collision checks against all obstacles

Builds:
vertexMap: {vertex_id: (x, y)}

adjListMap: {vertex_id: [[neighbor_id, dist], ...]}
✔ Shows experience with graph building, geometric algorithms, and distance computation

3. Uniform-Cost Search (UCS)

Implements UCS from scratch

Computes the true shortest weighted path

Returns both the vertex path and cumulative cost
✔ Demonstrates mastery of classical search algorithms and priority-queue logic

4. Start/Goal Integration

Inserts start and goal points into the roadmap dynamically

Computes new visible edges and updates adjacency lists

Calls UCS to compute final path
✔ Reflects knowledge of dynamic graph expansion and real-world navigation pipelines

5. Optional Visualization (Bonus)

Visualizes:

Obstacles

Roadmap edges (green)

Computed shortest path (red)

Uses Matplotlib for 2D rendering
✔ Demonstrates data visualization and debugging skills

📁 Project Structure
your_netid/
│── spr/
│   ├── spr.py            # Core SPR algorithm implementation
│   ├── visualize.py      # Environment + roadmap visualization
│── env_01.txt            # Polygonal obstacle file (example)

🚀 How to Run
Visualize the environment
python visualize.py env_01.txt

Run the SPR algorithm
python spr.py env_01.txt x_start y_start x_goal y_goal


Example:

python spr.py env_01.txt 1.0 2.0 3.0 4.0

🧠 Skills Demonstrated (Employer-Friendly Summary)

Computational geometry

Polygon processing, reflex vertex detection, visibility testing

Graph algorithms

Custom adjacency lists, weighted edges

Search algorithms

Uniform-Cost Search, priority queue optimization

Clean code organization

Modular Python structure, reusable functions

Data visualization

Rendering environments and paths with Matplotlib

📌 Future Extensions

Support for circular obstacles

Performance optimization using spatial indexing

GUI for interactive path-planning demos

Extension to rotational robots (C-space obstacles)
