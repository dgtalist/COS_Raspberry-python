import face_recognition
import cv2
import numpy as np

imgShin = face_recognition.load_image_file('img/shinmina.jpg')
imgShin = cv2.cvtColor(imgShin,cv2.COLOR_BGR2RGB)


imgTest = face_recognition.load_image_file('img/test1.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgShin)[0]
encodeShin = face_recognition.face_encodings(imgShin)[0]
# print(faceLoc)

cv2.rectangle(imgShin,(faceLoc[3],faceLoc[0]),
(faceLoc[1],faceLoc[2]),(255,0,255),2)
 
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),
(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeShin], encodeTest)
faceDis = face_recognition.face_distance([encodeShin], encodeTest)


cv2.putText(imgTest,f'{results} {round(faceDis[0],2)} ',
(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),3)


cv2.imshow('Shinmina', imgShin)
cv2.imshow('Shinmina_test', imgTest)
cv2.waitKey(0)
