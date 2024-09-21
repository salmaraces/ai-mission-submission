# Perception Sensors
- Explain the working principles (i.e. how they capture data from the environments, the type of data captured, data processing requirements, etc.) of radars, lidars and cameras.
Radar: Radars emit radio waves that bounce off objects and return to the sensor. By measuring the time delay and the frequency shift of the reflected waves, they capture data such as distance, velocity, and angle..
LiDAR: LiDAR uses laser pulses to measure distances by calculating the time it takes for light to reflect off objects. It generates high-resolution 3D point clouds, which require intensive data processing to identify objects and their shapes.
Cameras: Cameras capture 2D images using visible or infrared light. They provide rich texture and color information but require advanced algorithms to interpret depth, object recognition, and classification.

# Stereo Vision
- Explain how two cameras can be used to get 3D poisition information about objects.
Stereo vision uses two cameras positioned at a distance from each other to mimic human vision. By capturing images from slightly different perspectives, the disparity is computed. This disparity helps calculate the depth and 3D position of objects using triangulation.

# Machine Learning
- What are neural networks? How do they learn?
Neural networks are computing systems made of interconnected layers of neurons. They learn by adjusting the weights of connections between neurons during training, optimizing performance on specific tasks such as classification or regression.

- How can neural networks be used to aid with processing sensor data for envorionment perception?
Neural networks process sensor data by learning patterns from raw input, such as images or LiDAR point clouds. For example, convolutional neural networks (CNNs) can detect objects, classify them, and interpret complex scenes, enhancing the vehicle's understanding of its surroundings. They are used for tasks like object detection, lane detection, and obstacle avoidance.