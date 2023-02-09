from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
import cv2
import numpy as np
from PIL import Image
from data import LoadData
import pickle as pk


def knn(neighbor, traindata, trainlabel, testdata):
    neigh = KNeighborsClassifier(n_neighbors=neighbor)
    neigh.fit(traindata, trainlabel)
    return neigh.predict(testdata)

cascade_path = "haarcascade_frontalface_alt.xml"
IMAGE_SIZE = 224
color = (0, 255, 0)
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(cascade_path)

users = [
    "",
    "ye zar ni ko",
    "thet nyein chan lwin",
    "aung htet oo"
]


Data, Label = LoadData()
Data = np.asarray(Data)
Label = np.asarray(Label)

with open("pca.pkl", "rb") as pca_file:
    pca = pk.load(pca_file)

with open("trainDataS.pkl", "rb") as trainDataS_file:
    trainDataS = pk.load(trainDataS_file)

while True:
  _, frame = cap.read()

  # convert webcam into gray
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  faceRects = cascade.detectMultiScale(frame_gray, scaleFactor = 1.2, minNeighbors = 1, minSize = (50, 50))
  """
  Face Reacts
  [[229 144 193 193]]
  [[224 142 197 197]]
  [[223 141 196 196]]
  [[224 142 192 192]]
  [[222 141 198 198]]
  [[225 143 194 194]]
  [[223 141 196 196]]
  [[225 142 194 194]]
  ....
  """
  if len(faceRects) > 0:
    for faceRect in faceRects:
      # face position
      x, y, w, h = faceRect
      # divided the frame into mini frame only include face
      face_img = frame_gray[y - 10: y + h + 10, x - 10: x + w + 10]
      cv2.imshow("img", face_img)

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
      img_test = np.reshape(img_test, (1, IMAGE_SIZE * IMAGE_SIZE))
      testDataS = pca.transform(img_test)
      
      result = knn(5, trainDataS, np.asarray(Label), testDataS)  # 使用KNN进行分类，5为最近邻居数
      faceID = result[0]
      print(users[faceID])



  cv2.imshow("find me", frame)
  cv2.waitKey(10)