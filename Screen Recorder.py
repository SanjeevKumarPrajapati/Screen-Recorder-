import cv2
import pyautogui
import numpy as np
#create resolution
resolution=pyautogui.size()
#file name in which we store recording
inp=input("Enter file path : ")
f=60.0
save=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter(inp,save,f,resolution)

#create recording module
cv2.namedWindow("Recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording",(600,400))

while True:
    img=pyautogui.screenshot()
    f=np.array(img)
    f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Recording",f)
    if cv2.waitKey(1)==ord("q"):
        break
output.release()
cv2.destroyAllWindows()
