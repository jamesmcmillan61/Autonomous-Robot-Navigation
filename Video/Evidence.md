# Autonomous Robot Navigation  
### Evidence Submission — 701028 Autonomous Robots  
**James McMillan (202202995)**

---

## Table of Contents
1. [SLAM](#slam)
2. [Localisation](#localisation)
3. [Navigation — DWA](#navigation-dwa)
4. [Navigation — A*](#navigation-a)
5. [Safety & Recovery Behaviours](#safety--recovery-behaviours)
6. [Dynamic Obstacles](#dynamic-obstacles)
7. [Fault Scenarios](#fault-scenarios)

---


# SLAM

## **Camera view while Mapping**
<img width="166" height="118" alt="Camera View During Slam" src="https://github.com/user-attachments/assets/243c8699-b249-4335-8b4e-abff49bb8f43" />


## **Map Building (RVis view)**

<img width="862" height="650" alt="image" src="https://github.com/user-attachments/assets/a980c0dd-d168-43f6-a634-cc95cc1fc9dd" />


## **Before Loop Closure Fix**

<img width="600" height="419" alt="Skidding during map generation" src="https://github.com/user-attachments/assets/886fcdd1-30c8-41f3-9462-02506ccc22b8" />

## **After Loop Closure **

<img width="977" height="615" alt="image" src="https://github.com/user-attachments/assets/1eb03c9a-0c4e-4520-9a2e-99edf285e308" />

## **Returning to a Known Location for Loop Closure**
<img width="748" height="522" alt="Loop Closure " src="https://github.com/user-attachments/assets/472845cf-12a0-4587-b255-9911dec5fd07" />





---

# Localisation

## **Initial Pose Estimation (Before Manual Pose)**

GIF showing LIDAR scan not aligned with the static map (red scan lines mismatched with walls).

## **After Manual Poseing**

GIF showing LIDAR scan correctly aligned with the map after user sets initial pose in RViz.



## **Localisation Stability During Navigation**

GIF of a long navigation run with the robot’s pose estimate remaining stable (no drift, scan stays aligned).



## **AMCL Correcting Minor Drift**

GIF where the robot starts with a small pose error and AMCL gradually corrects it back into alignment.


---

# Navigation (DWA)

## **DWA Start-to-Goal Run (Before Tuning)**

GIF of DWA navigation with default inflation radius – robot gets too close to walls.

## **DWA After Increasing Inflation Radius**

GIF of DWA with increased inflation radius – robot stays safely away from walls and reaches goal.

## **DWA Stop-Start Behaviour**

GIF showing DWA frequently pausing and re-evaluating path (characteristic behaviour).

---

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


---

# Safety / recovery behaviours

## **Robot Stuck in Corner**

GIF of robot navigating into a corner with no viable path forward.



## **Recovery Behaviour: Spinning**

<img width="608" height="414" alt="Recovery behaviour Spinning" src="https://github.com/user-attachments/assets/be86b1e4-3468-4a69-abcb-c6f5cc65a326" />


## **Recovery Behaviour: Backing Up**

<img width="600" height="344" alt="Recovery behavure backing up" src="https://github.com/user-attachments/assets/407c3a3c-ceed-4d69-8c03-e7f6b26eceff" />



## **Recovery Behaviour: Waiting & Re-planning**

GIF of robot waiting (2 sec) then clearing costmap and re-planning successfully.


## **Costmap Showing Inflation Zones**

GIF of RViz costmap with inflated obstacles – robot stays outside red zones.


---


# Dynamic obstacles

## **Dynamic Obstacle Moving in Gazebo**

<img width="530" height="362" alt="Dynamic Obsticals" src="https://github.com/user-attachments/assets/6f763c55-e5db-4d88-8486-1b4d2a1e5f1c" />

## **Robot Stopping for Obstacle**

<img width="448" height="280" alt="Robot stops for dynamic obsticle" src="https://github.com/user-attachments/assets/a8644bad-6842-4917-a38f-3f2800bac92f" />
## **Costmap Clearing Mode – Obstacle Disappears**

GIF showing the costmap cell marked as occupied, then cleared after obstacle moves away.

## **Blocked Path**

<img width="331" height="357" alt="Blocked path" src="https://github.com/user-attachments/assets/a35a99f4-44ef-4ce3-897c-15302dd8e9bb" />

## **RViz Planned Path After Blockage**

<img width="702" height="842" alt="Re evaluating path based on blocked passage " src="https://github.com/user-attachments/assets/70e23c0a-b5da-4acd-8a2d-060be0baf1a7" />

---

# Fault Scenarios

## **AMCL Fixing drift / skidding **

<img width="600" height="402" alt="AMCL fixing drift" src="https://github.com/user-attachments/assets/510b26b7-2e79-4bb3-a290-1345fbea2041" />

## **Skid Fix: Velocity Smoother Tuned**

GIF after reducing max\_accel and max\_decel – smooth turning, no slip, path followed accurately.

## **Loop Closure Improvement (Before)**

GIF of map with obvious distortion before loop closure (see also 6.3).

## **Loop Closure Improvement (After)**

GIF of same area after loop closure – map corrected (see also 6.4)
