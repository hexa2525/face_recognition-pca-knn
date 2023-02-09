import cv2

img = cv2.imread("2.jpg",0)
cascade_path = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_path)
faceRects = cascade.detectMultiScale(img, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))


for (x, y, w, h) in faceRects:
   pad_w, pad_h = int(0.15 * w), int(0.01 * h)
   cv2.rectangle(img, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)
while True:
   cv2.imshow('image',img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()