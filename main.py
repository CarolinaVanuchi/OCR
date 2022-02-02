import cv2
import numpy as np
from src import corners

def main():

    # preprocessing
    image = cv2.imread("image/whiteboard2.png", cv2.IMREAD_UNCHANGED)
    image = corners.process(image, 11, 0.6)

    cv2.imshow("image", image)
    cv2.waitKey(0)

    cv2.imwrite('output/image.png', image)

# guard
if __name__ == "__main__":
    main()