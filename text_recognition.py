import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np

img_path="sign.png"
reader=easyocr.Reader(["en"], gpu= False)     # used the ocr library to identify the text in img. language used is "en= English"
results=reader.readtext(img_path)
results

top_left = tuple(result[0][0][0])     # place the image on x and y axis so that to identify the co-ordinates of the text in it
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread(img_path)
spacer = 100
for detection in result:   # here, we have identified the text and in order to show it we will draw a rectangle highlighting it
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
    img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
    spacer+=15
    
plt.imshow(img)
plt.show()

engine = pyttsx3.init()

# Define a function to recognize text and convert it to speech
def recognize_text(image):
  # Use EasyOCR to recognize the text in the image
  results = reader.readtext(img_path)

  # Extract the text from the results and use pyttsx3 to convert it to speech
  text = ' '.join([result[1] for result in results])
  engine.say(text)
  engine.runAndWait()
  # Load an image and recognize the text in it
recognize_text(img_path)
