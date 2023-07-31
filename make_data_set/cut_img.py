import os
import sys
import cv2
from datetime import datetime, timedelta
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class ImageSaver(Node):

    def __init__(self):
        super().__init__('image_saver')
        self.subscription = self.create_subscription(
            Image,
            '/video3',
            self.callback,
            10)
        self.subscription  # prevent unused variable warning

        self.bridge = CvBridge()

        # Set the time interval to save the image (in seconds)
        self.save_interval = 0.3

        # Set the path to save the images
        self.save_path = 'saved_images/'

        # Create the directory if it doesn't exist
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        # Initialize the file counter
        self.file_counter = 0

        self.last_saved_time = datetime.now()

    def callback(self, msg):
        # Check if the time interval has elapsed
        elapsed_time = datetime.now() - self.last_saved_time
        if elapsed_time < timedelta(seconds=self.save_interval):
            return

        # Convert the ROS message to OpenCV image
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Format the save filename with current time
        self.file_counter += 1
        filename = os.path.join(
            self.save_path, f'deli{self.file_counter:04d}.jpg')

        # Save the image
        cv2.imwrite(filename, cv_image)

        # Update the last saved time
        self.last_saved_time = datetime.now()


def main(args=None):
    rclpy.init(args=args)

    image_saver = ImageSaver()

    rclpy.spin(image_saver)

    # Clean up
    image_saver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
