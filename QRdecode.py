from pyzbar.pyzbar import decode
from PIL import Image
from os.path import expanduser
import os

def QRreade(image):
  # image変数の指し示す画像からQRコードの検出をする
  readResult = decode(Image.open(image))
  if (readResult != []):
    return readResult
  else:
    print('QRコードを検出できませんでした')
    exit()

def SearchImage():
  # WebCameraで撮った最新の画像を探す
  homeDir = expanduser('~')
  imageDir = homeDir + '\\Pictures\\Camera Roll'
  imageList = os.listdir(imageDir)
  return (imageDir + '\\' + imageList[-1])

image = SearchImage()
qrResult = QRreade(image)
print('Scanned Image: {0}' .format(image))
print('Scan Rssult: {0}' .format(qrResult))

with open('QRresult', 'w') as exportFile:
  exportFile.write(qrResult[0][0].decode('utf-8', 'ignore'))
