import cv2

class Utils:

    def remove_color(image):
        lower = (0, 0, 0)
        upper = (0, 0, 0) 
        img_rgb_inrange = cv2.inRange(image, lower, upper)
        neg_rgb_image = ~img_rgb_inrange
        return neg_rgb_image
       
    def resize(image, x, y):
        return cv2.resize(image, dsize=(x, y), interpolation=cv2.INTER_CUBIC)