# Autonomous Robot Navigation Evidence

# 701028 Autonomous Robots

## James McMillan | 202202995

[**SLAM**](#slam)

[**Localisation**](#localisation)

[**Navigation (DWA)**](#navigation-\(dwa\))

[**Navigation (A\*)**](#navigation-\(a*\))

[**Safety / recovery behaviours**](#safety-/-recovery-behaviours)

[**Dynamic obstacles**](#dynamic-obstacles)

[**Fault Scenarios**](#fault-scenarios)

# SLAM

## **Camera Feed During Mapping**

GIF of the robot’s camera view while manually teleoperating the robot to build the map.


## **Map Building (RVis view)**

GIF showing the map in RViz evolving as the robot moves through the environment (two different timestamps).

## **Before Loop Closure Fix**

GIF of the map before loop closure – show distortion, duplication, or misalignment (e.g., walls overlapping).

## **After Loop Closure Fix**

GIF of the same area after loop closure – map now correctly aligned and continuous.

## **Returning to a Known Location for Loop Closure**

GIF of the robot revisiting a previously mapped area, triggering loop closure correction.

# Localisation

## **Initial Pose Estimation (Before Manual Pose)**

GIF showing LIDAR scan not aligned with the static map (red scan lines mismatched with walls).

## **After Manual Poseing**

GIF showing LIDAR scan correctly aligned with the map after user sets initial pose in RViz.



## **Localisation Stability During Navigation**

GIF of a long navigation run with the robot’s pose estimate remaining stable (no drift, scan stays aligned).



## **AMCL Correcting Minor Drift**

GIF where the robot starts with a small pose error and AMCL gradually corrects it back into alignment.

# Navigation (DWA)

## **DWA Start-to-Goal Run (Before Tuning)**

GIF of DWA navigation with default inflation radius – robot gets too close to walls.

## **DWA After Increasing Inflation Radius**

GIF of DWA with increased inflation radius – robot stays safely away from walls and reaches goal.

## **DWA Stop-Start Behaviour**

GIF showing DWA frequently pausing and re-evaluating path (characteristic behaviour).


# Navigation (A\*)

## **9.1.4 – A\* Collision Before Fix (Sim Time Issue)**

GIF of A navigation colliding with a wall despite a clear planned path – show the collision.

## **A\* After Enabling Sim Time**

GIF of A successfully following the planned path and reaching goal without collision.

## **A\* Doorway Getting Stuck (Before Parameter Tuning)**

GIF of A getting stuck in a doorway and triggering “goal failed” error.

## **A\* Successful Navigation After Tuning**

GIF of A completing the same navigation smoothly and reaching goal.

## **A\* Re-planning**

GIF showing A hesitate at a junction then re-plan the optimal route.

# Safety / recovery behaviours

## **Robot Stuck in Corner**

GIF of robot navigating into a corner with no viable path forward.

# 

## **Recovery Behaviour: Spinning**

<img width="608" height="414" alt="Recovery behaviour Spinning" src="https://github.com/user-attachments/assets/be86b1e4-3468-4a69-abcb-c6f5cc65a326" />


## **Recovery Behaviour: Backing Up**

<img width="600" height="344" alt="Recovery behavure backing up" src="https://github.com/user-attachments/assets/407c3a3c-ceed-4d69-8c03-e7f6b26eceff" />



## **Recovery Behaviour: Waiting & Re-planning**

GIF of robot waiting (2 sec) then clearing costmap and re-planning successfully.

# 

## **Costmap Showing Inflation Zones**

GIF of RViz costmap with inflated obstacles – robot stays outside red zones.

# Dynamic obstacles

## **Dynamic Obstacle Moving in Gazebo**

GIF of the moving object (e.g., cube) crossing the robot’s planned path.

## **Robot Stopping for Obstacle**

GIF of robot detecting the moving obstacle (LIDAR shows red points) and stopping safely.

## **Costmap Clearing Mode – Obstacle Disappears**

GIF showing the costmap cell marked as occupied, then cleared after obstacle moves away.

## **Blocked Path – Robot Finds Alternative Route**

GIF of a row of unmapped objects completely blocking the direct path, and the robot navigating around them using a new plan.

## **RViz Planned Path After Blockage**

GIF of RViz showing the global planner finding a different route when the direct path is blocked.

# Fault Scenarios

## **Drift Before Fix (Misaligned Map & Scan)**

GIF of LIDAR scan misaligned with static map – robot appears to drive through walls.

## **Drift Fix: AMCL Recovery Enabled**

GIF after enabling AMCL automated recovery (recovery\_alpha\_fast=0.1) – map and scan stay aligned.

## **Wheel Slip / Skid (Before Tuning)**

GIF of robot turning but overshooting or oscillating due to slip – path tracking error.

## **Skid Fix: Velocity Smoother Tuned**

GIF after reducing max\_accel and max\_decel – smooth turning, no slip, path followed accurately.

## **Loop Closure Improvement (Before)**

GIF of map with obvious distortion before loop closure (see also 6.3).

## **Loop Closure Improvement (After)**

GIF of same area after loop closure – map corrected (see also 6.4)
