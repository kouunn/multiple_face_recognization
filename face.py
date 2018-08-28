import cv2

# Haar-like特徴分類器の読み込み
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# イメージファイルの読み込み
img = cv2.imread('test.jpg')

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 顔を検知
faces = face_cascade.detectMultiScale(gray)
for (x,y,w,h) in faces:
    # 検知した顔を矩形で囲む
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    # 顔画像（グレースケール）
    roi_gray = gray[y:y+h, x:x+w]
    # 顔ｇ増（カラースケール）
    roi_color = img[y:y+h, x:x+w]



# 画像表示
cv2.imshow('img',img)

# 何かキーを押したら終了
cv2.waitKey(0)
cv2.destroyAllWindows()