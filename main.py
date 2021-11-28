import cv2
import pytesseract
from src import treatment

image = cv2.imread('src/image/exemple.png')


window_name = 'image'
cv2.imshow(window_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()

gray = treatment.Treatment.put_gray(image)
thresh = treatment.Treatment.thresholding(gray)
opening = treatment.Treatment.opening(gray)
canny = treatment.Treatment.canny(gray)


window_name2 = 'canny'
cv2.imshow(window_name2, canny)

cv2.waitKey(0)
cv2.destroyAllWindows()


custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(canny, config=custom_config)
print(text)

cv2.waitKey(0)
cv2.destroyAllWindows()