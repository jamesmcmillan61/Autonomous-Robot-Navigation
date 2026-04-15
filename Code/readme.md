# LIMO Car Navigation Setup

All commands assume you are in a terminal with access to ROS 2 Humble and Gazebo (Ignition).

## Prerequisites

- ROS 2 Humble installed and sourced (`/opt/ros/humble/setup.bash`)
- LIMO robot simulation packages cloned into `~/limo_ws/src`
- Gazebo (Ignition) available for simulation

---

## 1. Build the Workspace

Build the LIMO workspace once before running any launch files.

```bash
cd ~/limo_ws
colcon build --symlink-install
source install/setup.bash
```

## 2. Generate a Map with SLAM

Start the SLAM toolbox and drive the robot around to create a map.

### 2.1 Launch SLAM and Gazebo

```bash

source /opt/ros/humble/setup.bash   # only needed if not sourced already
source ~/limo_ws/install/setup.bash
ros2 launch limo_car limo_car_slam.launch.py
This launches the LIMO robot in a Gazebo world and starts slam_toolbox.

```

### 2.2 Teleoperate the Robot

In a new terminal, run the keyboard teleop node to manually drive the robot and explore the environment.

```bash
source /opt/ros/humble/setup.bash
source ~/limo_ws/install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
Use the keys shown in the terminal (u, i, o, j, k, l, m, ,, ., /) to control the robot.
```

### 2.3 Visualize the Map in RViz (Optional)

In another terminal, open RViz2 to see the map being built in real time.

```bash

source /opt/ros/humble/setup.bash
source ~/limo_ws/install/setup.bash
rviz2 --ros-args -p use_sim_time:=true
Add the Map display and set its topic to /map.
```

### 2.4 Save the Generated Map

Once you have covered the desired area, save the map to disk.

```bash
cd ~
ros2 service call /slam_toolbox/save_map slam_toolbox/srv/SaveMap "{name: 'week5_map'}"
The map will be saved as week5_map.yaml and week5_map.pgm in your home directory (~/).
You can move it to a dedicated maps folder later, e.g., ~/limo_ws/maps/.
```

## 3. Launch Navigation

Now use the saved map to navigate autonomously with Nav2.

### 3.1 Start Nav2 and Gazebo

In a terminal, launch the navigation stack.

```bash

source /opt/ros/humble/setup.bash
source ~/limo_ws/install/setup.bash
ros2 launch limo_car limo_car_nav2.launch.py
```

### 3.2 Open RViz with Nav2 Default View

In a new terminal, launch RViz2 with the standard Nav2 configuration.

```bash
source /opt/ros/humble/setup.bash
source ~/limo_ws/install/setup.bash
rviz2 -d $(ros2 pkg prefix nav2_bringup)/share/nav2_bringup/rviz/nav2_default_view.rviz --ros-args -p use_sim_time:=true
```

### 3.3 Set Initial Pose and Navigation Goal

In RViz:

Click the 2D Pose Estimate button, then click on the map where the robot currently is and drag to set its orientation.

Click the 2D Nav Goal button, then click on a destination point and drag to set the desired final orientation.

The robot will plan a path and start moving autonomously.

## 4. (Optional) Add a Dynamic Obstacle

Spawn a moving box to test obstacle avoidance.

```bash

gz model --spawn-file ~/limo_ws/src/limo_car/models/moving_box/moving_box.sdf --model-name moving_obstacle -x 0 -y 0 -z 0.25
```

