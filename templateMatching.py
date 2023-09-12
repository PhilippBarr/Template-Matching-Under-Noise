import cv2
import numpy as np

_count = 0
def writeImg(image, PATH, stradd=""):
    global _count
    _count += 1
    cv2.imwrite(PATH + '{:04d}'.format(_count) + stradd + '.jpg', image)


# Adding noise on a image
def noise(image, prob):
    row, col, ch = image.shape
    rand1 = prob * np.random.rand(row, col, ch)
    rand2 = prob * np.random.rand(row, col, ch)
    output = (image + (rand1 * image - rand2 * image)).astype('int')
    return output.astype('uint8')


# Load the image to check
img_rgb = cv2.imread('images/diamond1.1.jpg')

# Adding some noise (0.05 = 5% noise)
imnoise=0.05
img_noise_rgb = noise(img_rgb, imnoise)

blur = img_noise_rgb

# To add Gaussian Noise, use the command below.
# blur = cv2.GaussianBlur(img_noise_rgb, (5, 5), 0)

# Gray Image
img_gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)   # img_noise_rgb | blur

# load the template image we look for
template = cv2.imread('images/diamond2.1.jpg', 0)
w, h = template.shape[::-1]
tem_hist = cv2.calcHist([img_rgb], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

# run the template matching
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.46
loc = np.where(res >= threshold)

# mark the corresponding location(s)
for pt in zip(*loc[::-1]):
    cv2.rectangle(blur, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)  # img_noise_rgb | blur

cv2.namedWindow("Detected", cv2.WINDOW_NORMAL)
cv2.imshow('Detected', blur)    # img_noise_rgb | blur
writeImg(blur, './imageResults/', str(imnoise))
cv2.resizeWindow('Detected', 800, 600)

cv2.waitKey()
cv2.destroyAllWindows()
