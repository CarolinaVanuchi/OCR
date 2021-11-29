import cv2
import pytesseract
from src import treatment
from src import latex

#image = cv2.imread('src/image/exemple.png')
#image = cv2.imread('src/image/exemple1.jpeg')
#image = cv2.imread('src/image/exemple2.jpeg')
#image = cv2.imread('src/image/exemple3.jpg')
image = cv2.imread('src/image/exemple4.png')

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


file = open('export.tex', 'w')
file.write(latex.Latex.header())
file.write(latex.Latex.content(text))
file.write(latex.Latex.footer())
 