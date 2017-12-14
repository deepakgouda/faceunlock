import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

# Uncomment the following two lines to capture your image for recognition.
# ret,img = video_capture.read()
# cv2.imwrite('user.jpg', img)

user_image = face_recognition.load_image_file("user.jpg")
user_face_encoding = face_recognition.face_encodings(user_image)[0]

access_file=open('access.txt','w')
access_file.write('Nope')

face_locations = []
face_encodings = []
face_names = []

frame=cv2.imread('user.jpg')

i=10
count=0
access=False
while i:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.33, fy=0.33)
    
    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        match = face_recognition.compare_faces([user_face_encoding], face_encoding)
        name = "Unknown"

        if match[0]:
            access=True

    i=i-1

access_file=open('access.txt','w')
access_file.write(str(access))
access_file.close()
video_capture.release()
cv2.destroyAllWindows()