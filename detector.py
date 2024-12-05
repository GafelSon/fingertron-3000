import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

vid = cv2.VideoCapture(0)

def find_hands(img, draw=True):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if draw:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    return img, results

def find_position(img, hand_landmarks, draw=True):
    lm_list = []
    h, w, c = img.shape
    for id, lm in enumerate(hand_landmarks.landmark):
        cx, cy = int(lm.x * w), int(lm.y * h)
        lm_list.append([id, cx, cy])
        if draw:
            cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
    return lm_list

finger_tips = [4, 8, 12, 16, 20]
while True:
    success, frame = vid.read()
    if not success:
        break

    frame, results = find_hands(frame)
    hands_up_count = []

    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            lm_list = find_position(frame, hand_landmarks, draw=False)
            if len(lm_list) < 21:
                continue

            fingers_status = []
            handedness = results.multi_handedness[idx].classification[0].label
            is_right_hand = handedness == "Right"

            if is_right_hand:
                thumb_up = lm_list[finger_tips[0]][1] < lm_list[finger_tips[0] - 1][1]
            else:
                thumb_up = lm_list[finger_tips[0]][1] > lm_list[finger_tips[0] - 1][1]
            fingers_status.append(1 if thumb_up else 0)

            for finger in range(1, 5):
                finger_up = lm_list[finger_tips[finger]][2] < lm_list[finger_tips[finger] - 2][2]
                fingers_status.append(1 if finger_up else 0)

            print(f"Hand {idx + 1} ({handedness}): Fingers status: {fingers_status}")
            hands_up_count.append(fingers_status.count(1))

    cv2.rectangle(frame, (10, 10), (200, 100), (0, 0, 255), cv2.FILLED)
    text = f"Count: {sum(hands_up_count) if hands_up_count else 0}"
    cv2.putText(frame, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv2.imshow("Finger Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
