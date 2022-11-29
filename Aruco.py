import cv2
from cv2 import aruco
import numpy as np

def getCenterFromAruco():
    cen = np.array([0 ,0])
    area = 0

    marker_dict = aruco.Dictionary_get(aruco.DICT_5X5_1000)

    param_markers = aruco.DetectorParameters_create()

    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)


    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        marker_corners, marker_IDs, reject = aruco.detectMarkers(
            gray_frame, marker_dict, parameters=param_markers
        )
        if marker_corners:
            for ids, corners in zip(marker_IDs, marker_corners):
                cv2.polylines(
                    frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv2.LINE_AA
                )
                corners = corners.reshape(4, 2)
                corners = corners.astype(int)
                top_right = corners[0].ravel()
                top_left = corners[1].ravel()
                bottom_right = corners[2].ravel()
                bottom_left = corners[3].ravel()
                center = bottom_left
                center[0] = (top_left[0] + bottom_right[0])/2
                center[1] = (top_left[1] + bottom_right[1])/2
                cv2.putText(
                    frame,
                    f"id: {ids[0]}",
                    top_right,
                    cv2.FONT_HERSHEY_PLAIN,
                    1.3,
                    (200, 100, 0),
                    2,
                    cv2.LINE_AA,
                )

                if str(ids[0]) == "300":
                        cen = center
                        area = (int(bottom_right[1]) - int(bottom_left[1]))**2
                
                with open(r"/home/ise.ros/Shyam/center.txt",'r+') as file:
                    file.truncate(0)
                
                file1 = open(r"/home/ise.ros/Shyam/center.txt", "a")
                file1.write(str(cen[0]))
                file1.close()

                with open(r"/home/ise.ros/Shyam/area.txt",'r+') as file:
                    file.truncate(0)
                
                file1 = open(r"/home/ise.ros/Shyam/area.txt", "a")
                file1.write(str(area))
                file1.close()
                #return
                
                cv2.putText(
                    frame,
                    f"Center: {center}",
                    center,
                    cv2.FONT_HERSHEY_PLAIN,
                    1.3,
                    (200, 100, 0),
                    2,
                    cv2.LINE_AA,
                )
                cv2.putText(
                    frame,
                    f"Area: {(int(bottom_right[1]) - int(bottom_left[1]))**2}",
                    bottom_right,
                    cv2.FONT_HERSHEY_PLAIN,
                    1.3,
                    (200, 100, 0),
                    2,
                    cv2.LINE_AA,
                )
                #print("Top Left: ", top_right)
                #print("Top Right: ", top_left)
                #print("Bottom Left: ", bottom_left)
                #print("Bottom Right: ", bottom_right)
                #print("Center Point: ", ((top_left[0] + bottom_right[0])/2 , (top_left[1] + bottom_right[1])/2))
                if ids == 3:
                    print(ids, "  ", corners)
        
        blur = cv2.GaussianBlur(gray_frame,(5,5),0)
        ret, thresh_img = cv2.threshold(blur,91,255,cv2.THRESH_BINARY)
        contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
        for c in contours :
        #cv2.drawContours(frame, [c], -1, (0,255,0), 3)
            if cv2.contourArea(c) > 1500 and cv2.contourArea(c) < 1600:
                approx = cv2.approxPolyDP(c, 0.009 * cv2.arcLength(c, True), True)
                cv2.drawContours(frame, [approx], 0, (0, 0, 255), 5) 
                #cv2.drawContours(frame, [c], -1, (0,255,0), 3)
                n = approx.ravel() 
                i = 0
    
                for j in n :
                    if(i % 2 == 0):
                        x = n[i]
                        y = n[i + 1]
    
                        # String containing the co-ordinates.
                        string = str(x) + " " + str(y) 
    
                        if(i == 0):
                        # text on topmost co-ordinate.
                            cv2.putText(frame, "Arrow tip", (x, y),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
                        else:
                            # text on remaining co-ordinates.
                            cv2.putText(frame, string, (x, y), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))

                    i = i + 1
                #cv2.line(frame, (arucoCenter[0], arucoCenter[1]), (x, y), (255,0,0), 4)

        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    return


if __name__ == "__main__":
    getCenterFromAruco()