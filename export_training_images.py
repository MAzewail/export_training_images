import cv2


v = cv2.VideoCapture("/content/my_video.mp4")


frameN = 0
while frameN <=3:
    s, frame = v.read()
    if s :
        path = '/content/drive/MyDrive/My_project/train/' + str(frameN) + '.jpg'
        print('creating...',path)
        cv2.imwrite(path, frame)
        frameN+=1

    else :
        break