
## AMCL correcting drift and skidding
During navigation the robot experienced drift and skidding, which caused its estimated pose to become inaccurate. As the error grew, AMCL detected the inconsistency between the robot’s predicted position and the sensor observations. AMCL then performed a pose correction, snapping the robot back to the correct location and orientation, as shown below. This demonstrates AMCL’s role in maintaining a stable and accurate pose estimate even when wheel slip or odometry drift occurs.

<img width="600" height="402" alt="AMCL fixing drift" src="https://github.com/user-attachments/assets/510b26b7-2e79-4bb3-a290-1345fbea2041" />

[Link to video](/AMCL_Correcting_drft.mp4)
