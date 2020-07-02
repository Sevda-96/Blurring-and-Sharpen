
import cv2
import numpy as np

# goruntuyu gray uygulayarak acar

img1 = cv2.imread('prosthesis.bmp', 0)

# keskinlestirme
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharping = cv2.filter2D(img1, -1, kernel)
# goruntuyu projeye kaydetmek icin gerekli fonksiyon
cv2.imwrite('soru2-sonuc(Keskinlestirme).jpg', sharping)

# bulanıklastırma
blurred_1 = cv2.blur(img1, (5, 5))
# goruntuyu projeye kaydetmek icin gerekli fonksiyon
cv2.imwrite('soru2-sonuc(Bulaniklastirma).jpg', blurred_1)

# goruntuyu projeyi ekranda gostermsi icin gerekli fonksiyon
cv2.imshow("orjinal", img1)
cv2.imshow("Keskinlestirme ", sharping)
cv2.imshow("Bulaniklastirma ", blurred_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
