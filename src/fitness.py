import cv2 as cv
import mediapipe as mp
import utils

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

coordinates_original = utils.parse_input('data/input.txt')


i = 0
# For webcam input:
cap = cv.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = pose.process(image)

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        # Flip the image horizontally for a selfie-view display.
        cv.imshow('MediaPipe Pose', cv.flip(image, 1))
        
        for curr in results.pose_landmarks.landmark:
            x,y,z,visibility = curr.x, curr.y,curr.z,curr.visibility
        
        for k in coordinates_original[i]:
            if (k == 'x'):
                x2 = coordinates_original[i][k]
            elif(k=='y'):
                y2 = coordinates_original[i][k]
            elif(k=='z'):
                z2 = coordinates_original[i][k]
            else:
                visibility2 = coordinates_original[i][k]

        print(x-x2)


        if cv.waitKey(5) & 0xFF == 27:
            break
        i += 1
cap.release()