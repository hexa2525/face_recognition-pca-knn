import cv2
import os
import time
from PIL import Image

count = 1
IMAGE_SIZE = 224
cap = cv2.VideoCapture(0)
cascade_path = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_path)

def save_img(img_frame):
    home = os.environ["HOME"]    
    path = os.path.join(home, "train/s8c")
    img = Image.fromarray(img_frame)    
    img.save(f"{path}/{count}.jpg")
    print(count)

while True:
  _, frame = cap.read()

  # convert webcam into gray
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  faceRects = cascade.detectMultiScale(frame_gray, scaleFactor = 1.2, minNeighbors = 1, minSize = (32, 32))

  if len(faceRects) > 0:
    for faceRect in faceRects:
      # face position
      x, y, w, h = faceRect
      # divided the frame into mini frame only include face
      face_img = frame_gray[y - 10: y + h + 10, x - 10: x + w + 10]

      top, bottom, left, right = (0, 0, 0, 0)
      h, w = face_img.shape
      longest_edge = max(h, w)

      # if high and width doesn't equal, run this if statement
      if h < longest_edge:
          dh = longest_edge - h
          top = dh // 2
          bottom = dh - top
      elif w < longest_edge:
          dw = longest_edge - w
          left = dw // 2
          right = dw - left
      else:
          pass

      BLACK = [0]

      constant = cv2.copyMakeBorder(face_img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)
      img_test = cv2.resize(constant, (IMAGE_SIZE, IMAGE_SIZE))
      cv2.imshow("result", img_test)
      save_img(img_test)
      count+=1

  cv2.imshow("find me", frame_gray)
  cv2.waitKey(10)

