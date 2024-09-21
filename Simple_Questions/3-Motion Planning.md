# Graph Search Algorithms
Graph searching algorithms are the cornerstone of path planning algorithms, the most popular of which are: BFS, DFS, Dijkstra’s and A\* algorithms 
  
- Briefly describe how each of those algorithms work.  
- Mention the pros and cons of each algorithm. 
BFS:
Explores all nodes level by level from the starting node, using a queue.
Guarantees the shortest path in unweighted graphs.
Inefficient for large graphs, as it explores all nodes.
DFS:
Explores as far as possible along each branch before backtracking, using a stack.
Efficient for deep paths.
Can get stuck in long paths and doesn’t guarantee the shortest path.
Dijkstra’s Algorithm:
Expands the least-cost node at each step, guaranteeing the shortest path in weighted graphs.
Finds the shortest path in weighted graphs.
Computationally expensive for large graphs.
A* Algorithm:
Combines Dijkstra’s and a heuristic function to prioritize paths toward the goal.
Efficient, often faster than Dijkstra’s, guarantees shortest path.
slow

# Practical Motion Planning
A Vaccum cleaning robot uses A\* algorithm to navigate its way through the house, however the paths it navigates are often too rough (Zig-Zag).
- As a motion planning engineer what could be a solution to this problem in the algorithm?  
to use path smoothing techniques post-planning, which remove unnecessary turns by interpolating between waypoints or optimizing the path.
- What is the risk of applying such a solution?
Smoothing may lead to collision risks, as it might cause the robot to take shortcuts that could lead through obstacles, making collision detection more complex.