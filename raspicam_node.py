if __name__==__main__":

    #--- Define HSV limits
    blue_min = (77,40,0)
    blue_max = (101, 255, 255) 
    
    #--- Define area limit [x_min, y_min, x_max, y_max] adimensional (0.0 to 1.0) starting from top left corner
    window = [0.25, 0.25, 0.65, 0.75]
    
    #-- IMAGE_SOURCE: either 'camera' or 'imagelist'
    SOURCE = 'camera'
    
    if SOURCE == 'camera':
        cap = cv2.VideoCapture(0)
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            #--- Detect keypoints
            keypoints, _ = blob_detect(frame, blue_min, blue_max, blur=3, 
                                        blob_params=None, search_window=window, imshow=False)
            #--- Draw search window
            frame = draw_window(frame, window, imshow=False)
            #--- Draw keypoints
            frame = draw_keypoints(frame, keypoints, imshow=False)
            #--- Show frame
            cv2.imshow("Frame", frame)
            #--- Break loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
    else:
        #-- Read image list from file:
        image_list = []
        image_list.append(cv2.imread("blob.jpg"))
        #image_list.append(cv2.imread("blob2.jpg"))
        #image_list.append(cv2.imread("blob3.jpg"))

        for image in image_list:
            #--- Detect keypoints
            keypoints, _ = blob_detect(image, blue_min, blue_max, blur=5, 
                                        blob_params=None, search_window=window, imshow=False)
            #--- Draw search window
            image = draw_window(image, window, imshow=False)
            #--- Draw keypoints
            image = draw_keypoints(image, keypoints, imshow=False)
            #--- Show image
            cv2.imshow("Frame", image)
            #--- Wait for a key press and close the window
            cv2.waitKey(0)
            cv2.destroyAllWindows()
