import cv2

img = cv2.imread('dreamshaper.jpg')

# pxl = img[727,150]
# print("Pixel value at 100,150 are",pxl)

# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.imshow('Image',img)
# cv2.waitKey(0)

# cv2.imshow('Image 1',gray_img)
# cv2.waitKey(0)


# img1 = img
# for i in range(720):
#     for j in range(720):
#         img1[i,j] = [255,255,255]-img[i,j]

# cv2.imshow('Image 2',img1)
# cv2.waitKey(0)

# rimg = cv2.resize(gray_img,(100,100))
# cv2.imshow('Image 3',rimg)
# cv2.waitKey(0)

# line_img = cv2.line(img,
#                     (0,0),(300,300),
#                     (0,255,0),3)
# cv2.imshow('Image 4',line_img)
# cv2.waitKey(0)


# rect_img = cv2.rectangle(img,
#                     (100,100),(200,200),
#                     (0,0,0))
# cv2.imshow('Image 4',rect_img)
# cv2.waitKey(0)

# cir_img = cv2.circle(img,
#                     (100,320),50,
#                     (0,0,255),-1)
# cv2.imshow('Image 4',cir_img)

blur_img = cv2.GaussianBlur(img,(99,29),0)
cv2.imshow('Image 4',blur_img)

cv2.waitKey(0)
cv2.destroyAllWindows()