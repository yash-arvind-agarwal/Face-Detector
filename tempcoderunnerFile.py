import cv2
import numpy as np

    #def nothing(x):
    #    pass

cap = cv2.VideoCapture(0) #open cameraand captures our video

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # haarcascadeis classifier which detects the facial points

    #cv2.namedWindow("Frame")
    #cv2.createTrackbar("Neighbours", "Frame", 5, 20, nothing)

count=0 #to tell no of persons
while True:
        _, frame = cap.read() #
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #converts blue green colour to grey

        #neighbours = cv2.getTrackbarPos("Neighbours", "Frame")

        faces = face_cascade.detectMultiScale(gray, 1.3, 2) # to detect the multiple persons
        if faces is():  #is is a func is used, if face is null it prints no facefound
            print("face not found !")
        else:
            count+=1 #for multiple faces
            for (x,y,h,w) in faces: #length , height, width in faces will be calculated automatially
                cf=frame[y:y+h,x:x+w]
                #(x, y, w, h) = rect
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) #in video capturing it creates a rectangle joining the facial points
                face =cv2.resize(cf,(600,600))
                face =cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                file_name_path='/Volumes/E/python_opencv/faces/'+str(count)+'.jpg' #it saves the images wherein test we can see a limit upto 500
                cv2.imwrite(file_name_path,face) # it writes the file(saves the file)
                cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),2) #for each image which was saved will be given by a name
                cv2.imshow("Frame", face) # to display the image

        key = cv2.waitKey(1) # it will wait for some time unless and unless user clicks escape key  
        if key == 27 or count==100:
            break

cap.release()
cv2.destroyAllWindows() # if we click escape it destroys all the windows