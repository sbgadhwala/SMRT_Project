# SMRT_Project


### Run_Dynamic_Robot is the file that is dynamic, and will run with camera's calibration settings. Followoing are the supporting files:

  * Aruco.py is the file that will identify Aruco markrers and use function from CameraCalibration.py file to predict the relative position
  * Camera Data.csv is the file used to train the regresison model. It contains the observations of Area and center coordinates of Aruco Tags from different points in cartesian plane
  * area.txt, center_x.txt and center_y.txt are the refernce files used to read the live (updated) values of above mentioned metrics
  * current_pos.txt is the file in which robot's predicted relative X and Y coordinates are saved (Z-coordinate remians unaffected since there is no relative change in height)

(Refer to Steps to Run Robot.odt file for step by step execution of the whole process using ROS)


### Dim2_To_Dim1 is the file that involves picking up hangers from a different conveyor (thats in a different orientation) and dopping off on the 1st conveyor
