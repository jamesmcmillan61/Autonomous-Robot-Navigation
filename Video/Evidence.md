# Autonomous Robot Navigation  
### Evidence Submission — 701028 Autonomous Robots  
**James McMillan (202202995)**

---

## Table of Contents
1. [SLAM](#slam)
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

# Navigation (DWA)
<img width="716" height="860" alt="NavWithDWA_XS" src="https://github.com/user-attachments/assets/97032f51-7532-48ea-a3eb-4e49468d4ecb" />

## **DWA Start-to-Goal Run (Before Tuning)**

## **DWA Stop-Start Behaviour**

GIF showing DWA frequently pausing and re-evaluating path (characteristic behaviour).


---

# Navigation (A\*)

## **A\* Getting Stuck (Before Parameter Tuning)**

<img width="920" height="464" alt="Robot getting stuck in doorway" src="https://github.com/user-attachments/assets/33a1345a-245c-430c-9fd5-35145a92e283" />

## **A\* Successful Navigation **

<img width="600" height="600" alt="Sucsessfull Navigation with A* path planning" src="https://github.com/user-attachments/assets/03b46421-0831-40af-8f0b-9fc1189fbe75" />

[Full video here](https://github.com/jamesmcmillan61/Autonomous-Robot-Navigation/blob/main/Video/Navigation/AStar/AStar%20Navigation.mp4)

---

# Safety / recovery behaviours

## **Recovery Behaviour: Spinning**

<img width="608" height="414" alt="Recovery behaviour Spinning" src="https://github.com/user-attachments/assets/be86b1e4-3468-4a69-abcb-c6f5cc65a326" />


## **Recovery Behaviour: Backing Up**

<img width="600" height="344" alt="Recovery behavure backing up" src="https://github.com/user-attachments/assets/407c3a3c-ceed-4d69-8c03-e7f6b26eceff" />

## **Recovery Behaviour: Waiting & Re-planning**

GIF of robot waiting (2 sec) then clearing costmap and re-planning successfully.


## **Costmaps **

### Local cost map 
<img width="441" height="541" alt="image" src="https://github.com/user-attachments/assets/2d255db7-e6e9-44db-a887-d00d2ced3056" />

### Global costmap 
<img width="438" height="537" alt="image" src="https://github.com/user-attachments/assets/6376c2e3-a95d-4e26-8678-d596643192e9" />

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

