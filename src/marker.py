import cv2
import numpy as np

class Marker:

    def recognize(image):

        contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        i = 0
        for contour in contours:

            if i == 0:
                i = 1
                continue

            approx = cv2.approxPolyDP( contour, 0.01 * cv2.arcLength(contour, True), True)
            
            cv2.drawContours(image, [contour], 0, (20, 20, 20), 1)

            M = cv2.moments(contour)
            if M['m00'] != 0.0:
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])

            if len(approx) == 4:
                cv2.putText(image, 'Retangulo', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (20, 20, 20), 2)

        return image
