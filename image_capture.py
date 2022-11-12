import cv2 

vid=cv2.VideoCapture(0)

while True:
    ret, image=vid.read()
    cv2.imshow('image', image)
    
