import cv2
import mediapipe as mp
import math
import time
import winsound

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def calculate_EAR(landmarks, eye_indices, frame_width, frame_height):
    p1 = landmarks[eye_indices[0]]
    p2 = landmarks[eye_indices[1]]
    p3 = landmarks[eye_indices[2]]
    p4 = landmarks[eye_indices[3]]
    p5 = landmarks[eye_indices[4]]
    p6 = landmarks[eye_indices[5]]

    p1 = (int(p1.x * frame_width), int(p1.y * frame_height))
    p2 = (int(p2.x * frame_width), int(p2.y * frame_height))
    p3 = (int(p3.x * frame_width), int(p3.y * frame_height))
    p4 = (int(p4.x * frame_width), int(p4.y * frame_height))
    p5 = (int(p5.x * frame_width), int(p5.y * frame_height))
    p6 = (int(p6.x * frame_width), int(p6.y * frame_height))

    vertical1 = math.dist(p2, p6)
    vertical2 = math.dist(p3, p5)
    horizontal = math.dist(p1, p4)

    if horizontal == 0:
        return 0.0

    EAR = (vertical1 + vertical2) / (2.0 * horizontal)
    return EAR

LEFT_EYE_INDICES  = [33, 160, 158, 133, 153, 144]
RIGHT_EYE_INDICES = [362, 385, 387, 263, 373, 380]

cap = cv2.VideoCapture(0)

EYE_THRESHOLD     = 0.25
CLOSED_TIME_LIMIT = 3

eye_closed_start = None
alarm_on = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_rgb.flags.writeable = False
    results = face_mesh.process(frame_rgb)
    frame_rgb.flags.writeable = True

    frame_height, frame_width = frame.shape[:2]

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            left_ear  = calculate_EA