#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

def image_callback(msg):
    try:
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
        # Process the image as needed
    except CvBridgeError as e:
        rospy.logerr("CvBridgeError: %s", e)

def main():
    rospy.init_node('usb_camera_node', anonymous=True)
    image_topic = "usb_camera/image"
    rospy.Subscriber(image_topic, Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
