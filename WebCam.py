import cv2
import pyzbar.pyzbar as pyzbar
import PIL.Image
from os.path import expanduser
import os

window_name = "main"
cap = cv2.VideoCapture(0)
# Width, Height FPS
cap.set(3, 1280)
cap.set(4, 720)
cap.set(5, 15)
cv2.namedWindow(window_name)

while True:
  # Get flame
  ret, flame = cap.read()
  flame = cv2.cvtColor(flame, cv2.COLOR_BGR2GRAY)

  # Show flame
  cv2.imshow(window_name, flame)

  # Binarization
  tresh = 100
  max_pixel = 255
  ret, flame = cv2.threshold(flame, tresh, max_pixel, cv2.THRESH_BINARY)

  # Scan flame
  qr_result = pyzbar.decode(flame)
  if qr_result != []:
    print(qr_result[0][0])
    with open('QRresult', 'w') as exportFile:
      exportFile.write(qr_result[0][0].decode('utf-8', 'ignore'))
    exit()

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cv2.release()
cv2.destroyAllWindows()
