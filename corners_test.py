# https://youtu.be/vIrmMAib7Go
# https://youtu.be/vXqKniVe6P8

import cv2
import numpy as np
from src import corners

def main():

    # preprocessing
    image = cv2.imread("image/whiteboard.png", cv2.IMREAD_UNCHANGED)

    image = corners.process(image, 11, 0.6)

    cv2.imshow("image", image)
    cv2.waitKey(0)
   
    # cv2.imshow("image", morph)
    # cv2.waitKey(0)
    # cv2.imshow("image", hsv)
    # cv2.waitKey(0)
    # cv2.imshow("image", mask)
    # cv2.waitKey(0)
    # cv2.imshow("image", match)
    # cv2.waitKey(0)
    # cv2.imshow("image", image)
    # cv2.waitKey(0)


# guard
if __name__ == "__main__":
    main()