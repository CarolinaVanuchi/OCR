import cv2
import pytesseract
from src import treatment
from src import latex
from src import utils

#image = cv2.imread('src/image/exemple.png')
#image = cv2.imread('src/image/exemple1.jpeg')
image = cv2.imread('src/image/exemple2.png')

window_name = 'image'
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = treatment.Treatment.put_gray(image) #escala de cinza
#thresh = treatment.Treatment.thresholding(gray) #aplicar limiarização, determinar uma densidade de cinza
#opening = treatment.Treatment.opening(gray) #aplicar uma dilatação
canny = treatment.Treatment.canny(gray) #dilatar

window_canny = 'canny'
cv2.imshow(window_canny, canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(canny, config=custom_config)

remove_color = utils.Utils.remove_color(image)
remove_color = utils.Utils.resize(remove_color, 240, 140)

window_mark = 'Just image'
cv2.imshow(window_mark, remove_color)
cv2.waitKey(0) 
cv2.destroyAllWindows()

cv2.imwrite('output/image/image.png', remove_color)

file = open('output/export.tex', 'w')
file.write(latex.Latex.header())
file.write(latex.Latex.content(text))
file.write(latex.Latex.add_image('Exemplo', 'image/image.png', 'Proprios Alunos', 'Exemplo projeto OCR'))
file.write(latex.Latex.footer())
