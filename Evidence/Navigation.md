# Autonomous Robot Navigation  
### Evidence — 701028 Autonomous Robots  
**James McMillan (202202995)**

---

## Table of Contents
1. [SLAM](#slam)
2. [Navigation — DWA](#navigation-dwa)
3. [Navigation — A*](#navigation-a)
4. [Safety & Recovery Behaviours](#safety--recovery-behaviours)
5. [Dynamic Obstacles](#dynamic-obstacles)
6. [Fault Scenarios](#fault-scenarios)

---
# SLAM

### Camera View During Mapping
<p align="center">
  <img src="https://github.com/user-attachments/assets/243c8699-b249-4335-8b4e-abff49bb8f43" width="300" style="border-radius: 16px;"
/>
</p>

### Map Building in RViz
<p align="center">
  <img src="https://github.com/user-attachments/assets/a980c0dd-d168-43f6-a634-cc95cc1fc9dd" width="600" style="border-radius: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.15);"
/>
</p>

### Loop Closure — Before Correction
<p align="center">
  <img src="https://github.com/user-attachments/assets/886fcdd1-30c8-41f3-9462-02506ccc22b8" width="600" />
</p>

### Loop Closure — After Correction
<p align="center">
  <img src="https://github.com/user-attachments/assets/1eb03c9a-0c4e-4520-9a2e-99edf285e308" width="600" />
</p>

### Returning to a Known Location (Loop Closure Trigger)
<p align="center">
  <img src="https://github.com/user-attachments/assets/472845cf-12a0-4587-b255-9911dec5fd07" width="600" />
</p>

---
# Navigation (DWA)

### DWA Visualisation in RViz
<p align="center">
  <img src="https://github.com/user-attachments/assets/97032f51-7532-48ea-a3eb-4e49468d4ecb" width="600" />
</p>

### DWA Start-to-Goal Run (Before Tuning)
<p align="center">
Can be found at - [Evidence/Navigation/NavWithDWA (1).mp4](Evidence/Navigation/NavWithDWA (1).mp4)

</p>

---

# Navigation (A*)

### A* Getting Stuck (Before Parameter Tuning)
<p align="center">
  <img src="https://github.com/user-attachments/assets/33a1345a-245c-430c-9fd5-35145a92e283" width="600" />
</p>

### A* Successful Navigation
<p align="center">
  <img src="https://github.com/user-attachments/assets/03b46421-0831-40af-8f0b-9fc1189fbe75" width="600" />
</p>

[**Full video available here**](https://github.com/jamesmcmillan61/Autonomous-Robot-Navigation/blob/main/Video/Navigation/AStar/AStar%20Navigation.mp4)

---
# Safety & Recovery Behaviours

### Recovery: Spinning
<p align="center">
  <img src="https://github.com/user-attachments/assets/be86b1e4-3468-4a69-abcb-c6f5cc65a326" width="600" />
</p>

### Recovery: Backing Up
<p align="center">
  <img src="https://github.com/user-attachments/assets/407c3a3c-ceed-4d69-8c03-e7f6b26eceff" width="600" />
</p>

### Recovery: Waiting & Re-planning
<p align="center">
  <img src="GIF_URL_HERE" width="600" />
</p>

## Costmaps

| Local Costmap | Global Costmap |
|--------------|----------------|
| <p align="center"><img src="https://github.com/user-attachments/assets/2d255db7-e6e9-44db-a887-d00d2ced3056" width="400" /></p> | <p align="center"><img src="https://github.com/user-attachments/assets/6376c2e3-a95d-4e26-8678-d596643192e9" width="400" /></p> |

---

# Dynamic Obstacles

### Dynamic Obstacle in Gazebo
<p align="center">
  <img src="https://github.com/user-attachments/assets/6f763c55-e5db-4d88-8486-1b4d2a1e5f1c" width="600" />
</p>

### Robot Stopping for Obstacle
<p align="center">
  <img src="https://github.com/user-attachments/assets/a8644bad-6842-4917-a38f-3f2800bac92f" width="600" />
</p>

### Costmap Clearing Mode
<p align="center">
  <img src="https://github.com/user-attachments/assets/ddfac08a-83b5-4b90-abec-5a1dfca589eb" width="600" />
</p>

### Blocked Path
<p align="center">
  <img src="https://github.com/user-attachments/assets/a35a99f4-44ef-4ce3-897c-15302dd8e9bb" width="600" />
</p>

### RViz Re-planned Path
<p align="center">
  <img src="https://github.com/user-attachments/assets/70e23c0a-b5da-4acd-8a2d-060be0baf1a7" width="600" />
</p>

---

# Fault Scenarios

### AMCL Fixing Drift / Skidding
[Link to video](/Video/AMCL%20Correcting%20drift.mp4)
<p align="center">
  <img src="https://github.com/user-attachments/assets/510b26b7-2e79-4bb3-a290-1345fbea2041" width="600" />
</p>

