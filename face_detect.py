import cv2

def getDataFromCamera(func):

  IMAGE_SIZE = 224
  color = (0, 255, 0)

  # capture
  cap = cv2.VideoCapture(0)

  cascade_path = "haarcascade_frontalface_alt.xml"
  cascade = cv2.CascadeClassifier(cascade_path)

  while True:
    _, frame = cap.read()

    # convert frame into gray
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detected faces
    # numbers of faces
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
    # if faces found
    if len(faceRects) > 0:
      for faceRect in faceRects:
        # face position
        x, y, w, h = faceRect
        # divided the frame into mini frame only include face
        face_img = frame_gray[y - 10: y + h + 10, x - 10: x + w + 10]

        top, bottom, left, right = adjustImageSize(face_img)
        BLACK = [0]
        constant = cv2.copyMakeBorder(face_img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)

        img_test = cv2.resize(constant, (IMAGE_SIZE, IMAGE_SIZE))

        func(img_test, frame, faceRect, cap)
    else:
      pass
    
    cv2.imshow("find me", frame)
    k = cv2.waitKey(10)

    if k & 0xFF == ord('q'):
        break

  cap.release()
  cv2.destroyAllWindows()


def adjustImageSize(face_img):
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
  
  return top, bottom, left, right