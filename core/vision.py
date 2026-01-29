import cv2
import face_recognition

def recognize_face():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()

    faces = face_recognition.face_locations(frame)
    if faces:
        return True
    return False

