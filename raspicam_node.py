import cv2
import numpy as np

def blob_detect(image, hsv_min, hsv_max, blur=0, blob_params=None, search_window=None, imshow=False):
    # Your existing code for blob detection
    if blur > 0:
        image = cv2.blur(image, (blur, blur))

    # ... (other parts of your blob detection code)

    return keypoints, reversemask

if __name__ == "__main__":
    # Define HSV limits
    blue_min = (77, 40, 0)
    blue_max = (101, 255, 255)
    
    # Define area limit [x_min, y_min, x_max, y_max] adimensional (0.0 to 1.0) starting from top left corner
    window = [0.25, 0.25, 0.65, 0.75]

    # Open camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Detect keypoints
        keypoints, _ = blob_detect(frame, blue_min, blue_max, blur=3, blob_params=None, search_window=window, imshow=False)

        # Draw search window
        frame = draw_window(frame, window)

        # Draw keypoints
        frame = draw_keypoints(frame, keypoints, imshow=True)

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()
