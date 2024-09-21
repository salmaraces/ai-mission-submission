# Introduction
In this section of the mission you are supposed to read the attached paper throroughly and unserstand as much as you can of it, to answer the following questions.
You will also discuss the paper further in the interview.

# General Questions
- Why is autonomous racing challenging?
Autonomous racing involves managing high-speed dynamics while ensuring real-time, reliable decision-making under rapidly changing conditions. These races push both hardware and software to their limits, requiring advanced algorithms that must react quickly to obstacles, other vehicles, and the environment to maintain competitiveness and safety.
- What is meany by infrastructure-less localization?
Infrastructure-less localization refers to determining a vehicle’s position on the track without relying on external tools or systems, like GPS or specialized sensors. The car must localize itself using onboard sensors and mapping algorithms, making it more adaptable to diverse environments.

# Frenet Coordinates
- Explain Frenet coordinates.
Frenet coordinates are a reference system based on a vehicle’s position along a path or curve. Instead of standard Cartesian coordinates, positions are expressed relative to the path itself: one coordinate measures the distance along the curve, and the other measures lateral displacement from it.
- Mention the advantage of using Frenet coordiantes
Frenet coordinates simplify path-following tasks in autonomous driving by directly relating a vehicle's movement to the road or track, making it easier to compute the required steering or throttle inputs for staying on a desired path.

# State Estimation
- What is the role of the IMU?
The IMU measures the car's acceleration and angular velocity, providing data for estimating the vehicle’s state, including orientation and movement, which helps maintain control.
- Explain the used state estimation method.
The ForzaETH Race Stack uses a combination of sensor fusion and estimation techniques to accurately predict the vehicle's position and velocity. This involves integrating IMU data with information from other sensors like LiDAR to continuously update the vehicle's state.

# Perception
- What features are extracted from LiDAR detections?
LiDAR is used to detect obstacles, including other race cars and static objects. It provides data for creating a real-time map of the surroundings, detecting distances, and identifying the shapes and positions of objects around the vehicle.
- Why was an opponent tracking module added?
The opponent tracking module is critical in Head-to-Head racing scenarios. It helps predict the movements of competing vehicles, enabling the planning module to avoid collisions and make strategic overtakes.

# Motion planning and Control
- What is the purpose of the local planner?
The local planner generates real-time, short-term paths for the vehicle to follow, based on sensor inputs and the current environment. It ensures that the car remains on the track while avoiding dynamic and static obstacles.
-  What are the roles of the lateral and longitudinal controllers?
Lateral controller: Manages the vehicle’s steering to keep it on the desired path.
Longitudinal controller: Controls speed and acceleration, ensuring smooth braking and throttle adjustments based on track conditions and opponent positions.