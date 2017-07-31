import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/win-8/AppData/Local/Programs/Python/Python36/task/grids/task1_img_3.jpg',0)
digit=[]
d=[]

for i in range(0,12):
    digit.append(cv2.imread('C:/Users/win-8/AppData/Local/Programs/Python/Python36/task/digits/'+str(i)+'.jpg',0))

lst=[]

#here in place of 6, you can take the value of grid by seeing your grid
for i in range(6):
    for j in range(6):
        x=''
        if j==6-1:
            for l in d:
                if l==10:
                    l='-'
                elif l==11:
                    l='+'
                else:
                    l=str(l)
                x=x+l
            lst.append(eval(x))
            d=[]
                
        else:
            #100 because my image have grids with size 100*100
            #-5 helps to get rid of the black pixels present while croping the image, so is +5
            crop_img=img[100*i+5:100*(i+1)-5,100*j+5:100*(j+1)-5]
            for k in range(12):
                res = cv2.matchTemplate(digit[k],crop_img,cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                if max_val>0.9:
                    d.append(k)

m=list(map(str,lst))
print(m)
font=cv2.FONT_HERSHEY_SIMPLEX
k=0
for i in m:
    #if else condition is used to adjust the result with in the grid
    #520 and 70, i have taken by multiple trials
    if len(i)==1:
        cv2.putText(img, i, (520,70+k), font, 2.15, (0,0,0), 2, cv2.LINE_AA)
    else:
        cv2.putText(img, i, (500,70+k), font, 2.15, (0,0,0), 2, cv2.LINE_AA)
    k+=100

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
