from styx_msgs.msg import TrafficLight
import rospy
import cv2
from std_msgs.msg import String
# import tensorflow

RED_PIXELS_THRESHOLD = 50

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        self.chatter_classifier = rospy.Publisher('/chatter_classifier', String, queue_size=1)
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        # self.chatter_classifier.publish(str(max(image.data[0])) + "  " + str(max(image.data[1])) + "  " + str(max(image.data[2])))
        b, g, r = cv2.split(image)
        height, width, ch = image.shape

        # self.chatter_classifier.publish(str(b))
        # self.chatter_classifier.publish(str(height) + "  " + str(width) + "  " + str(ch) + " " + str(sum(sum(r==r.max()))) + str(light.state))
        # TODO implement light color prediction
        # return TrafficLight.UNKNOWN
        traffic_light = TrafficLight.UNKNOWN
        if sum(sum(r == 255)) > RED_PIXELS_THRESHOLD: # number of red pixels greater than some threshold
            traffic_light = TrafficLight.RED
        else:
            traffic_light = TrafficLight.GREEN
        self.chatter_classifier.publish(str(traffic_light))
        return traffic_light
        # return light.state    # for testing
