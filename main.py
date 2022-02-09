import sys
import cv2
import numpy as np
from src import corners
from src import pdf

def main():

    # preprocessing
    # image = cv2.imread("image/whiteboard.png", cv2.IMREAD_COLOR)
    image = cv2.imread("image/whiteboard2.png", cv2.IMREAD_COLOR)
    # image = cv2.imread("image/whiteboard3.jpeg", cv2.IMREAD_COLOR)
  
    threshold = 0.75
    offset = 15
    if len(sys.argv) >= 2:
        threshold = float(sys.argv[1])
        offset = int(sys.argv[2])

    image = corners.process(image, offset, threshold)
    
    # cv2.imshow("image", image)
    # cv2.waitKey(0)

    cv2.imwrite('output/5_image.png', image)
    pdf.to_pdf('output/images', 297, 210, 'output/output.pdf')
   
# guard
if __name__ == "__main__":
    main()