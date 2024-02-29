# import cv2

# image = cv2.imread(
#     "/Users/abhays/Desktop/python projects/rando-projs/mahati.jpg")

# # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # inverted_image = 255 - gray_image

# # blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
# # inverted_blurred = 255 - blurred

# # pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# # cv2.imshow("Original Image", image)
# # cv2.imshow("Pencil sketch", pencil_sketch)
# # cv2.waitKey(0)

# src = cv2.pencilSketch(
#     "/Users/abhays/Desktop/python projects/rando-projs/mahati.jpg")

# dst_gray, dst_color = cv2.pencilSketch(
#     src, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
# cv2.imshow("Original Image", image)
# cv2.imshow("Pencil Sketch", )

# cv2.waitKey(0)

import cv2

# Read image

im = cv2.imread("/Users/abhays/Desktop/python projects/rando-projs/ladi.png")

# Edge preserving filter with two different flags.
imout = cv2.edgePreservingFilter(im, flags=cv2.RECURS_FILTER)
cv2.imwrite("edge-preserving-recursive-filter.jpg", imout)

imout = cv2.edgePreservingFilter(im, flags=cv2.NORMCONV_FILTER)
cv2.imwrite("edge-preserving-normalized-convolution-filter.jpg", imout)

# Detail enhance filter
imout = cv2.detailEnhance(im)
cv2.imwrite("detail-enhance.jpg", imout)

# Pencil sketch filter
imout_gray, imout = cv2.pencilSketch(
    im, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
cv2.imwrite("pencil-sketch.jpg", imout_gray)
cv2.imwrite("pencil-sketch-color.jpg", imout)

# Stylization filter
cv2.stylization(im, imout)
cv2.imwrite("stylization.jpg", imout)
