import cv2
import numpy as np

# Open the camera (usually camera index 0 is the built-in camera)
cap = cv2.VideoCapture(0)

print(f"widtht : {cap.get(3)}")
print(f"height : {cap.get(4)}")

WIDTH = int(cap.get(3))

# Initial lower and upper bounds for the target color in HSV
lower_bound = np.array([0, 150, 150])
upper_bound = np.array([10, 255, 255])

while True:
    # Read a frame from the camera
    ret, frame = cap.read()


    # Convert the frame from BGR to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the target color
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around the detected objects
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if (w*h) >= 500:
        	# this section is for bbox and printing direction to move.
        	x0 = x + (w/2)
        	#y0 = y + (h/2)
        	if x0 > ( (WIDTH/2) + 50 ):
        		print("move to the left")
        	elif x0 < ( (WIDTH/2) - 50 ):
        		print("move to the right")
        	else:
        		print("centered.") 
        	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with bounding boxes
    cv2.imshow('Color Object Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
