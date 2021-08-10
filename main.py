import cv2

if __name__ == '__main__':
    img = cv2.imread("imagen1.jpg")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    invert = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(invert,(21,21),100)
    invertblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(gray,invertblur,scale=256.0)

    cv2.imwrite("imagen2.png",sketch)