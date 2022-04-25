import cv2
import imutils
import pytesseract
import datetime

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'



image = cv2.imread(r'test\test18.JPG') #test4 test2 test12 test16 test18 test4.-3 test5 test8 test10 test11
image = imutils.resize(image, width=300 )
cv2.imshow("original image", image)
cv2.waitKey(0)


'''
cam = cv2.VideoCapture(0)
result, image = cam.read()

if result:
  
    cv2.imshow("test", image)
  
    cv2.imwrite("test.jpg", image)
  
    cv2.waitKey(0)
    cv2.destroyWindow("test")
else:
    print("No image detected. Please! try again")
'''

    

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("greyed image", gray_image)
cv2.waitKey(0)

gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17) 
cv2.imshow("smoothened image", gray_image)
cv2.waitKey(0)

edged = cv2.Canny(gray_image, 30, 200) 
cv2.imshow("edged image", edged)
cv2.waitKey(0)

cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image1=image.copy()
cv2.drawContours(image1,cnts,-1,(0,255,0),3)
cv2.imshow("contours",image1)
cv2.waitKey(0)

cnts = sorted(cnts, key = cv2.contourArea, reverse = True) [:30]
#screenCnt = None
screenCnt = 0
image2 = image.copy()
cv2.drawContours(image2,cnts,-1,(0,255,0),3)
cv2.imshow("Top 30 contours",image2)
cv2.waitKey(0)

i=7
for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4: 
                screenCnt = approx
        x,y,w,h = cv2.boundingRect(c) 
        new_img=image[y:y+h,x:x+w]
        cv2.imwrite('./'+str(i)+'.png',new_img)
        i+=1
        break


#cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("image with detected license plate", image)
cv2.waitKey(0)


Cropped_loc = './7.png'
cv2.imshow("cropped", cv2.imread(Cropped_loc))
plate = pytesseract.image_to_string(Cropped_loc, lang='eng')
print("Number plate is:", plate)
#num = 0
num = int(plate[-2])
#print(len(plate))
print(num)

'''
for element in plate:
    print(element, end='*')
print("\n")
'''

index = open("templates/index.html").read().format(p1=plate)

#Date
x = datetime.datetime.now()
date = x.strftime("%d")
date = int(date)
print(date)
if(date%2==0 and num%2!=0):
    print("Challan")
elif(date%2!=0 and num%2==0):
    print("Challan")
elif(date%2==0 and num%2==0):
    print("No Challan")
elif(date%2!=0 and num%2!=0):
    print("No Challan")



cv2.waitKey(0)
cv2.destroyAllWindows()




