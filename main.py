#https://www.youtube.com/watch?v=-4MPtERPq2E
import cv2 # Read image  /  camera / video input
from pyzbar.pyzbar import decode
import time
from datetime import datetime

#img =cv2.imread('multiple.png')
#print(decode(img))

cap = cv2.VideoCapture(0)
cap.set(3,640) #3 - width
cap.set(4,480) #4 - Height
used_codes=[]


camera = True
while camera == True:
    success, frame = cap.read()


    def markAttendance(code):
        with open('Attendance2.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
                if code not in nameList:
                    now = datetime.now()
                    dtString = now.strftime('%H:%M,%S')
                    f.writelines(f'\n{code},{dtString}')
                    #markAttendance(code)

    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print('Approved. You can enter!')
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(5)
            markAttendance(code)
        elif code.data.decode('utf-8') in used_codes:
            print('Sorry, this code has been already used!')
            time.sleep(5)
        else:
            pass






    cv2.imshow('Testing-code-scan', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

